#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

PROJECTS_BLOCK = '        <p class="project-group-label reveal">SELECTED PROJECTS</p>\n        <div class="featured-project-grid">\n          <article class="featured-project-card reveal">\n            <div class="featured-project-hero">\n              <div class="featured-project-heading">\n                <span class="featured-project-kicker">RESEARCH PROGRAM · CMP · TCAD</span>\n                <h3>CHIPS MASTER PROGRAM</h3>\n              </div>\n            </div>\n            <div class="featured-project-content">\n              <div class="featured-project-meta">\n                <span class="featured-status featured-status-progress">연구 진행 중</span>\n                <span class="featured-period">2026.04–2027.01</span>\n              </div>\n              <h3 class="featured-project-title">\n                <a href="projects/dram-bcat.html">20 nm급 BCAT DRAM MEB–Cov–GIDL 강건 설계</a>\n              </h3>\n              <p class="featured-project-problem">\n                MEB 공정 편차가 Cov와 drain-side 전계를 거쳐 GIDL 및 refresh 부담에 미치는 영향을 단계적으로 검증하는 장기 TCAD 연구입니다.\n              </p>\n              <div class="featured-project-info featured-project-result">\n                <span>현재 검증 결과</span>\n                <strong>Run 0 완료 · simplified 2D BCAT geometry/contact/doping/mesh 검증 · SDE–SDevice 연결 및 기본 Id–Vg turn-on 확인</strong>\n              </div>\n              <p class="featured-project-tech">Sentaurus TCAD · BCAT · MEB/Cov · BTBT/GIDL · Process Variation</p>\n              <div class="featured-project-actions">\n                <button class="featured-action featured-action-primary" type="button" data-project-summary="bcat">현재 단계</button>\n                <a class="featured-action" href="https://github.com/minhosong-mse/CMP" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </div>\n          </article>\n\n          <article class="featured-project-card reveal">\n            <div class="featured-project-hero">\n              <div class="featured-project-heading">\n                <span class="featured-project-kicker">COURSEWORK · TEAM · TCAD</span>\n                <h3>반도체집적공정</h3>\n              </div>\n            </div>\n            <div class="featured-project-content">\n              <div class="featured-project-meta">\n                <span class="featured-status">완료</span>\n                <span class="featured-period">2026-1</span>\n              </div>\n              <h3 class="featured-project-title">\n                <a href="projects/automotive-nmos.html">423 K 고온·단채널 NMOS 공정 최적화</a>\n              </h3>\n              <p class="featured-project-problem">\n                고온과 채널 길이 감소로 증가한 누설전류와 SS 열화를 분석하고, Halo–LDD–P-well 순서로 공정 조건을 단계적으로 조정했습니다.\n              </p>\n              <div class="featured-project-info featured-project-result">\n                <span>핵심 결과</span>\n                <strong>Ioff 약 7 orders 감소 · Ion/Ioff 23 → 1.39 × 10⁸ · SS 1015.2 → 198.6 mV/dec</strong>\n              </div>\n              <p class="featured-project-tech">Sentaurus TCAD · Parameter Sweep · High-Temperature Analysis</p>\n              <div class="featured-project-actions">\n                <button class="featured-action featured-action-primary" type="button" data-project-summary="automotive">요약 보기</button>\n                <a class="featured-action" href="https://github.com/minhosong-mse/Semiconductor_Process" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </div>\n          </article>\n\n          <article class="featured-project-card reveal">\n            <div class="featured-project-hero">\n              <div class="featured-project-heading">\n                <span class="featured-project-kicker">COMPETITION · TEAM · DATA ANALYSIS</span>\n                <h3>SSU 데이터톤 2025</h3>\n              </div>\n            </div>\n            <div class="featured-project-content">\n              <div class="featured-project-meta">\n                <span class="featured-status">완료</span>\n                <span class="featured-period">2025.12–2026.01</span>\n              </div>\n              <h3 class="featured-project-title">\n                <a href="projects/datathon.html">62,199건 논문 기반 반도체 연구 동향 분석</a>\n              </h3>\n              <p class="featured-project-problem">\n                범용 키워드의 false positive를 검수하고, 포토리소그래피와 첨단 패키징 중심으로 분석 범위를 재설계했습니다.\n              </p>\n              <div class="featured-project-info featured-project-result">\n                <span>핵심 결과</span>\n                <strong>제목·키워드·초록 통합 Python 분류 파이프라인 구축 · 반도체 관련 17,413건과 공정 관련 4,000건 이상 단계적 선별</strong>\n              </div>\n              <p class="featured-project-tech">Python · pandas · Jupyter · Regular Expressions</p>\n              <div class="featured-project-actions">\n                <button class="featured-action featured-action-primary" type="button" data-project-summary="datathon">요약 보기</button>\n                <a class="featured-action" href="https://github.com/minhosong-mse/Datathon" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </div>\n          </article>\n        </div>\n\n        <div class="additional-projects">\n          <p class="project-group-label reveal">MORE PROJECTS</p>\n          <div class="additional-project-grid">\n            <article class="additional-project-card reveal">\n              <div class="additional-project-top">\n                <span class="featured-status">완료</span>\n                <span class="featured-period">2026-1</span>\n              </div>\n              <div class="additional-project-content">\n                <p class="additional-project-source">COURSEWORK · 반도체집적공정</p>\n                <h3><a href="projects/semiconductor-process.html">NMOS 최적화 및 PMOS 공정 변환</a></h3>\n                <p class="additional-project-description">\n                  SimpleMOS 기준 NMOS 성능 탐색 후 N-well·Boron implant·음전압 sweep을 적용해 PMOS 공정으로 변환하고 5개 공정 변수를 최적화했습니다.\n                </p>\n                <p class="additional-project-result">교과목 내 NMOS 공동 1위 · PMOS Ion/Ioff 6.561 × 10¹¹</p>\n              </div>\n              <div class="additional-project-actions">\n                <button type="button" data-project-summary="nmos">요약 보기</button>\n                <a href="https://github.com/minhosong-mse/Semiconductor_Process_mid" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </article>\n\n            <article class="additional-project-card reveal">\n              <div class="additional-project-top">\n                <span class="featured-status">완료</span>\n                <span class="featured-period">2026-1</span>\n              </div>\n              <div class="additional-project-content">\n                <p class="additional-project-source">COURSEWORK · 반도체공정과화학분석</p>\n                <h3><a href="projects/hybrid-metrology.html">SE–X-ray Hybrid Metrology</a></h3>\n                <p class="additional-project-description">\n                  ALD High-k 초박막의 밀도·계면 거칠기 정량화를 위해 SE와 X-ray 계측의 상보적 제약을 문헌 기반으로 설계했습니다.\n                </p>\n                <p class="additional-project-result">수업 프로젝트 → CPC 1차 심사 → 반도체공학회 특별세션 공동 발표</p>\n              </div>\n              <div class="additional-project-actions">\n                <button type="button" data-project-summary="hybrid">요약 보기</button>\n                <a href="https://github.com/minhosong-mse/2026-SE-Xray-Hybrid-Metrology" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </article>\n\n            <article class="additional-project-card reveal">\n              <div class="additional-project-top">\n                <span class="featured-status">완료</span>\n                <span class="featured-period">2026-1</span>\n              </div>\n              <div class="additional-project-content">\n                <p class="additional-project-source">COURSEWORK · 디지털논리회로</p>\n                <h3><a href="projects/digital-logic.html">Vivado 기반 교통 신호 제어기 개선</a></h3>\n                <p class="additional-project-description">\n                  기존 5-state FSM을 유지하면서 보행자 요청 입력과 요청 처리 중 대기 LED 피드백을 추가했습니다.\n                </p>\n                <p class="additional-project-result">Verilog RTL·testbench 수정 · 상태 전환 및 LED 유지 waveform 검증</p>\n              </div>\n              <div class="additional-project-actions">\n                <button type="button" data-project-summary="logic">요약 보기</button>\n                <a href="https://github.com/minhosong-mse/Digital_Logic" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>\n              </div>\n            </article>\n          </div>\n        </div>\n'
CSS_BEGIN = '/* === image-free project layout 2026-08-04: begin === */'
CSS_END = '/* === image-free project layout 2026-08-04: end === */'
CSS_OVERRIDE = '\n/* === image-free project layout 2026-08-04: begin === */\n\n.featured-project-grid {\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: 22px;\n  align-items: stretch;\n}\n\n.featured-project-card {\n  display: flex;\n  min-width: 0;\n  height: 100%;\n  flex-direction: column;\n}\n\n.featured-project-hero {\n  display: flex;\n  grid-template-columns: none;\n  height: auto;\n  min-height: 168px;\n  align-items: flex-end;\n  padding: 27px 28px 25px;\n}\n\n.featured-project-heading {\n  width: 100%;\n}\n\n.featured-project-heading h3 {\n  font-size: clamp(1.55rem, 2.05vw, 2.45rem);\n  line-height: 1.06;\n  letter-spacing: -0.045em;\n  white-space: nowrap;\n}\n\n.featured-project-kicker {\n  margin-bottom: 10px;\n}\n\n.featured-project-content {\n  padding: 24px 25px 27px;\n}\n\n.featured-project-title {\n  font-size: clamp(1.18rem, 1.55vw, 1.42rem);\n  line-height: 1.33;\n}\n\n.featured-project-problem {\n  margin-top: 12px;\n  font-size: 0.84rem;\n}\n\n.featured-project-info {\n  padding: 13px 14px;\n}\n\n.featured-project-info strong {\n  font-size: 0.78rem;\n  line-height: 1.58;\n}\n\n.featured-project-tech {\n  margin-top: 14px;\n  font-size: 0.71rem;\n}\n\n.featured-project-actions {\n  padding-top: 20px;\n}\n\n.additional-projects {\n  margin-top: 48px;\n}\n\n.additional-project-grid {\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: 16px;\n}\n\n.additional-project-card {\n  display: flex;\n  min-width: 0;\n  min-height: 245px;\n  flex-direction: column;\n  gap: 0;\n  padding: 21px 21px 19px;\n}\n\n.additional-project-top {\n  display: flex;\n  align-items: flex-start;\n  justify-content: space-between;\n  gap: 12px;\n}\n\n.additional-project-content {\n  display: block;\n  min-width: 0;\n}\n\n.additional-project-source,\n.additional-project-content .additional-project-source {\n  margin: 12px 0 0;\n  color: var(--cyan-dark);\n  font-size: 0.6rem;\n  font-weight: 900;\n  line-height: 1.45;\n  letter-spacing: 0.075em;\n  word-break: keep-all;\n}\n\n.additional-project-content h3 {\n  margin: 6px 0 0;\n  font-size: 1.08rem;\n  line-height: 1.35;\n  letter-spacing: -0.02em;\n}\n\n.additional-project-description,\n.additional-project-content .additional-project-description {\n  margin: 9px 0 0;\n  color: var(--muted);\n  font-size: 0.76rem;\n  font-weight: 400;\n  line-height: 1.62;\n}\n\n.additional-project-result,\n.additional-project-content .additional-project-result {\n  margin: 10px 0 0;\n  color: var(--navy);\n  font-size: 0.72rem;\n  font-weight: 780;\n  line-height: 1.56;\n}\n\n.additional-project-actions {\n  gap: 14px;\n  margin-top: auto;\n  padding-top: 15px;\n}\n\n.contact-links-grid .contact-link strong {\n  font-size: clamp(1.08rem, 1.35vw, 1.55rem);\n}\n\n@media (max-width: 1100px) {\n  .featured-project-grid {\n    grid-template-columns: 1fr;\n  }\n\n  .featured-project-card {\n    display: flex;\n    flex-direction: column;\n  }\n\n  .featured-project-hero {\n    min-height: 145px;\n    align-items: flex-end;\n  }\n\n  .featured-project-heading h3 {\n    font-size: clamp(1.65rem, 4vw, 2.35rem);\n  }\n\n  .additional-project-grid {\n    grid-template-columns: 1fr;\n  }\n\n  .additional-project-card {\n    min-height: 0;\n  }\n}\n\n@media (max-width: 700px) {\n  .featured-project-hero {\n    min-height: 132px;\n    padding: 22px 20px 20px;\n  }\n\n  .featured-project-heading h3 {\n    font-size: clamp(1.34rem, 6.2vw, 1.8rem);\n  }\n\n  .featured-project-content {\n    padding: 21px 19px 23px;\n  }\n\n  .featured-project-title {\n    font-size: 1.22rem;\n  }\n\n  .featured-project-actions {\n    grid-template-columns: 1fr;\n  }\n\n  .additional-projects {\n    margin-top: 38px;\n  }\n\n  .additional-project-card {\n    padding: 19px 18px 17px;\n  }\n\n  .additional-project-source,\n  .additional-project-content .additional-project-source {\n    font-size: 0.57rem;\n    letter-spacing: 0.055em;\n  }\n\n  .contact-links-grid .contact-link strong {\n    font-size: 1.08rem;\n  }\n}\n\n@media (max-width: 410px) {\n  .featured-project-heading h3 {\n    font-size: 1.25rem;\n    letter-spacing: -0.04em;\n  }\n\n  .featured-project-kicker {\n    font-size: 0.57rem;\n  }\n\n  .featured-period {\n    font-size: 0.65rem;\n  }\n}\n\n/* === image-free project layout 2026-08-04: end === */\n'

