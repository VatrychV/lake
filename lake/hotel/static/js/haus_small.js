let slideIndex = 0;
const slides = document.querySelectorAll('.container .image');
const totalSlides = slides.length;
const slidesToShow = 0; // Кількість слайдів для показу
const slideWidth = slides[0].clientWidth;

function showSlides() {
    let startPosition = slideIndex * slideWidth * -1;
    document.getElementById('container').style.transform = `translateX(${startPosition}px)`;
}

function nextSlide() {
    slideIndex++;
    if (slideIndex > totalSlides - slidesToShow) {
        slideIndex = totalSlides - slidesToShow;
    }
    showSlides();
}

function prevSlide() {
    slideIndex--;
    if (slideIndex < 0) {
        slideIndex = 0;
    }
    showSlides();
}

showSlides();
