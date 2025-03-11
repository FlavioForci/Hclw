document.addEventListener('DOMContentLoaded', () => {
    // Sidebar-Initialisierung
    const sidebar = document.querySelector(".sidebar");
    const content = document.querySelector(".content");
    const menuToggle = document.querySelector('.menu-toggle');
    
    // Menü-Toggle-Funktion
    function toggleSidebar() {
        sidebar.classList.toggle("active");
        content.classList.toggle("shifted");
        document.body.style.overflow = sidebar.classList.contains("active") ? "hidden" : "auto";
    }

    // Menü-Toggle-Funktion aktivieren
    menuToggle.addEventListener('click', toggleSidebar);

    // Info-Section-Toggle-Funktion
    document.getElementById('toggleButton').addEventListener('click', () => {
        document.querySelector('.info-section').classList.toggle('active');
    });

    // Funktion zum Schließen der Sidebar, wenn außerhalb geklickt wird
    document.addEventListener('click', (event) => {
        // Wenn der Klick außerhalb der Sidebar und des Menüs erfolgt, schließen wir die Sidebar
        if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
            sidebar.classList.remove("active");
            content.classList.remove("shifted");
            document.body.style.overflow = "auto";  // Aktivieren der Bildlaufleiste, wenn die Sidebar geschlossen wird
        }
    });

});







function toggleMenu() {
    const navLinks = document.getElementById("navLinks");
    navLinks.classList.toggle("active");
}