class UpdateError(RuntimeError):
    pass

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")

def update_index(html: str) -> str:
    section_start = html.find('<section class="section section-projects"')
    experience_start = html.find(
        '<section class="section section-soft" id="experience"', section_start
    )
    block_start = html.find(
        '<p class="project-group-label reveal">SELECTED PROJECTS</p>',
        section_start,
        experience_start,
    )
    if min(section_start, experience_start, block_start) == -1:
        raise UpdateError("Projects section markers were not found in index.html.")

    outer_close = html.rfind("      </div>\n    </section>", block_start, experience_start)
    if outer_close == -1:
        raise UpdateError("The closing boundary of the Projects section was not found.")

    html = html[:block_start] + PROJECTS_BLOCK + html[outer_close:]

    html, count = re.subn(
        r'assets/css/style\.css(?:\?v=[^"]*)?',
        "assets/css/style.css?v=20260804-2",
        html,
        count=1,
    )
    if count != 1:
        raise UpdateError("The stylesheet link was not found in index.html.")
    return html

def update_css(css: str) -> str:
    block_pattern = re.compile(
        re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END),
        flags=re.DOTALL,
    )
    css = block_pattern.sub("", css)
    return css.rstrip() + "\n\n" + CSS_OVERRIDE.strip() + "\n"

