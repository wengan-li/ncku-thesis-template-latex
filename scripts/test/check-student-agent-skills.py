#!/usr/bin/env python3
"""Check portable student knowledge; compile the published snippets themselves.

Default: source contracts and negative mutations. --build adds a cold pilot and
copied-context build. --project validates an extracted project; --context checks
readable content without claiming that a template runtime exists.
Only the Python standard library is required. Build logs remain under build/.
"""

from __future__ import annotations

import argparse
import json
import importlib.util
import shlex
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[2]
SKILL = Path('.agents/skills/ncku-thesis-writing')
REFERENCE = SKILL / 'references/template-usage.md'
GENERATOR = ROOT / 'scripts/docs/generate-writing-reference.py'
ALIASES = ('CLAUDE.md', 'context/CLAUDE.md')
LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
CJK = re.compile(r'[\u3400-\u9fff]')
SNIPPET = re.compile(r'<!-- student-snippet: ([a-z-]+) -->\n```(\w+)\n(.*?)\n```', re.S)
BAD_LOG = re.compile(r'undefined (?:references|citations)|Citation .+ undefined|'
                     r'Reference .+ undefined|Rerun to get|Label\(s\) may have changed|'
                     r'There were multiply-defined labels', re.I)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def alias(directory: Path) -> None:
    path = directory / 'CLAUDE.md'
    require(path.is_symlink(), f'alias must be a symlink: {path}')
    require(os.readlink(path) == 'AGENTS.md', f'alias target must be relative AGENTS.md: {path}')
    require(path.resolve() == (directory / 'AGENTS.md').resolve(), f'alias escapes its directory: {path}')
    require(path.read_bytes() == (directory / 'AGENTS.md').read_bytes(), f'alias resolved content differs: {path}')


def english_agent(path: Path) -> None:
    require(CJK.search(path.read_text(encoding='utf-8')) is None,
            f'agent instructions must be English only: {path}')


def has_runtime(directory: Path) -> bool:
    return ((directory / 'thesis.tex').is_file() and (directory / 'conf').is_dir()
            and (directory / 'template/configure.tex').is_file())


def verified_repository_root(directory: Path) -> bool:
    try:
        result = subprocess.run(['git', '-C', str(directory), 'rev-parse', '--show-toplevel'],
                                capture_output=True, text=True)
    except OSError:
        return False
    return result.returncode == 0 and Path(result.stdout.strip()).resolve() == directory.resolve()


def find_project(cwd: Path, target: Path | None = None) -> Path | None:
    """Mirror the student instructions without searching unrelated directories.

    An explicit orphan target cannot borrow a runtime from cwd. A verified
    repository root is the only place where a child directory is considered.
    """
    cwd = cwd.resolve()
    origin = (target if target.is_absolute() else cwd / target).resolve() if target is not None else cwd
    for directory in (origin, *origin.parents):
        if has_runtime(directory):
            return directory
    if verified_repository_root(origin) and has_runtime(origin / 'thesis'):
        return origin / 'thesis'
    return None


