

const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');
const slides = document.querySelectorAll('.slide'); // Alle Slides auswählen
let slideIndex = 0;
const slideCount = slides.length;

// Funktion zum Anzeigen eines bestimmten Slides
function goToSlide(index) {
    if (index < 0) {
        slideIndex = slideCount - 1;
    } else if (index >= slideCount) {
        slideIndex = 0;
    } else {
        slideIndex = index;
    }

     slider.style.transform = `translateX(-${slideIndex * 100}%)`;
}


// Event-Listener für die Buttons (können in initSlider verschoben werden)


//Init
function initSlider() {

    // Füge die Event-Listener für die Pfeiltasten hinzu
    prevButton.addEventListener('click', () => goToSlide(slideIndex - 1));
    nextButton.addEventListener('click', () => goToSlide(slideIndex + 1));
}

initSlider(); // Rufe die Initialisierungsfunktion auf