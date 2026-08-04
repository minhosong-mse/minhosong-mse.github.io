document.documentElement.classList.add("js");

(() => {
  const header = document.querySelector(".site-header");
  const menuToggle = document.querySelector(".menu-toggle");
  const navList = document.querySelector("#primary-nav");
  const navLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
  const sections = [...document.querySelectorAll("main section[id]")];
  const revealItems = [...document.querySelectorAll(".reveal")];
  const year = document.querySelector("#current-year");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const projectSummaries = {
    nmos: {
      title: "NMOS 최적화 및 PMOS 공정 변환",
      blocks: [
        ["1. 프로젝트 한눈에 보기", "교과목 SimpleMOS 흐름을 바탕으로 NMOS 성능을 최적화하고 도핑 종과 바이어스를 PMOS에 맞게 변환한 개인 프로젝트입니다."],
        ["2. 문제와 목표", "Ion 증가 조건이 Ioff와 SS에 항상 유리하지 않아 Ion/Ioff, SS, Vtgm을 함께 비교했습니다."],
        ["3. 내가 수행한 작업과 핵심 판단", "NMOS 후보 조건을 넓게 탐색한 뒤 유망 범위를 세분화했습니다. PMOS에서는 LDD dose를 먼저 안정화하고 S/D implant와 RTA를 순차 조정했습니다."],
        ["4. 결과", "NMOS는 교과목 내 공동 1위를 기록했고 Ion/Ioff 6.186 × 10¹¹, SS 82.953 mV/dec를 얻었습니다."],
        ["5. 범위 및 GitHub 자료", "NMOS 원본 command 파일은 공개 저장소에 보존되어 있지 않으며 결과는 README와 보고서에 근거합니다. 실측 검증은 포함하지 않습니다."],
      ],
    },
    automotive: {
      title: "423 K 고온 조건 NMOS 공정 최적화",
      blocks: [
        ["1. 프로젝트 한눈에 보기", "423 K와 Lg = 0.12 µm 조건에서 Halo–LDD–P-well을 순차 조정한 4인 팀 프로젝트입니다."],
        ["2. 문제와 목표", "고온과 단채널 효과로 Ioff와 SS가 동시에 악화되어 Ion 손실을 제한하며 전계와 공핍층을 재조정했습니다."],
        ["3. 내가 수행한 작업과 핵심 판단", "팀 리더로 전체 최적화 순서를 설계하고 Halo dose·energy 탐색을 전담했습니다."],
        ["4. 결과", "Ioff를 약 7 orders 줄이고 Ion/Ioff를 23에서 1.39 × 10⁸로 개선했습니다. SS는 1015.2에서 198.6 mV/dec로 감소했습니다."],
        ["5. 범위 및 GitHub 자료", "TCAD 연구이며 차량용 인증·실측 검증이 아닙니다. 최종 P-well 단계의 Ion 수치는 공개 결과표에 없어 단정하지 않습니다."],
      ],
    },
    datathon: {
      title: "SSU Datathon 2025",
      blocks: [
        ["1. 프로젝트 한눈에 보기", "62,199건의 공학 논문에서 반도체·공정 후보를 단계적으로 분류하고 포토리소그래피와 첨단 패키징 연구 흐름을 분석했습니다."],
        ["2. 문제와 목표", "범용 키워드가 false positive를 만들어 분류 숫자보다 도메인 적합성을 높이는 것이 핵심이었습니다."],
        ["3. 내가 수행한 작업과 핵심 판단", "팀 리더이자 공정팀으로 Advanced Packaging 키워드 정의, 데이터 검수, 연도별 추세 해석과 최종 발표 통합을 수행했습니다."],
        ["4. 결과", "논문 제목·키워드·초록을 통합한 Python 분류 파이프라인으로 62,199건의 공학 논문에서 17,413건의 반도체 관련 논문과 4,000건 이상의 공정 관련 논문을 단계적으로 선별했습니다."],
        ["5. 범위 및 GitHub 자료", "키워드 기반 분류는 문맥을 완전히 이해하지 못합니다. 표본 수동 검수와 precision/recall 측정을 추가하면 신뢰도가 더 높아집니다."],
      ],
    },
    hybrid: {
      title: "SE–X-ray Hybrid Metrology",
      blocks: [
        ["1. 프로젝트 한눈에 보기", "ALD High-k 초박막에서 SE 역모델링의 파라미터 상관성과 비유일성을 조사하고 XRR 구조정보를 제약조건으로 결합한 문헌 기반 프로젝트입니다."],
        ["2. 문제와 목표", "낮은 fitting error가 유일한 물리적 구조를 보장하지 않는다는 점을 설명했습니다."],
        ["3. 내가 수행한 작업과 핵심 판단", "팀 리더 및 SE 파트 담당으로 계측 한계를 정리하고 피드백 후 3D 패턴·측정 영역 문제를 추가했습니다."],
        ["4. 결과", "수업 프로젝트에서 CPC 1차 심사와 반도체공학회 특별세션 공동 발표로 확장했습니다."],
        ["5. 범위 및 GitHub 자료", "직접 장비 측정이 아니라 선행연구와 계측 원리를 분석한 프로젝트입니다."],
      ],
    },
    bcat: {
      title: "AI 메모리용 20 nm급 BCAT 강건 설계",
      blocks: [
        ["1. 현재 연구 질문", "MEB 편차가 Cov와 drain-side 전계를 통해 GIDL과 refresh 부담에 어떤 영향을 주는지 검증합니다."],
        ["2. 현재 완료", "20 nm급 simplified 2D BCAT baseline의 geometry, contact, doping, mesh와 SDE–SDevice 연결을 구축했습니다."],
        ["3. 현재 진행", "DC metric 정의와 baseline 전기 특성을 안정화하고 있습니다."],
        ["4. 다음 단계", "BTBT/GIDL 조건 구축, MEB split, 온도 및 공정 편차, robust process window 분석을 진행합니다."],
        ["5. 범위와 한계", "최종 최적 recipe나 leakage 감소율은 아직 공개하지 않습니다."],
      ],
    },
    logic: {
      title: "Vivado 기반 교통 신호 제어기 개선",
      blocks: [
        ["1. 프로젝트 한눈에 보기", "차량 감지에만 반응하던 5-state FSM에 보행자 요청과 대기 LED를 추가한 개인 프로젝트입니다."],
        ["2. 문제와 목표", "보행자 입력 경로와 요청 접수 피드백이 없어 기존 상태 수를 유지하며 기능을 확장했습니다."],
        ["3. 내가 수행한 작업과 핵심 판단", "btn_pedestrian를 차량 센서와 OR 조건으로 결합하고 S1–S4 동안 led_wait를 유지하도록 RTL과 testbench를 수정했습니다."],
        ["4. 결과", "차량과 보행자 입력이 동일한 상태 전환을 시작하고 요청 처리 중 LED가 유지되는 waveform을 확인했습니다."],
        ["5. 범위 및 GitHub 자료", "독립 Verilog/testbench 파일과 FPGA board 검증이 없어 .v, testbench, XDC 추가가 우선입니다."],
      ],
    },
  };

  const closeMenu = () => {
    if (!menuToggle || !navList) return;
    menuToggle.setAttribute("aria-expanded", "false");
    navList.classList.remove("is-open");
  };

  if (menuToggle && navList) {
    menuToggle.addEventListener("click", () => {
      const willOpen = menuToggle.getAttribute("aria-expanded") !== "true";
      menuToggle.setAttribute("aria-expanded", String(willOpen));
      navList.classList.toggle("is-open", willOpen);
    });

    navLinks.forEach((link) => link.addEventListener("click", closeMenu));

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeMenu();
        menuToggle.focus();
      }
    });

    document.addEventListener("click", (event) => {
      if (header && !header.contains(event.target)) closeMenu();
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 820) closeMenu();
    });
  }

  const setActiveLink = (sectionId) => {
    navLinks.forEach((link) => {
      const isActive = link.getAttribute("href") === `#${sectionId}`;
      link.classList.toggle("active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  if ("IntersectionObserver" in window && sections.length) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
        if (visible[0]) setActiveLink(visible[0].target.id);
      },
      {
        rootMargin: "-24% 0px -58% 0px",
        threshold: [0, 0.1, 0.35],
      }
    );
    sections.forEach((section) => sectionObserver.observe(section));
  }

  if (reducedMotion || !("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    revealItems.forEach((item) => revealObserver.observe(item));
  }

  document.querySelectorAll("[data-code-viewer]").forEach((viewer) => {
    const tabs = [...viewer.querySelectorAll('[role="tab"]')];
    const panels = [...viewer.querySelectorAll('[role="tabpanel"]')];
    if (!tabs.length || !panels.length) return;

    const activateTab = (nextTab, moveFocus = false) => {
      tabs.forEach((tab) => {
        const isActive = tab === nextTab;
        tab.setAttribute("aria-selected", String(isActive));
        tab.tabIndex = isActive ? 0 : -1;
      });

      panels.forEach((panel) => {
        panel.hidden = panel.id !== nextTab.getAttribute("aria-controls");
      });

      if (moveFocus) nextTab.focus();
    };

    const selectedTab =
      tabs.find((tab) => tab.getAttribute("aria-selected") === "true") || tabs[0];
    activateTab(selectedTab);

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => activateTab(tab));
      tab.addEventListener("keydown", (event) => {
        let nextIndex = index;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") {
          nextIndex = (index + 1) % tabs.length;
        } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
          nextIndex = (index - 1 + tabs.length) % tabs.length;
        } else if (event.key === "Home") {
          nextIndex = 0;
        } else if (event.key === "End") {
          nextIndex = tabs.length - 1;
        } else {
          return;
        }

        event.preventDefault();
        activateTab(tabs[nextIndex], true);
      });
    });
  });

  const summaryDialog = document.querySelector("#project-summary-dialog");
  const summaryTitle = document.querySelector("#project-summary-title");
  const summaryContent = document.querySelector("#project-summary-content");
  const summaryClose = summaryDialog?.querySelector(".project-summary-close");
  let summaryTrigger = null;

  const openProjectSummary = (projectKey, trigger) => {
    const summary = projectSummaries[projectKey];
    if (!summaryDialog || !summaryTitle || !summaryContent || !summary) return;

    summaryTitle.textContent = summary.title;
    summaryContent.replaceChildren(
      ...summary.blocks.map(([heading, description]) => {
        const section = document.createElement("section");
        const title = document.createElement("h3");
        const copy = document.createElement("p");
        section.className = "project-summary-block";
        title.textContent = heading;
        copy.textContent = description;
        section.append(title, copy);
        return section;
      })
    );

    summaryTrigger = trigger;
    summaryDialog.showModal();
  };

  document.querySelectorAll("[data-project-summary]").forEach((button) => {
    button.addEventListener("click", () => {
      openProjectSummary(button.dataset.projectSummary, button);
    });
  });

  summaryClose?.addEventListener("click", () => summaryDialog.close());

  summaryDialog?.addEventListener("click", (event) => {
    const bounds = summaryDialog.getBoundingClientRect();
    const isOutside =
      event.clientX < bounds.left ||
      event.clientX > bounds.right ||
      event.clientY < bounds.top ||
      event.clientY > bounds.bottom;
    if (isOutside) summaryDialog.close();
  });

  summaryDialog?.addEventListener("close", () => {
    summaryTrigger?.focus();
    summaryTrigger = null;
  });

  if (year) year.textContent = String(new Date().getFullYear());
})();
