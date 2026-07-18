#!/usr/bin/env python3
"""Verify focused figure, multi-figure, and table compatibility behavior."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Float contract FAIL: {message}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("build_dir", type=Path)
    args = parser.parse_args()

    stem = args.build_dir / "float-contract"
    log = stem.with_suffix(".log").read_text(errors="replace")
    text = stem.with_suffix(".txt").read_text(errors="replace")
    aux = stem.with_suffix(".aux").read_text(errors="replace")
    fls = stem.with_suffix(".fls").read_text(errors="replace")
    pdfinfo = stem.with_suffix(".pdfinfo").read_text(errors="replace")
    images = stem.with_suffix(".images").read_text(errors="replace")
    compact_log = "".join(log.split())
    normalized_text = " ".join(text.split())

    state_markers = (
        "NCKU-FLOAT-SINGLE-STATE:2.0/5/FloatSingleCaption/ncku:float:single/tbp/left/0.7",
        "NCKU-FLOAT-MULTI-STATE:3/FloatMultiCaption/ncku:float:multi/right/0.6",
        "NCKU-FLOAT-TABLE-TOP-STATE:0.0/FloatTableTopCaption/ncku:float:table-top/top/3pt/1.2/0.5",
        "NCKU-FLOAT-TABLE-BOTTOM-STATE:0.4/FloatTableBottomCaption/ncku:float:table-bottom/bottom/2pt/0.8/0.3",
        "NCKU-FLOAT-TABLE-STAR-STATE:0.0/FloatTableStarTitle/ncku:float:table-star/top/0.2",
        "NCKU-TABLE-KEY-DEFAULTS:0.0////top/6pt/1/0.4",
        "NCKU-TABLE-KEY-EXPANDED:0.55/ExpandedNomTitle/ExpandedCaption/ncku:table-expanded/bottom/4pt/1.4/0.85",
        "NCKU-TABLE-KEY-RESET:0.0////top/6pt/1/0.4",
        "NCKU-FIGURE-KEY-DEFAULTS:1.0/0///H//0.4",
        "NCKU-FIGURE-KEY-EXPANDED:1.75/15/ExpandedCaption/ncku:expanded/ignored-pos/ignored-align/0.9",
        "NCKU-FIGURE-KEY-RESET:1.0/0///H//0.4",
        "NCKU-MULTI-KEY-DEFAULTS:1////0.4",
        "NCKU-MULTI-KEY-EXPANDED:4/ExpandedMultiCaption/ncku:multi-expanded/ignored-multi-align/0.95",
        "NCKU-MULTI-KEY-PARTIAL:1/PartialMulti///0.4",
        "NCKU-MULTI-KEY-OMITTED:1////0.4",
        "NCKU-SUBFIGURE-KEY-DEFAULTS:1.0/0///",
        "NCKU-SUBFIGURE-KEY-EXPANDED:1.8/25/ExpandedSubCaption/ncku:sub-expanded/ignored-sub-align",
        "NCKU-SUBFIGURE-KEY-PARTIAL:1.0/0/PartialSub//",
        "NCKU-SUBFIGURE-KEY-OMITTED:1.0/0///",
        "NCKU-MULTI-ROW-ONE:A",
        "NCKU-MULTI-ROW-ONE:B",
        "NCKU-MULTI-ROW-TWO:C+D",
        "NCKU-MULTI-ROW-ONE:E",
        "NCKU-MULTI-ROW-THREE:F+G+H",
        "NCKU-MULTI-ROW-TWO:I+J",
        "NCKU-MULTI-ROW-FOUR:K+L+M+N",
        "NCKU-MULTI-ROW-TWO:O+P",
    )
    for marker in state_markers:
        require(marker in compact_log, f"missing key-state marker: {marker}")
    require(
        "NCKU-TEST-PASS:focusedfloatcontractcompiled" in compact_log,
        "missing pass marker",
    )

    forbidden = (
        r"undefined references",
        r"Rerun to get (cross-references|outlines) right",
        r"Undefined control sequence",
        r"destination with the same identifier",
        r"Token not allowed in a PDF string",
        r"Overfull \\hbox",
        r"Underfull \\hbox",
    )
    for warning in forbidden:
        require(re.search(warning, log, re.IGNORECASE) is None, f"log contains {warning}")

    require(re.search(r"^Pages:\s+1$", pdfinfo, re.MULTILINE) is not None, "PDF is not one page")
    require(re.search(r"^Page size:.*A4", pdfinfo, re.MULTILINE) is not None, "PDF is not A4")

    visible_fragments = (
        "Figure 1.1: Float Single Caption",
        "(a) Float Sub A",
        "(b) Float Sub B",
        "(c) Float Sub C",
        "Figure 1.2: Float Multi Caption",
        "Table 1.1: Float Table Top Caption",
        "TOP-A TOP-B TOP-C TOP-D",
        "BOTTOM-A BOTTOM-B BOTTOM-C BOTTOM-D BOTTOM-E BOTTOM-F",
        "Table 1.2: Float Table Bottom Caption",
        "Float Table Star Title",
        "STAR-A STAR-B",
        "References: 1.1, 1.2, 1.2a, 1.2b, 1.2c, 1.1, 1.2.",
    )
    for fragment in visible_fragments:
        require(fragment in normalized_text, f"missing visible fragment: {fragment}")

    names = (
        "Float Single Caption",
        "Float Multi Caption",
        "Float Sub A",
        "Float Sub B",
        "Float Sub C",
        "Float Table Top Caption",
        "Float Table Bottom Caption",
        "Float Table Star Title",
    )
    names_region = normalized_text.split("Names:", 1)[1]
    for name in names:
        require(name in names_region, f"nameref title missing: {name}")

    require(
        normalized_text.index("Table 1.1: Float Table Top Caption")
        < normalized_text.index("TOP-A TOP-B"),
        "top table caption moved below content",
    )
    require(
        normalized_text.index("BOTTOM-A BOTTOM-B BOTTOM-C")
        < normalized_text.index("Table 1.2: Float Table Bottom Caption"),
        "bottom table caption moved above content",
    )
    require(
        normalized_text.index("Float Table Star Title")
        < normalized_text.index("STAR-A STAR-B"),
        "star table title moved below content",
    )

    labels = {
        "ncku:float:single": ("1.1", "Float Single Caption"),
        "ncku:float:multi": ("1.2", "Float Multi Caption"),
        "ncku:float:sub-a": ("1.2a", "Float Sub A"),
        "ncku:float:sub-b": ("1.2b", "Float Sub B"),
        "ncku:float:sub-c": ("1.2c", "Float Sub C"),
        "ncku:float:table-top": ("1.1", "Float Table Top Caption"),
        "ncku:float:table-bottom": ("1.2", "Float Table Bottom Caption"),
    }
    for label, (number, title) in labels.items():
        pattern = rf"\\newlabel\{{{re.escape(label)}\}}\{{\{{{re.escape(number)}\}}\{{i\}}\{{{re.escape(title)}\}}"
        require(re.search(pattern, aux) is not None, f"incorrect label metadata: {label}")
    require(
        re.search(r"\\newlabel\{ncku:float:table-star\}.*\{Float Table Star Title\}", aux)
        is not None,
        "star table title metadata is missing",
    )
    require("TmpValueCaption" not in aux, "mutable single/table caption leaked into aux")
    require("TmpMIValueCaption" not in aux, "mutable multi caption leaked into aux")
    require("TmpMISubValueCaption" not in aux, "scoped subcaption leaked into aux")

    image_rows = re.findall(r"^\s+\d+\s+\d+\s+image\s+", images, re.MULTILINE)
    smask_rows = re.findall(r"^\s+\d+\s+\d+\s+smask\s+", images, re.MULTILINE)
    require(len(image_rows) == 4, f"expected 4 embedded image rows, got {len(image_rows)}")
    require(len(smask_rows) == 4, f"expected 4 alpha-mask rows, got {len(smask_rows)}")
    for asset in (
        "INPUT ./example/how-to/write/figure/pic/CC-BY-NC.png",
        "INPUT ./example/how-to/write/figure/pic/CC-BY-NC-ND.png",
    ):
        require(asset in fls, f"missing recorded image asset: {asset}")

    figure_source = Path("thesis/template/command/cmd-figure.tex").read_text()
    figures_source = Path("thesis/template/command/cmd-figures.tex").read_text()
    table_source = Path("thesis/template/command/cmd-table.tex").read_text()
    require(r"\begin{figure}[H]" in figure_source, "single figure no longer forces H")
    require(r"\begin{figure}[H]" in figures_source, "multi figure no longer forces H")
    require(r"\begin{table}[H]" in table_source, "table no longer forces H")
    require(
        r"\keys_define:nn { ncku / insert-figure }" in figure_source,
        "single-figure keys no longer use the bounded l3keys family",
    )
    require(
        figure_source.count(".tl_set_e:N") == 7,
        "single-figure l3keys family no longer has seven expanded-storage keys",
    )
    require(
        "/InsertFigure/.is family" not in figure_source,
        "legacy pgfkeys single-figure family was reintroduced",
    )
    require(
        r"\NCKUPrivateSetInsertFigureKeys{#1}" in figure_source,
        "single-figure command bypasses the private key parser",
    )
    require(
        r"\keys_define:nn { ncku / insert-table }" in table_source,
        "single-table keys no longer use the bounded l3keys family",
    )
    require(
        table_source.count(".tl_set_e:N") == 8,
        "single-table l3keys family no longer has eight expanded-storage keys",
    )
    require(
        "/InsertTable/.is family" not in table_source,
        "legacy pgfkeys single-table family was reintroduced",
    )
    require(
        r"\NCKUPrivateSetInsertTableKeys{#1}" in table_source,
        "single-table command bypasses the private key parser",
    )
    require(figure_source.count(r"\TmpValuePosition") == 1, "figure pos key became behaviorally active")
    require(figure_source.count(r"\TmpValueAlign") == 1, "figure align key became behaviorally active")
    require(figures_source.count(r"\TmpMIValueAlign") == 1, "multi-figure align key became behaviorally active")
    require(
        r"\newcommand\NCKUPrivateSetInsertFiguresKeys[1]" in figures_source,
        "top-level multi-figure private parser seam is missing",
    )
    require(
        r"\newcommand\NCKUPrivateSetInsertFiguresSubFigureKeys[1]" in figures_source,
        "nested subfigure private parser seam is missing",
    )
    require(
        figures_source.count(r"\NCKUPrivateSetInsertFiguresKeys{#1}") == 1,
        "top-level multi-figure command bypasses its private seam",
    )
    require(
        figures_source.count(r"\NCKUPrivateSetInsertFiguresSubFigureKeys{#1}") == 1,
        "nested subfigure command bypasses its private seam",
    )
    require(
        r"/InsertFigures/.is family" in figures_source,
        "legacy top-level multi-figure family is missing before migration",
    )
    require(
        r"/InsertFiguresSubFigure/.is family" in figures_source,
        "legacy nested subfigure family is missing before migration",
    )

    print(
        "Float contract PASS: single/multi/subfigure/table routes, labels/ref/nameref, "
        "top/bottom/star captions, key-state/no-op placement, 4 images, A4 single page"
    )


if __name__ == "__main__":
    main()
