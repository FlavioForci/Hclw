const sliders = document.querySelectorAll('.slider-container');

sliders.forEach((slider) => {
    const prevButton = slider.querySelector('.prev');
    const nextButton = slider.querySelector('.next');
    const slides = slider.querySelectorAll('.slide');
    let slideIndex = 0;

    prevButton.addEventListener('click', () => {
        slideIndex--;
        if (slideIndex < 0) {
            slideIndex = slides.length - 1;
        }
        slider.querySelector('.slider').style.transform = `translateX(-${slideIndex * 100}%)`;
    });

    nextButton.addEventListener('click', () => {
        slideIndex++;
        if (slideIndex >= slides.length) {
            slideIndex = 0;
        }
        slider.querySelector('.slider').style.transform = `translateX(-${slideIndex * 100}%)`;
    });
});
