(function () {
  var KEY = "hlw-reader-theme";
  var root = document.documentElement;

  function preferred() {
    try {
      var saved = localStorage.getItem(KEY);
      if (saved === "light" || saved === "dark") return saved;
    } catch (e) {}
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function label(theme) {
    return theme === "dark" ? "מצב יום" : "מצב לילה";
  }

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    try {
      localStorage.setItem(KEY, theme);
    } catch (e) {}
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.textContent = label(theme);
      btn.title = theme === "dark" ? "עבור למצב יום" : "עבור למצב לילה";
    }
  }

  apply(preferred());

  document.addEventListener("DOMContentLoaded", function () {
    apply(root.getAttribute("data-theme") || preferred());
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var next =
        root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      apply(next);
    });
  });
})();
