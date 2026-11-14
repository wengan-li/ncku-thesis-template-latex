#!/usr/bin/env python3
"""Project existing teaching code into the portable English agent reference.

Only comment-delimited regions of existing TeX/BibTeX teaching inputs are read.
The PDF consumes those same regions as executable content or verbatim examples.
No translation, LaTeX parser, new handbook source or student build step is used.
"""
from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path('thesis/.agents/skills/ncku-thesis-writing/references/template-usage.md')
SOURCES = {
    'chapter-shapes': 'how-to/write/chapter/chapter.tex',
    'ordered-list': 'how-to/write/basic/list.tex',
    'unordered-list': 'how-to/write/basic/list.tex',
    'single-figure': 'how-to/write/figure/figure.tex',
    'multi-figure': 'how-to/write/figure/figure.tex',
    'table': 'how-to/write/table/table.tex',
    'equation': 'how-to/write/equation/equation.tex',
    'theorem-shapes': 'how-to/use/conf.tex',
    'reference-shapes': 'how-to/write/basic/label.tex',
    'nomenclature-shapes': 'how-to/write/nomenclature/nomenclature.tex',
    'abstract': 'abstract/eng.tex',
    'acknowledgments': 'acknowledgments/eng.tex',
    'appendix-open': 'appendix/appendix.tex',
    'appendix-close': 'appendix/appendix.tex',
    'citation': 'content-test/ref-cite.tex',
    'bibliography-entry': 'references/paper.bib',
    'bibliography-registration': 'references/references.tex',
    'direct-build': 'how-to/use/build/build.tex',
}


def region(root: Path, name: str) -> str:
    path = root / 'thesis/example' / SOURCES[name]
    text = path.read_text(encoding='utf-8')
    pattern = (rf'^% writing-snippet-begin: {re.escape(name)}\n(.*?)'
               rf'^% writing-snippet-end: {re.escape(name)}\s*$')
    matches = re.findall(pattern, text, re.M | re.S)
    if len(matches) != 1:
        raise ValueError(f'Missing or duplicate shared teaching region: {name}')
    return matches[0]


def code(root: Path, name: str) -> str:
    text = region(root, name)
    text = re.sub(r'\A\s*\\begin\{verbatim\}\s*\n', '', text)
    text = re.sub(r'\n[ \t]*\\end\{verbatim\}\s*\Z', '', text)
    # Strip TeX comments, preserving escaped percent signs. No prose translation.
    lines = []
    for line in text.splitlines():
        for match in re.finditer('%', line):
            prefix = line[:match.start()]
            if (len(prefix) - len(prefix.rstrip('\\'))) % 2 == 0:
                line = prefix
                break
        lines.append(line.rstrip())
    return textwrap.dedent('\n'.join(lines)).strip()


def command(root: Path, name: str, symbol: str) -> str:
    matches = [line.strip() for line in code(root, name).splitlines()
               if re.match(rf'^\s*\\{re.escape(symbol)}(?:\{{|$)', line)]
    if len(matches) != 1:
        raise ValueError(f'Expected one shared command: {name}/{symbol}')
    return matches[0]


