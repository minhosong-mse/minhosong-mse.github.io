#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re, shutil, sys
from datetime import datetime

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
PKG = Path(__file__).resolve().parent
FILES = PKG / "files"
INDEX = ROOT / "index.html"
CSS = ROOT / "assets" / "css" / "style.css"

CSS_BEGIN = "/* === FuriosaAI + LLM portfolio update 2026-08-08: begin === */"
CSS_END = "/* === FuriosaAI + LLM portfolio update 2026-08-08: end === */"

CSS_PATCH = r'''
/* === FuriosaAI + LLM portfolio update 2026-08-08: begin === */
.timeline-media-logo { background: #fff; }
.timeline-media-logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: #fff;
  padding: 14px;
}
.furiosa-wordmark img {
  object-fit: contain;
  background: #fff;
  padding: clamp(18px, 4vw, 46px);
}
.training-content-compact h3 a {
  color: inherit;
  text-decoration: none;
}
.training-content-compact h3 a:hover,
.training-content-compact h3 a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 4px;
}
.training-link-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  align-items: center;
}
@media (max-width: 700px) {
  .timeline-media-logo img { padding: 10px; }
  .furiosa-wordmark img { padding: 18px; }
}
/* === FuriosaAI + LLM portfolio update 2026-08-08: end === */
'''

FURIOSA_CARD = r'''
          <article class="timeline-item reveal">
            <div class="timeline-side">
              <div class="timeline-date">2026.08.07</div>
              <div class="timeline-media timeline-media-logo">
                <a href="experiences/furiosaai.html">
                  <img src="assets/images/experience/furiosaai/thumbnail.png" alt="FuriosaAI 로고">
                </a>
              </div>
            </div>
            <div class="timeline-body">
              <p class="timeline-type">FURIOSAAI · LLM APPLICATION PROJECT</p>
              <h3>FuriosaAI 사옥 최종 프로젝트 발표 및 기업탐방</h3>
              <p>GPU·NPU 기반 LLM Agent 및 RAG 단기강좌에서 구현한 「대학 학칙 도우미」를 FuriosaAI 사옥에서 최종 팀 프로젝트로 발표하고, NPU 기반 AI 시스템의 산업 현장을 경험했습니다.</p>
              <a class="text-link" href="experiences/furiosaai.html">VIEW FURIOSAAI EXPERIENCE <span aria-hidden="true">→</span></a>
            </div>
          </article>'''.rstrip()

if not INDEX.is_file() or not CSS.is_file():
    print("ERROR: Run this updater from the cloned minhosong-mse.github.io root.")
    raise SystemExit(1)

stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = ROOT.parent / f"{ROOT.name}-furiosa-backup-{stamp}"
backup.mkdir(parents=True, exist_ok=False)

for rel in ["index.html", "assets/css/style.css", "experiences/furiosaai.html", "training/llm-agent-rag.html"]:
    src = ROOT / rel
    if src.exists():
        dst = backup / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

html = INDEX.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

# Experience card
if 'href="experiences/furiosaai.html"' not in html:
    marker = '        <div class="timeline">\n          <article class="timeline-item reveal">'
    if marker not in html:
        print("ERROR: Experience timeline insertion point not found.")
        raise SystemExit(1)
    html = html.replace(
        marker,
        '        <div class="timeline">\n' + FURIOSA_CARD + '\n          <article class="timeline-item reveal">',
        1
    )

# Training titles/details
pairs = {
    '<h3>반도체 공정 with TCAD</h3>':
      '<h3><a href="training/tcad-process.html">반도체 공정 with TCAD</a></h3>',
    '<h3>반도체 소자 with TCAD</h3>':
      '<h3><a href="training/tcad-device.html">반도체 소자 with TCAD</a></h3>',
    '<h3>GPU·NPU 기반 LLM Agent 및 RAG 실습</h3>':
      '<h3><a href="training/llm-agent-rag.html">GPU·NPU 기반 LLM Agent 및 RAG 실습</a></h3>',
    '<div class="training-date-compact">2026.07.30–31</div>':
      '<div class="training-date-compact">2026.07.30–08.07</div>',
    '<p>Furiosa RNGD · Tool Calling · Agent Loop · MCP · RAG Pipeline</p>':
      '<p>FuriosaAI RNGD · Tool Calling · Agentic AI · MCP · RAG · Streamlit Application</p>',
}
for old, new in pairs.items():
    if old in html:
        html = html.replace(old, new, 1)

for github_url, detail_url in [
    ("https://github.com/minhosong-mse/2026-TCAD-Process-Short-Course", "training/tcad-process.html"),
    ("https://github.com/minhosong-mse/2026-TCAD-Device-Short-Course", "training/tcad-device.html"),
    ("https://github.com/minhosong-mse/2026-LLM-Agent-RAG-Short-Course", "training/llm-agent-rag.html"),
]:
    old = f'<a class="training-github" href="{github_url}" target="_blank" rel="noopener noreferrer">GITHUB <span aria-hidden="true">↗</span></a>'
    new = (
        '<div class="training-link-row">'
        f'<a class="training-github" href="{detail_url}">DETAILS <span aria-hidden="true">→</span></a>'
        f'<a class="training-github" href="{github_url}" target="_blank" rel="noopener noreferrer">GITHUB <span aria-hidden="true">↗</span></a>'
        '</div>'
    )
    if old in html:
        html = html.replace(old, new, 1)

html = re.sub(r'assets/css/style\.css(?:\?v=[^"]*)?', 'assets/css/style.css?v=20260808-1', html, count=1)

css = re.sub(re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END), "", css, flags=re.S)
css = css.rstrip() + "\n\n" + CSS_PATCH.strip() + "\n"

# Copy pages/assets
for src in FILES.rglob("*"):
    if src.is_file():
        rel = src.relative_to(FILES)
        dst = ROOT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

INDEX.write_text(html, encoding="utf-8")
CSS.write_text(css, encoding="utf-8")

exclude = ROOT / ".git" / "info" / "exclude"
if exclude.parent.is_dir():
    current = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    helpers = ["apply_furiosa_portfolio_update.py", "run_furiosa_portfolio_update.bat", "README_APPLY.txt", "files/"]
    missing = [x for x in helpers if x not in current.splitlines()]
    if missing:
        with exclude.open("a", encoding="utf-8") as f:
            if current and not current.endswith("\n"):
                f.write("\n")
            f.write("\n# Local Furiosa portfolio updater\n")
            for x in missing:
                f.write(x + "\n")

print("Update completed.")
print("Backup:", backup)
print("Changed/added:")
print(" - index.html")
print(" - assets/css/style.css")
print(" - experiences/furiosaai.html")
print(" - training/llm-agent-rag.html")
print(" - assets/images/experience/furiosaai/*")
