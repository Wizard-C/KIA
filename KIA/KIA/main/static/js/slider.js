window.addEventListener("DOMContentLoaded", function() {
    var left = document.querySelector(".slider__left"),
        right = document.querySelector(".slider__right"),
        container = document.querySelector(".slider__container"),
        timer;
    right.addEventListener("click", function() {
        window.clearTimeout(timer);
        var last = container.querySelector(".slider__item:last-child");
        var first = container.querySelector(".slider__item:first-child");
        container.classList.remove("animate");
        if (!container.classList.contains("left")) {
            container.classList.add("left");
            container.insertBefore(last, first);
        }
        timer = window.setTimeout(function() {
            container.classList.add("animate");
            container.classList.remove("left")
        },30)
    });
    left.addEventListener("click", function() {
        window.clearTimeout(timer);
        var first = container.querySelector(".slider__item:first-child");
        container.classList.remove("animate");
        if (container.classList.contains("left")) {
            container.classList.remove("left");
            container.appendChild(first)
        }
        timer = window.setTimeout(function() {
            container.classList.add("animate");
            container.classList.add("left")
        },30)
    })
});