def fragments(root: Path) -> list[tuple[str, str, str]]:
    """Finite projection: code-only selection and explicit placeholder binding.

    Bind illustrative values only, never translated text or guessed syntax.
    Title/NAME stay unchanged; empty caption placeholders receive Caption so their labels are numbered.
    """
    chapter = command(root, 'chapter-shapes', 'StartChapter')
    chapter_open = chapter.replace('{ Label }', '{shared:chapter-open}')
    sections = '\n'.join(command(root, 'chapter-shapes', symbol).replace('{ Label }', '{shared:' + key + '}')
                         for symbol, key in [('StartSection', 'section'),
                                             ('StartSubSection', 'subsection'),
                                             ('StartSubSubSection', 'subsubsection')])
    refs = []
    for symbol, label in [('RefEquation', 'eq:example:eq1'), ('RefEquationB', 'eq:example:eq1'),
                          ('RefBib', 'testpage:bib:paper:mapreduce'),
                          ('RefPage', 'shared:chapter-open'), ('RefTo', 'fig:little-man-no.1')]:
        found = re.findall(rf'\\{symbol}\{{\.\.\.\}}', region(root, 'reference-shapes'))
        if len(found) != 1:
            raise ValueError(f'Expected one shared reference shape: {symbol}')
        refs.append(found[0].replace('{...}', '{' + label + '}'))
    nom = code(root, 'nomenclature-shapes').replace('{ LABEL }', '{shared:nomenclature}')
    front = '\n'.join([code(root, 'abstract'), code(root, 'acknowledgments'), nom])
    appendix = '\n'.join([code(root, 'appendix-open'),
                          chapter.replace('{ Label }', '{shared:appendix}'), code(root, 'appendix-close')])
    build = re.fullmatch(r'\\verb\|([^|]+)\|', code(root, 'direct-build'))
    if build is None:
        raise ValueError('Expected the shared direct-build verb command')
    return [
        ('chapter-open', 'latex', chapter_open),
        ('sections', 'latex', sections),
        ('chapter-close', 'latex', command(root, 'chapter-shapes', 'EndChapter')),
        ('front-matter', 'latex', front),
        ('appendix', 'latex', appendix),
        ('basic-text', 'latex', code(root, 'ordered-list') + '\n' + code(root, 'unordered-list')),
        ('figure', 'latex', code(root, 'single-figure').replace('{./figure.png}', '{./context/pilot/figure.png}')),
        ('multi-figure', 'latex', re.sub(r'caption = \{\s*\}', 'caption = {Caption}', code(root, 'multi-figure')).replace('{./figure.png}', '{./context/pilot/figure.png}')),
        ('table', 'latex', code(root, 'table')),
        ('equation', 'latex', code(root, 'equation')),
        ('theorems', 'latex', '\n'.join(command(root, 'theorem-shapes', symbol)
                                      for symbol in ['InsertTheorem', 'InsertProof'])),
        ('references', 'latex', '\n'.join(refs)),
        ('citation', 'latex', code(root, 'citation')),
        ('bibliography-entry', 'bibtex', code(root, 'bibliography-entry')),
        ('bibliography-registration', 'latex', code(root, 'bibliography-registration').replace('{example/', '{context/')),
        ('direct-build', 'bash', build[1]),
    ]


def render(root: Path) -> str:
    output = ['<!-- generated: shared teaching projection; do not edit -->', '',
              '# Template usage fragments', '',
              'These fragments are generated from the teaching code, not a second handbook. '
              'Replace illustrative titles, labels and data with supplied thesis material. '
              'Paths are relative to the matching student project root. Supply an image at '
              '`./context/pilot/figure.png` before using the figure fragments. Read the skill for assembly, '
              'edit boundaries, compilation and recovery. The teaching corpus and generator '
              'are not needed to read or compile this reference.', '']
    for name, language, body in fragments(root):
        if re.search(r'[\u3400-\u9fff]', body):
            raise ValueError(f'Projected fragment contains non-English prose: {name}')
        output.extend([f'## {name.replace("-", " ").capitalize()}', '',
                       f'<!-- student-snippet: {name} -->', f'```{language}', body, '```', ''])
    return '\n'.join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail without writing if projection is stale')
    parser.add_argument('--root', type=Path, default=ROOT, help='repository or isolated test fixture root')
    args = parser.parse_args()
    try:
        expected = render(args.root)
        destination = args.root / OUTPUT
        if args.check:
            if not destination.is_file() or destination.read_text(encoding='utf-8') != expected:
                print('Generated writing reference drift: run just writing-reference', file=sys.stderr)
                return 1
            print('Shared teaching projection PASS: template-usage.md is current')
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(expected, encoding='utf-8')
            print('Generated writing reference: ' + str(OUTPUT))
    except (OSError, ValueError) as error:
        print('Shared teaching projection FAIL: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
