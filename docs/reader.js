(function () {
  var root = document.documentElement;
  var storagePrefix = root.getAttribute("data-storage-prefix");
  if (!storagePrefix) {
    throw new Error("Missing data-storage-prefix on <html>");
  }
  var THEME_KEY = storagePrefix + "-theme";
  var FONT_KEY = storagePrefix + "-font-scale";
  var LINE_KEY = storagePrefix + "-line-scale";
  var SCROLL_PREFIX = storagePrefix + "-scroll:";
  var FONT_MIN = 0.85;
  var FONT_MAX = 1.45;
  var FONT_STEP = 0.08;
  var LINE_MIN = 0.95;
  var LINE_MAX = 1.25;

  function preferredTheme() {
    try {
      var saved = localStorage.getItem(THEME_KEY);
      if (saved === "light" || saved === "dark") return saved;
    } catch (e) {}
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function themeLabel(theme) {
    return theme === "dark" ? "מצב יום" : "מצב לילה";
  }

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch (e) {}
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.textContent = themeLabel(theme);
      btn.title = theme === "dark" ? "עבור למצב יום" : "עבור למצב לילה";
    }
  }

  function readNumber(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      var n = parseFloat(raw);
      if (!isNaN(n)) return n;
    } catch (e) {}
    return fallback;
  }

  function clamp(n, min, max) {
    return Math.min(max, Math.max(min, n));
  }

  function applyTypography(fontScale, lineScale) {
    root.style.setProperty("--font-scale", String(fontScale));
    root.style.setProperty("--line-scale", String(lineScale));
    try {
      localStorage.setItem(FONT_KEY, String(fontScale));
      localStorage.setItem(LINE_KEY, String(lineScale));
    } catch (e) {}
  }

  function scrollMetrics() {
    var el = document.documentElement;
    var max = el.scrollHeight - el.clientHeight;
    if (max <= 0) return { pct: 0, ratio: 0 };
    var ratio = window.scrollY / max;
    return { pct: Math.round(ratio * 100), ratio: ratio };
  }

  function updateProgress() {
    var m = scrollMetrics();
    root.style.setProperty("--progress", m.pct + "%");
  }

  function chapterSlug() {
    return root.getAttribute("data-chapter") || "";
  }

  function saveScroll() {
    var slug = chapterSlug();
    if (!slug) return;
    try {
      localStorage.setItem(SCROLL_PREFIX + slug, String(scrollMetrics().ratio));
    } catch (e) {}
  }

  function restoreScroll() {
    var slug = chapterSlug();
    if (!slug) return;
    var ratio = 0;
    try {
      ratio = parseFloat(localStorage.getItem(SCROLL_PREFIX + slug) || "0");
    } catch (e) {
      return;
    }
    if (!(ratio > 0.02)) return;
    requestAnimationFrame(function () {
      var max = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      if (max > 0) window.scrollTo(0, max * clamp(ratio, 0, 1));
      updateProgress();
    });
  }

  function setDrawer(open) {
    document.body.classList.toggle("drawer-open", open);
    var toggle = document.getElementById("menu-toggle");
    var drawer = document.getElementById("toc-drawer");
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
    if (drawer) {
      drawer.setAttribute("aria-hidden", open ? "false" : "true");
      if (open) {
        var closeBtn = document.getElementById("drawer-close");
        if (closeBtn) closeBtn.focus();
      }
    }
  }

  applyTheme(preferredTheme());
  applyTypography(
    clamp(readNumber(FONT_KEY, 1), FONT_MIN, FONT_MAX),
    clamp(readNumber(LINE_KEY, 1), LINE_MIN, LINE_MAX)
  );

  document.addEventListener("DOMContentLoaded", function () {
    applyTheme(root.getAttribute("data-theme") || preferredTheme());

    var themeBtn = document.getElementById("theme-toggle");
    if (themeBtn) {
      themeBtn.addEventListener("click", function () {
        var next =
          root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        applyTheme(next);
      });
    }

    var smaller = document.getElementById("font-smaller");
    var larger = document.getElementById("font-larger");
    if (smaller) {
      smaller.addEventListener("click", function () {
        var font = clamp(readNumber(FONT_KEY, 1) - FONT_STEP, FONT_MIN, FONT_MAX);
        var line = clamp(readNumber(LINE_KEY, 1) - 0.03, LINE_MIN, LINE_MAX);
        applyTypography(font, line);
      });
    }
    if (larger) {
      larger.addEventListener("click", function () {
        var font = clamp(readNumber(FONT_KEY, 1) + FONT_STEP, FONT_MIN, FONT_MAX);
        var line = clamp(readNumber(LINE_KEY, 1) + 0.03, LINE_MIN, LINE_MAX);
        applyTypography(font, line);
      });
    }

    var menuToggle = document.getElementById("menu-toggle");
    var backdrop = document.getElementById("drawer-backdrop");
    var drawerClose = document.getElementById("drawer-close");
    if (menuToggle) {
      menuToggle.addEventListener("click", function () {
        setDrawer(!document.body.classList.contains("drawer-open"));
      });
    }
    if (backdrop) backdrop.addEventListener("click", function () { setDrawer(false); });
    if (drawerClose) drawerClose.addEventListener("click", function () { setDrawer(false); });
    function nativeFullscreenElement() {
      return (
        document.fullscreenElement ||
        document.webkitFullscreenElement ||
        null
      );
    }

    function canNativeFullscreen() {
      return !!(
        document.documentElement.requestFullscreen ||
        document.documentElement.webkitRequestFullscreen
      );
    }

    function requestNativeFullscreen() {
      var el = document.documentElement;
      if (el.requestFullscreen) return el.requestFullscreen();
      if (el.webkitRequestFullscreen) return el.webkitRequestFullscreen();
      return Promise.reject();
    }

    function exitNativeFullscreen() {
      if (document.exitFullscreen) return document.exitFullscreen();
      if (document.webkitExitFullscreen) return document.webkitExitFullscreen();
      return Promise.resolve();
    }

    function syncFullscreenUi(active) {
      document.body.classList.toggle("is-fullscreen", active);
      var btn = document.getElementById("fullscreen-toggle");
      if (!btn) return;
      btn.setAttribute("aria-pressed", active ? "true" : "false");
      btn.textContent = active ? "יציאה" : "מסך מלא";
      btn.title = active ? "יציאה ממסך מלא" : "מסך מלא";
    }

    function enterFullscreen() {
      setDrawer(false);
      syncFullscreenUi(true);
      if (!canNativeFullscreen()) return;
      try {
        var result = requestNativeFullscreen();
        if (result && typeof result.catch === "function") {
          result.catch(function () {
            /* CSS immersive fallback already on */
          });
        }
      } catch (e) {}
    }

    function leaveFullscreen() {
      syncFullscreenUi(false);
      if (nativeFullscreenElement()) {
        try {
          exitNativeFullscreen();
        } catch (e) {}
      }
    }

    function toggleFullscreen() {
      if (document.body.classList.contains("is-fullscreen") || nativeFullscreenElement()) {
        leaveFullscreen();
      } else {
        enterFullscreen();
      }
    }

    var fullscreenBtn = document.getElementById("fullscreen-toggle");
    if (fullscreenBtn) {
      fullscreenBtn.addEventListener("click", toggleFullscreen);
    }
    function onNativeFullscreenChange() {
      if (nativeFullscreenElement()) {
        syncFullscreenUi(true);
      } else if (canNativeFullscreen()) {
        // Browser exited native fullscreen (Esc / gesture); clear immersive chrome.
        syncFullscreenUi(false);
      }
    }
    document.addEventListener("fullscreenchange", onNativeFullscreenChange);
    document.addEventListener("webkitfullscreenchange", onNativeFullscreenChange);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        setDrawer(false);
        if (document.body.classList.contains("is-fullscreen") && !nativeFullscreenElement()) {
          leaveFullscreen();
        }
      }
    });

    var scrollTimer = null;
    window.addEventListener(
      "scroll",
      function () {
        updateProgress();
        if (scrollTimer) clearTimeout(scrollTimer);
        scrollTimer = setTimeout(saveScroll, 150);
      },
      { passive: true }
    );
    window.addEventListener("beforeunload", saveScroll);
    updateProgress();
    restoreScroll();
  });
})();
