document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('.menu-toggle');
    const navContainer = document.querySelector('.nav-container');

    toggleButton.addEventListener('click', () => {
        navContainer.classList.toggle('active');
    });

    // Schließen des Menüs beim Klicken außerhalb
    document.addEventListener('click', (e) => {
        if (!navContainer.contains(e.target) && !toggleButton.contains(e.target)) {
            navContainer.classList.remove('active');
        }
    });
});



document.addEventListener('DOMContentLoaded', function () {
    const eventImages = document.querySelectorAll('.toggle-image');
    
    eventImages.forEach(function (image) {
        image.addEventListener('click', function () {
            eventImages.forEach(function (img) {
                if (img !== image) {
                    img.closest('.event-item').classList.toggle('hidden'); // Blendet alle außer das geklickte Bild ein/aus
                }
            });
        });
    });
});


document.querySelectorAll('.toggle-image').forEach(img => {
    img.addEventListener('click', function() {
        // Toggle visibility for all images except the clicked one
        document.querySelectorAll('.toggle-image').forEach(otherImg => {
            if (otherImg !== img) {
                otherImg.classList.toggle('hidden');
            }
        });
    });
});
 


document.getElementById('toggleButton').addEventListener('click', function() {
    const infoSection = document.querySelector('.info-section');
    infoSection.classList.toggle('hidden'); // Entfernt oder fügt die "hidden" Klasse hinzu
    infoSection.classList.toggle('active'); // Fügt oder entfernt die "active" Klasse für Sichtbarkeit
});
