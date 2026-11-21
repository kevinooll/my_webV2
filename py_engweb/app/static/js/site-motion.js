(() => {
  const root = document.documentElement;
  if (root.dataset.jtMotionReady) return;
  root.dataset.jtMotionReady = "true";

  const preference = window.matchMedia("(prefers-reduced-motion: no-preference)");
  const seen = new WeakSet();
  const candidates = document.querySelectorAll(
    "[data-motion-reveal], .home-page :is(.student-review-item, .why-jentalk-cards > *, " +
    ".test-card-item, .beginner-card, .teacher-carousel-card), " +
    ".course-page :is(.level-card, .scenario-card), .lesson-card, .ig-work-card"
  );
  let observer;
  let slideWatcher;
  const slides = document.querySelectorAll("[data-teacher-slide], [data-test-slide]");

  function syncReveal() {
    observer?.disconnect();
    if (!preference.matches || !("IntersectionObserver" in window)) return;

    observer = new IntersectionObserver((entries) => {
      let order = 0;
      for (const { target, isIntersecting } of entries) {
        if (!isIntersecting || seen.has(target)) continue;
        seen.add(target);
        observer.unobserve(target);
        target.style.setProperty("--motion-order", Math.min(order++, 3));
        target.classList.add("motion-revealed");
      }
    }, { rootMargin: "0px 0px -20px 0px" });

    for (const target of candidates) {
      if (!seen.has(target)) observer.observe(target);
    }
  }

  preference.addEventListener?.("change", syncReveal);
  syncReveal();

  // The existing carousel owns selection, focus, and visibility.
  function watchSlides() {
    if (!slides.length || !("MutationObserver" in window)) return;
    slideWatcher ??= new MutationObserver((changes) => {
      for (const target of new Set(changes.map(({ target }) => target))) {
        target.classList.toggle("motion-slide-enter", preference.matches && !target.hidden);
      }
    });
    for (const slide of slides) {
      slideWatcher.observe(slide, { attributes: true, attributeFilter: ["hidden"] });
    }
  }
  watchSlides();

  window.addEventListener("pagehide", () => {
    observer?.disconnect();
    slideWatcher?.disconnect();
    preference.removeEventListener?.("change", syncReveal);
  });
  window.addEventListener("pageshow", (event) => {
    if (!event.persisted) return;
    preference.addEventListener?.("change", syncReveal);
    syncReveal();
    watchSlides();
  });

  // Keep native validation and form payload intact. Only guard this page's pending submission.
  for (const form of document.querySelectorAll("[data-motion-submit]")) {
    const status = form.querySelector("[data-motion-status]");
    form.addEventListener("submit", (event) => {
      if (event.defaultPrevented) return;
      if (form.hasAttribute("data-motion-pending")) {
        event.preventDefault();
        return;
      }
      form.setAttribute("data-motion-pending", "");
      if (status) status.textContent = "正在送出，請稍候…";
    });
    window.addEventListener("pageshow", () => {
      form.removeAttribute("data-motion-pending");
      if (status) status.textContent = "";
    });
  }
})();
