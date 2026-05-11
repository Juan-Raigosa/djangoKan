
let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
arrow[i].addEventListener("click", (e) => {
    let arrowParent = e.target.parentElement.parentElement; //selecting main parent of arrow
    arrowParent.classList.toggle("showMenu");
});
}
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", () => {
sidebar.classList.toggle("close");
});

const carousel = document.querySelector("[data-carousel]");
if (carousel) {
const slides = Array.from(carousel.querySelectorAll(".carousel-slide"));
const dotsContainer = carousel.querySelector(".carousel-dots");
const prevButton = carousel.querySelector("[data-carousel-prev]");
const nextButton = carousel.querySelector("[data-carousel-next]");
let activeIndex = 0;
let autoplayId;

const dots = slides.map((_, index) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "carousel-dot";
    dot.setAttribute("aria-label", `Ir a la imagen ${index + 1}`);
    dot.addEventListener("click", () => {
    updateCarousel(index);
    restartAutoplay();
    });
    dotsContainer.appendChild(dot);
    return dot;
});

function updateCarousel(index) {
    activeIndex = (index + slides.length) % slides.length;

    slides.forEach((slide, slideIndex) => {
    slide.classList.toggle("active", slideIndex === activeIndex);
    });

    dots.forEach((dot, dotIndex) => {
    dot.classList.toggle("active", dotIndex === activeIndex);
    });
}

function restartAutoplay() {
    window.clearInterval(autoplayId);
    autoplayId = window.setInterval(() => {
    updateCarousel(activeIndex + 1);
    }, 4000);
}

prevButton.addEventListener("click", () => {
    updateCarousel(activeIndex - 1);
    restartAutoplay();
});

nextButton.addEventListener("click", () => {
    updateCarousel(activeIndex + 1);
    restartAutoplay();
});

updateCarousel(0);
restartAutoplay();
}
