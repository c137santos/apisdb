#!/usr/bin/env python3
"""Converte todos os arquivos .md/.MD do repositório em PDFs via Chrome headless."""

import os
import subprocess
import tempfile
import markdown
from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "docs" / "pdfs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CHROME = "google-chrome"

CSS = """
<style>
  @page { margin: 1.5cm; }
  @media print {
    @page { margin: 1.5cm; }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #24292e;
    max-width: 900px;
    margin: 0 auto;
    padding: 30px 40px;
  }
  h1, h2, h3, h4 { font-weight: 600; margin-top: 24px; margin-bottom: 8px; }
  h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 8px; }
  h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 6px; }
  h3 { font-size: 1.25em; }
  code {
    background: #f6f8fa;
    border-radius: 3px;
    font-family: "SFMono-Regular", Consolas, monospace;
    font-size: 85%;
    padding: 0.2em 0.4em;
  }
  pre code {
    display: block;
    padding: 16px;
    overflow-x: auto;
    background: #f6f8fa;
    border-radius: 6px;
  }
  table { border-collapse: collapse; width: 100%; margin: 16px 0; }
  th, td { border: 1px solid #dfe2e5; padding: 8px 12px; text-align: left; }
  th { background: #f6f8fa; font-weight: 600; }
  tr:nth-child(even) { background: #fafbfc; }
  img { max-width: 100%; height: auto; border-radius: 4px; }
  blockquote {
    border-left: 4px solid #dfe2e5;
    color: #6a737d;
    margin: 0;
    padding: 0 16px;
  }
  a { color: #0366d6; text-decoration: none; }
  hr { border: 0; border-top: 1px solid #eaecef; margin: 24px 0; }
</style>
"""

MD_EXTENSIONS = [
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.attr_list",
]

def md_to_pdf(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(text, extensions=MD_EXTENSIONS)

    # Resolve imagens relativas para caminho absoluto
    html_body = html_body.replace('src="', f'src="{md_path.parent}/')
    html_body = html_body.replace(f'src="{md_path.parent}//home', 'src="/home')

    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{CSS}</head><body>{html_body}</body></html>"

    output_pdf = OUTPUT_DIR / (md_path.stem + ".pdf")

    with tempfile.NamedTemporaryFile(suffix=".html", mode="w", encoding="utf-8", delete=False) as f:
        f.write(html)
        tmp_html = f.name

    try:
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                f"--print-to-pdf={output_pdf}",
                "--print-to-pdf-no-header",
                "--no-pdf-header-footer",
                f"file://{tmp_html}",
            ],
            check=True,
            capture_output=True,
        )
    finally:
        os.unlink(tmp_html)

    return output_pdf


def find_md_files() -> list[Path]:
    files = []
    for ext in ("*.md", "*.MD"):
        files.extend(BASE_DIR.rglob(ext))
    # Exclui o próprio script e a pasta docs/pdfs
    IGNORE = {"docs/pdfs", ".venv", "node_modules", ".git"}
    return [f for f in files if not any(p in str(f) for p in IGNORE)]


def main():
    md_files = find_md_files()
    print(f"Encontrados {len(md_files)} arquivo(s) Markdown:\n")
    for f in md_files:
        print(f"  {f.relative_to(BASE_DIR)}")

    print()
    errors = []
    for md_file in md_files:
        print(f"Gerando PDF: {md_file.relative_to(BASE_DIR)} ...", end=" ", flush=True)
        try:
            pdf = md_to_pdf(md_file)
            print(f"OK → {pdf.relative_to(BASE_DIR)}")
        except Exception as e:
            print(f"ERRO: {e}")
            errors.append((md_file, e))

    print(f"\nPDFs gerados em: {OUTPUT_DIR.relative_to(BASE_DIR)}/")
    if errors:
        print(f"\n{len(errors)} erro(s):")
        for f, e in errors:
            print(f"  {f.name}: {e}")


if __name__ == "__main__":
    main()
