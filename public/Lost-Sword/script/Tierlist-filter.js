document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-button');
    const characterGrid = document.querySelector('.Character-grid'); // Wähle den *Character-grid* Container!

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
           
            filterButtons.forEach(btn => btn.classList.remove('active'));

            // 2. Füge 'active' zum geklickten Button hinzu
            this.classList.add('active');

            // 3. Filterlogik
            const filterValue = this.dataset.filter;

            // Selektiere die *Charakter-Divs* innerhalb des Character-Grids
            const characterDivs = characterGrid.querySelectorAll('.Character-S, .Character-A, .Character-B');

            characterDivs.forEach(charDiv => {
                // Hole die Klassen des aktuellen Charakter-Divs als String
                const charClasses = charDiv.className;

                if (filterValue === 'all') {
                    charDiv.style.display = 'block'; // Zeige alle an
                } else if (charClasses.includes(filterValue)) {
                    charDiv.style.display = 'block'; // Zeige an, wenn die Klasse übereinstimmt
                } else {
                    charDiv.style.display = 'none'; // Sonst ausblenden
                }
            });
        });
    });
});