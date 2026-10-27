// Light / dark theme switcher.
// Loaded in <head> so the saved theme is applied before the page is painted (no flash).
(() => {
  const STORAGE_KEY = "theme";
  const DEFAULT_THEME = "dark";
  const root = document.documentElement;

  const getSavedTheme = () => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      return saved === "light" || saved === "dark" ? saved : null;
    } catch {
      return null; // storage can be blocked (private mode, strict settings)
    }
  };

  const saveTheme = (theme) => {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch {
      // the theme still changes for this visit, it just won't be remembered
    }
  };

  const applyTheme = (theme) => {
    root.setAttribute("data-theme", theme);

    const toggle = document.getElementById("theme-toggle");
    if (toggle) {
      toggle.setAttribute("aria-label", `Switch to ${theme === "dark" ? "light" : "dark"} theme`);
    }
  };

  applyTheme(getSavedTheme() ?? DEFAULT_THEME);

  document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("theme-toggle");
    if (!toggle) return;

    applyTheme(root.getAttribute("data-theme")); // button exists now, sync its label

    toggle.addEventListener("click", () => {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      saveTheme(next);
    });
  });
})();