def add_local_excludes(root: Path) -> None:
    exclude_path = root / ".git" / "info" / "exclude"
    if not exclude_path.parent.is_dir():
        return

    names = [
        "apply_project_layout_update.py",
        "run_project_layout_update.bat",
        "README_PROJECT_LAYOUT_UPDATE.txt",
    ]
    current = exclude_path.read_text(encoding="utf-8") if exclude_path.exists() else ""
    lines = set(current.splitlines())
    additions = [name for name in names if name not in lines]
    if not additions:
        return

    with exclude_path.open("a", encoding="utf-8") as file:
        if current and not current.endswith("\n"):
            file.write("\n")
        file.write("\n# Local portfolio update helpers\n")
        for name in additions:
            file.write(name + "\n")

def main() -> int:
    root = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd()
    index_path = root / "index.html"
    css_path = root / "assets" / "css" / "style.css"

    missing = [path for path in (index_path, css_path) if not path.is_file()]
    if missing:
        print("ERROR: Run this updater from the cloned repository root.")
        print("Missing:")
        for path in missing:
            print(f"  - {path}")
        return 1

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = root.parent / f"{root.name}-backup-{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=False)

    try:
        for source in (index_path, css_path):
            relative = source.relative_to(root)
            destination = backup_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        index_path.write_text(update_index(read_text(index_path)), encoding="utf-8")
        css_path.write_text(update_css(read_text(css_path)), encoding="utf-8")
        add_local_excludes(root)
    except Exception as exc:
        print(f"ERROR: {exc}")
        print(f"Backup directory: {backup_dir}")
        return 1

    print("Portfolio project layout update completed.")
    print(f"Repository: {root}")
    print(f"Backup: {backup_dir}")
    print("Modified:")
    print("  - index.html")
    print("  - assets/css/style.css")
    print("")
    print("Preview, then commit only the two modified files with GitHub Desktop.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
