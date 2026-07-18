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

  if (year) year.textContent = String(new Date().getFullYear());
})();
