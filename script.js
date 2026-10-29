(() => {
  "use strict";

  const STORAGE_KEY = "a-starter:theme";
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");

  const systemPrefersDark = () =>
    window.matchMedia("(prefers-color-scheme: dark)").matches;

  const resolvedTheme = () => {
    const explicit = root.getAttribute("data-theme");
    if (explicit === "light" || explicit === "dark") return explicit;
    return systemPrefersDark() ? "dark" : "light";
  };

  const applyTheme = (theme) => {
    if (theme === "light" || theme === "dark") {
      root.setAttribute("data-theme", theme);
    } else {
      root.removeAttribute("data-theme");
    }
    if (toggle) {
      const effective = resolvedTheme();
      toggle.setAttribute("aria-pressed", String(effective === "dark"));
      toggle.setAttribute(
        "aria-label",
        effective === "dark" ? "Switch to light theme" : "Switch to dark theme"
      );
    }
  };

  let stored = null;
  try {
    stored = localStorage.getItem(STORAGE_KEY);
  } catch {
    /* storage may be unavailable (private mode, sandbox) — ignore */
  }
  applyTheme(stored);

  if (toggle) {
    toggle.addEventListener("click", () => {
      const next = resolvedTheme() === "dark" ? "light" : "dark";
      applyTheme(next);
      try {
        localStorage.setItem(STORAGE_KEY, next);
      } catch {
        /* ignore */
      }
    });
  }

  const mql = window.matchMedia("(prefers-color-scheme: dark)");
  const onSystemChange = () => {
    let hasStored = false;
    try {
      hasStored = !!localStorage.getItem(STORAGE_KEY);
    } catch {
      /* ignore */
    }
    if (!hasStored) applyTheme(null);
  };
  if (mql.addEventListener) mql.addEventListener("change", onSystemChange);
  else if (mql.addListener) mql.addListener(onSystemChange);

  const depsEl = document.getElementById("stat-deps");
  if (depsEl && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const target = 0;
    const start = 7;
    const duration = 450;
    const t0 = performance.now();
    depsEl.textContent = String(start);
    const tick = (t) => {
      const p = Math.min(1, (t - t0) / duration);
      const eased = 1 - Math.pow(1 - p, 3);
      const value = Math.round(start + (target - start) * eased);
      depsEl.textContent = String(value);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
})();