def check_context(context: Path) -> None:
    base = context / SKILL
    required = ['README.md', 'README.en.md', 'AGENTS.md', str(SKILL / 'SKILL.md')]
    required += [str(REFERENCE)]
    require(not (context / 'usage').exists(), 'duplicate usage handbook must not be packaged')
    for relative in required:
        path = context / relative
        require(path.is_file() and not path.is_symlink(), f'missing regular payload file: {relative}')
    for path in (context / '.agents').rglob('*'):
        if path.is_file() or path.is_symlink():
            require(path.is_relative_to(base), f'unapproved student skill: {path}')
    alias(context)
    english_agent(context / 'AGENTS.md')
    skill = (base / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    require(front is not None, 'missing skill frontmatter')
    require(all(re.fullmatch(r'(name|description): [^\n]+', line)
                for line in front[1].splitlines()), 'unsupported skill frontmatter')
    fields = dict(line.split(': ', 1) for line in front[1].splitlines() if ': ' in line)
    require(len(front[1].splitlines()) == len(fields) == 2, 'duplicate or missing frontmatter fields')
    require(fields.get('name') == 'ncku-thesis-writing', 'wrong skill name')
    require(bool(fields.get('description', '').strip()), 'missing skill description')
    require('references/template-usage.md' in skill, 'unrouted generated reference')
    for path in ([context / name for name in ('README.md', 'README.en.md', 'AGENTS.md')]
                 + list(base.rglob('*'))):
        if path.is_dir():
            continue
        require(not path.is_symlink(), f'payload dependency is a symlink: {path}')
        require(path.suffix == '.md', f'unexpected payload file: {path}')
        if path.is_relative_to(base):
            english_agent(path)
            require('example/' not in path.read_text(), f'nonportable teaching dependency: {path}')
        text = path.read_text(encoding='utf-8')
        for forbidden in ('/Users/', 'scripts/test/', 'just test', 'codegraph explore',
                          'docs/features/', '.claude/settings', 'mcpServers'):
            require(forbidden not in text, f'nonportable dependency {forbidden}: {path}')
        for raw in LINK.findall(text):
            target = urllib.parse.unquote(raw.strip('<>'))
            parts = urllib.parse.urlsplit(target)
            require(not parts.scheme and not parts.netloc, f'nonlocal dependency: {target}')
            require(not parts.path.startswith(('/', '\\')) and '\\' not in parts.path,
                    f'unsafe path: {target}')
            destination = (path.parent / parts.path).resolve()
            require(destination.is_relative_to(context.resolve()), f'escaping dependency: {target}')
            require(destination.is_file(), f'missing sidecar: {target}')
    print(f'Student context payload PASS: {context}')


def check_project(project: Path) -> None:
    require(has_runtime(project),
            'A matching complete thesis template containing thesis.tex, conf/ and '
            'template/configure.tex is required.')
    require((project / 'AGENTS.md').is_file(), 'missing student project router')
    english_agent(project / 'AGENTS.md')
    require(not (project / '.agents').exists(), 'repository skills leaked into student root')
    for path in project.rglob('AGENTS.md'):
        require(path.relative_to(project).as_posix() in ('AGENTS.md', 'context/AGENTS.md'),
                f'unapproved agent router: {path}')
    alias(project)
    check_context(project / 'context')


def check_zip(archive: Path, prefix: str) -> None:
    """Check representation and bytes without confusing symlink data with text."""
    with ZipFile(archive) as zf:
        names = zf.namelist()
        require(len(names) == len(set(names)), 'duplicate ZIP entries')
        for item in zf.infolist():
            path = PurePosixPath(item.filename)
            require(not path.is_absolute() and '..' not in path.parts and '\\' not in item.filename,
                    f'unsafe ZIP path: {item.filename}')
            require(item.filename.startswith(prefix), f'path outside ZIP root: {item.filename}')
            relative = item.filename[len(prefix):]
            if '.agents' in PurePosixPath(relative).parts:
                require(relative in ('context/.agents/', 'context/.agents/skills/') or
                        relative.startswith('context/.agents/skills/ncku-thesis-writing/'),
                        f'unapproved ZIP skill tree: {relative}')
            mode = item.external_attr >> 16
            if stat.S_ISLNK(mode):
                require(relative in ALIASES, f'unexpected ZIP symlink: {relative}')
                require(zf.read(item) == b'AGENTS.md', f'wrong ZIP alias target: {relative}')
            if relative in ALIASES:
                require(stat.S_ISLNK(mode), f'ZIP alias lost symlink mode: {relative}')
            if relative.endswith(('AGENTS.md', 'CLAUDE.md')):
                require(relative in ('AGENTS.md', 'context/AGENTS.md') + ALIASES,
                        f'unapproved agent router: {relative}')
            require(not any(part in {'.codegraph', '.git', '.claude'} for part in path.parts),
                    f'local state in ZIP: {item.filename}')
        for relative in ALIASES + ('context/' + str(SKILL / 'SKILL.md'),):
            require(prefix + relative in names, f'missing ZIP payload: {relative}')
        # Extract only after paths and symlink payloads were checked. Python's
        # zipfile does not restore symlinks; Info-ZIP does and is the public gate.
        with tempfile.TemporaryDirectory(prefix='student-alias-') as temporary:
            subprocess.run(['unzip', '-q', str(archive.resolve()), '-d', temporary], check=True)
            check_project(Path(temporary) / prefix)
    print(f'Student ZIP aliases and extracted payload PASS: {archive}')


def published(context: Path) -> dict[str, str]:
    snippets: dict[str, str] = {}
    for name, _, code in SNIPPET.findall((context / REFERENCE).read_text(encoding='utf-8')):
        require(name not in snippets, f'duplicate generated snippet: {name}')
        snippets[name] = code
    return snippets


def projection_module():
    spec = importlib.util.spec_from_file_location('writing_projection', GENERATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generation_contracts() -> None:
    generator = projection_module()
    with tempfile.TemporaryDirectory(prefix='writing-generation-') as temporary:
        fixture = Path(temporary)
        for name in set(generator.SOURCES.values()):
            target = fixture / 'thesis/example' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / 'thesis/example' / name, target)

        def run(check: bool, expected: int, diagnostic: str) -> None:
            command = [sys.executable, str(GENERATOR), '--root', str(fixture)]
            if check:
                command.append('--check')
            result = subprocess.run(command, capture_output=True, text=True)
            require(result.returncode == expected and diagnostic in result.stdout + result.stderr,
                    f'projection mutation failed for wrong reason: {result.stdout}{result.stderr}')

        run(False, 0, 'Generated writing reference:')
        run(True, 0, 'Shared teaching projection PASS:')
        source_files = {Path('thesis/example') / name for name in set(generator.SOURCES.values())}
        actual_files = {path.relative_to(fixture) for path in fixture.rglob('*') if path.is_file()}
        require(actual_files - source_files == {generator.OUTPUT}, 'unexpected generated artifact')
        output = fixture / generator.OUTPUT
        output.write_text(output.read_text() + '\nStale generated bytes.\n')
        run(True, 1, 'Generated writing reference drift:')
        print('Student negative PASS: stale generated reference')
        run(False, 0, 'Generated writing reference:')
        source = fixture / 'thesis/example/how-to/write/figure/figure.tex'
        source.write_text(source.read_text().replace('Little man No.1', 'Changed canonical caption', 1))
        run(True, 1, 'Generated writing reference drift:')
        run(False, 0, 'Generated writing reference:')
        require('Changed canonical caption' in output.read_text(), 'canonical change did not flow into reference')
        run(True, 0, 'Shared teaching projection PASS:')
        print('Student negative PASS: changed canonical teaching source')
        print('Student positive PASS: deterministic regeneration follows teaching bytes')


def source_contract() -> tuple[dict, dict[str, str]]:
    check_project(ROOT / 'thesis')
    require(find_project(ROOT) == ROOT / 'thesis', 'repository-root discovery missed thesis/ child')
    for target in (Path('thesis/context'), Path('thesis/context/introduction/introduction.tex')):
        require(find_project(ROOT, target) == ROOT / 'thesis', f'target-content discovery failed: {target}')
    require(find_project(ROOT / 'thesis/context', Path('introduction/introduction.tex')) == ROOT / 'thesis',
            'nested relative target discovery failed')
    print('Student positive PASS: repository root, target content file/directory and nested cwd discovery')
    manifest = json.loads((ROOT / 'tests/802-student-usage.json').read_text())
    require(manifest.get('schema') == 2, 'unsupported shared-source manifest schema')
    generated = projection_module().render(ROOT)
    require((ROOT / 'thesis/context' / REFERENCE).read_text() == generated,
            'Generated writing reference drift: run just writing-reference')
    snippets = published(ROOT / 'thesis/context')
    require(set(snippets) == set(manifest['snippets']), 'published snippet inventory drift')
    source = (ROOT / manifest['bibliography_source']).read_text()
    require(snippets['bibliography-entry'] in source, 'published bibliography entry differs from supplied source')
    require(snippets['bibliography-registration'] in (ROOT / 'thesis/context/references/references.tex').read_text(),
            'published database registration differs from student source')
    return manifest, snippets


def negative_contracts() -> None:
    """Mutate copies, and require the intended diagnostic for each failure."""
    cases = ('entrypoint', 'sidecar', 'frontmatter', 'absolute', 'escape', 'alias-file',
             'alias-target', 'hidden', 'maintenance-skill', 'chinese-skill',
             'chinese-sidecar', 'chinese-context-router', 'duplicate-handbook')
    with tempfile.TemporaryDirectory(prefix='student-negatives-') as temporary:
        for case in cases:
            context = Path(temporary) / case
            shutil.copytree(ROOT / 'thesis/context', context, symlinks=True)
            base = context / SKILL
            expected = ''
            if case == 'entrypoint':
                (base / 'SKILL.md').unlink(); expected = 'missing regular payload'
            elif case == 'sidecar':
                (context / REFERENCE).unlink(); expected = 'missing regular payload'
            elif case == 'frontmatter':
                path = base / 'SKILL.md'
                path.write_text(path.read_text().replace('name: ncku-thesis-writing', 'name: wrong-name'))
                expected = 'wrong skill name'
            elif case in ('absolute', 'escape'):
                with (base / 'SKILL.md').open('a') as stream:
                    stream.write('\n[bad](/etc/passwd)\n' if case == 'absolute' else '\n[bad](../../../../../../outside.md)\n')
                expected = 'unsafe path' if case == 'absolute' else 'escaping dependency'
            elif case.startswith('alias'):
                (context / 'CLAUDE.md').unlink()
                if case == 'alias-file':
                    (context / 'CLAUDE.md').write_text((context / 'AGENTS.md').read_text())
                    expected = 'alias must be a symlink'
                else:
                    (context / 'CLAUDE.md').symlink_to('../AGENTS.md'); expected = 'alias target'
            elif case == 'hidden':
                shutil.rmtree(context / '.agents'); expected = 'missing regular payload'
            elif case == 'maintenance-skill':
                path = context / '.agents/skills/repo-maintenance/SKILL.md'
                path.parent.mkdir()
                path.write_text('Repository maintenance instructions')
                expected = 'unapproved student skill'
            elif case == 'duplicate-handbook':
                (context / 'usage').mkdir()
                expected = 'duplicate usage handbook'
            else:
                path = (base / 'SKILL.md' if case == 'chinese-skill' else
                        base / 'sidecar.md' if case == 'chinese-sidecar' else context / 'AGENTS.md')
                with path.open('a', encoding='utf-8') as stream:
                    stream.write('\n學生寫作指示。\n')
                expected = 'English only'
            try:
                check_context(context)
            except AssertionError as error:
                require(expected in str(error), f'{case}: wrong failure: {error}')
            else:
                raise AssertionError(f'negative mutation unexpectedly passed: {case}')
            print(f'Student negative PASS: {case}')
        # Chinese belongs in human guides and remains a supported positive case.
        require(CJK.search((ROOT / 'thesis/context/README.md').read_text()) is not None,
                'Traditional-Chinese human guide is missing')
        print('Student positive PASS: Chinese human guide outside .agents')
        project = Path(temporary) / 'chinese-project-router'
        shutil.copytree(ROOT / 'thesis/context', project / 'context', symlinks=True)
        (project / 'conf').mkdir()
        (project / 'template').mkdir()
        (project / 'template/configure.tex').write_text('runtime sentinel')
        (project / 'thesis.tex').write_text('entry sentinel')
        (project / 'AGENTS.md').write_text('學生寫作指示。')
        (project / 'CLAUDE.md').symlink_to('AGENTS.md')
        try:
            check_project(project)
        except AssertionError as error:
            require('English only' in str(error), f'wrong project-router language diagnostic: {error}')
        else:
            raise AssertionError('Chinese project router unexpectedly passed')
        print('Student negative PASS: chinese-project-router')
        orphan = Path(temporary) / 'orphan/context'
        shutil.copytree(ROOT / 'thesis/context', orphan, symlinks=True)
        check_context(orphan)
        require(find_project(orphan) is None, 'orphan content unexpectedly discovered a runtime')
        require(find_project(ROOT, orphan / 'context.tex') is None,
                'explicit orphan target borrowed the repository runtime')
        unverified = Path(temporary) / 'unverified'
        (unverified / 'thesis/conf').mkdir(parents=True)
        (unverified / 'thesis/template').mkdir()
        (unverified / 'thesis/thesis.tex').write_text('entry sentinel')
        (unverified / 'thesis/template/configure.tex').write_text('runtime sentinel')
        require(find_project(unverified) is None, 'unverified directory searched its thesis/ child')
        print('Student negative PASS: unverified child runtime')
        try:
            check_project(orphan.parent)
        except AssertionError as error:
            require('matching complete thesis template' in str(error), 'wrong missing-runtime diagnostic')
        else:
            raise AssertionError('context-only copy unexpectedly has a runtime')
        print('Student negative PASS: missing matching runtime')
        # These malformed archives fail before extraction; a valid actual
        # git-archive ZIP is checked separately by the required release gate.
        for case, mode, data, expected in (
            ('zip-alias-mode', stat.S_IFREG | 0o644, b'AGENTS.md', 'lost symlink mode'),
            ('zip-alias-escape', stat.S_IFLNK | 0o777, b'../../AGENTS.md', 'wrong ZIP alias target'),
        ):
            archive = Path(temporary) / (case + '.zip')
            with ZipFile(archive, 'w') as zf:
                item = ZipInfo('ncku-thesis-template-latex/CLAUDE.md')
                item.create_system = 3
                item.external_attr = mode << 16
                zf.writestr(item, data)
            try:
                check_zip(archive, 'ncku-thesis-template-latex/')
            except AssertionError as error:
                require(expected in str(error), f'{case}: wrong failure: {error}')
            else:
                raise AssertionError(f'bad ZIP alias unexpectedly passed: {case}')
            print(f'Student negative PASS: {case}')


def validate_build(project: Path, manifest: dict) -> None:
    check_project(project)
    result = subprocess.run(shlex.split(published(project / 'context')['direct-build']),
                            cwd=project, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (project / 'pilot-build.log').write_bytes(result.stdout)
    require(result.returncode == 0, f'published pilot build failed; see {project}/pilot-build.log')
    require((project / 'thesis.pdf').stat().st_size > 0 and (project / 'thesis.synctex.gz').stat().st_size > 0,
            'pilot lacks PDF/SyncTeX')
    log = (project / 'thesis.log').read_text(errors='replace')
    require(not BAD_LOG.search(log), f'pilot did not converge: {project}')
    recorder = project / 'thesis.fls'
    require(recorder.is_file() and recorder.stat().st_size > 0, 'pilot recorder is missing')
    require(not (project / 'example').exists(), 'portable pilot unexpectedly contains teaching corpus')
    require(not any('example/' in line or '.agents/' in line
                    for line in recorder.read_text().splitlines() if line.startswith('INPUT ')),
            'portable pilot loaded teaching or agent instructions as runtime input')
    aux = (project / 'thesis.aux').read_text()
    for label in manifest['labels']:
        require('\\newlabel{' + label + '}' in aux, f'published label missing: {label}')
    require('\\bibcite{testpage:bib:paper:mapreduce}' in aux, 'published citation did not resolve')
    subprocess.run(['pdftotext', '-layout', 'thesis.pdf', 'pilot.txt'], cwd=project, check=True)
    text = ' '.join((project / 'pilot.txt').read_text().split())
    for value in manifest['text']:
        require(value in text, f'published pilot PDF lacks: {value}')
    require('??' not in text, 'unresolved visible reference in pilot')
    print(f'Published pilot PDF/text/labels/citation convergence PASS: {project}')


def build_pilot(source_project: Path, output: Path, manifest: dict) -> None:
    require(not output.exists(), f'pilot output already exists: {output}')
    project = output / 'project'
    shutil.copytree(source_project, project, symlinks=True,
                    ignore=shutil.ignore_patterns('example', '*.aux', '*.log', '*.bbl', '*.blg', '*.fdb_latexmk',
                                                  '*.fls', '*.synctex.gz', '*.toc', '*.lof', '*.lot', '*.out', '*.xdv'))
    snippets = published(project / 'context')
    config = project / 'conf/conf.tex'
    text = config.read_text()
    require(text.count('\n\\ExampleMode\n') == 1, 'unexpected shipped content-mode declaration')
    # Only the disposable project is changed, following the student guide.
    config.write_text(text.replace('\n\\ExampleMode\n', '\n%\\ExampleMode\n'))
    pilot = project / 'context/pilot'
    pilot.mkdir()
    shutil.copyfile(ROOT / manifest['image_source'], pilot / 'figure.png')
    (pilot / 'pilot.tex').write_text('\n'.join(snippets[name] for name in manifest['body']) + '\n')
    (project / 'context/references/paper.bib').write_text(snippets['bibliography-entry'] + '\n')
    # Keep the standard front-matter/chapter/bibliography/appendix order while
    # using the exact published code, without unrelated placeholder citations.
    (project / 'context/context.tex').write_text(
        '\\DisplayInnerCover\n' + snippets['front-matter'] + '\n\\DisplayIndex\n'
        '\\input{./context/pilot/pilot}\n' + snippets['bibliography-registration'] + '\n' + snippets['appendix'] + '\n')
    validate_build(project, manifest)
    copied = output / 'copied'
    shutil.copytree(project, copied, symlinks=True,
                    ignore=shutil.ignore_patterns('context', 'thesis.*', 'pilot*'))
    # Restore the immutable entry point; directory copy includes hidden skills
    # and preserves relative aliases. The matching runtime is a separate copy.
    shutil.copyfile(source_project / 'thesis.tex', copied / 'thesis.tex')
    shutil.copytree(project / 'context', copied / 'context', symlinks=True)
    validate_build(copied, manifest)
    # Corrupt a published label reference. TeX may exit 0 but convergence must fail.
    content = copied / 'context/pilot/pilot.tex'
    content.write_text(content.read_text().replace('\\RefTo{fig:little-man-no.1}', '\\RefTo{fig:missing-pilot}'))
    try:
        validate_build(copied, manifest)
    except AssertionError as error:
        require('did not converge' in str(error), f'wrong corrupted-label failure: {error}')
    else:
        raise AssertionError('corrupted published label unexpectedly passed')
    print('Student negative PASS: corrupted published reference')
    content.write_text(content.read_text().replace('\\RefTo{fig:missing-pilot}', '\\RefTo{fig:little-man-no.1}'))
    validate_build(copied, manifest)
    content.write_text(content.read_text().replace('\\RefBib{testpage:bib:paper:mapreduce}',
                                                 '\\RefBib{missing-supplied-source}'))
    try:
        validate_build(copied, manifest)
    except AssertionError:
        require(BAD_LOG.search((copied / 'thesis.log').read_text(errors='replace')) is not None,
                'corrupted citation failed for an unrelated reason')
    else:
        raise AssertionError('corrupted published citation unexpectedly passed')
    print('Student negative PASS: corrupted published citation')
    content.write_text(content.read_text().replace('\\RefBib{missing-supplied-source}',
                                                 '\\RefBib{testpage:bib:paper:mapreduce}'))
    validate_build(copied, manifest)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path)
    parser.add_argument('--context', type=Path)
    parser.add_argument('--zip', type=Path)
    parser.add_argument('--prefix', default='ncku-thesis-template-latex/')
    parser.add_argument('--build', action='store_true')
    parser.add_argument('--source-project', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT / 'build/tests/student-usage')
    args = parser.parse_args()
    try:
        if args.zip:
            check_zip(args.zip, args.prefix)
        elif args.project:
            check_project(args.project)
        elif args.context:
            check_context(args.context)
        else:
            manifest, _ = source_contract()
            generation_contracts()
            negative_contracts()
            if args.build:
                build_pilot(args.source_project or ROOT / 'thesis', args.output, manifest)
    except (AssertionError, OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f'Student agent skills FAIL: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
