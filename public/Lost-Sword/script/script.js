const toggleButton = document.getElementById('toggle-button');  // Kein .querySelector mehr
const navbar = document.querySelector('nav'); //querySelector verwenden, um das <nav>-Element auszuwählen


toggleButton.addEventListener('click', () => {
    navbar.classList.toggle('active');
    toggleButton.classList.toggle('active');

    if (navbar.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
});











function setActiveLink() {
    const navLinks = document.querySelectorAll('nav ul li a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        const href = link.getAttribute('href');

        // Normalize paths for comparison
        const normalizedHref = normalizePath(href);
        const normalizedCurrentPath = normalizePath(currentPath);

        // Debugging-Ausgaben (kannst du später entfernen)
        console.log("--- Neuer Link ---");
        console.log("  href-Attribut:", href);
        console.log("  Normalisierter href:", normalizedHref);
        console.log("  Aktueller Pfad (window.location.pathname):", currentPath);
        console.log("  Normalisierter aktueller Pfad:", normalizedCurrentPath);


        if (normalizedHref === normalizedCurrentPath ||
            (normalizedCurrentPath === '' && normalizedHref === 'index.html') ||
            (normalizedCurrentPath === 'index.html' && normalizedHref === '') ||
            normalizedHref === normalizedCurrentPath + '/' // HINZUGEFÜGT

           )
           {
            console.log("  -> Link ist AKTIV!");  // Debugging
            link.classList.add('active-link');
        } else {
            console.log("  -> Link ist INAKTIV."); // Debugging
            link.classList.remove('active-link');
        }
    });
}

// WICHTIG: Hilfsfunktion zur Pfadnormalisierung (unverändert)
function normalizePath(path) {
    let normalized = path;

     
     if (normalized.startsWith('./')) {
         normalized = normalized.slice(2);
     }

    // 2. Entferne den Basis-Pfad (WICHTIG!)
    const basePath = '/public/Lost-Sword/';  //  <-- ANPASSEN, falls nötig!
    if (normalized.startsWith(basePath)) {
        normalized = normalized.slice(basePath.length);
    }

    // 3. Entferne führenden Schrägstrich (nach dem Entfernen des Basis-Pfads)
     if (normalized.startsWith('/')) {
        normalized = normalized.slice(1);
    }

    // 4. Entferne nachgestellten Schrägstrich
    if (normalized.endsWith('/')) {
        normalized = normalized.slice(0, -1);
    }

    // 5. Entferne "index.html" oder "index.php" am Ende
    if (normalized.endsWith('index.html')) {
        normalized = normalized.slice(0, -10);
    }
    if (normalized.endsWith('index.php')) {
        normalized = normalized.slice(0, -9);
    }


    return normalized;
}


setActiveLink();
window.addEventListener('popstate', setActiveLink);
window.addEventListener('hashchange', setActiveLink);
