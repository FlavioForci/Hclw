// Wählen Sie die Buttons und die Charakter-Elemente aus
const dpsButton = document.getElementById('dps-button');
const tankButton = document.getElementById('tank-button');
const healerButton = document.getElementById('healer-button');
const tierRows = document.querySelectorAll('.tier-row');

// Aktivieren Sie alle Buttons bei der Seitenladung
dpsButton.classList.add('active');
tankButton.classList.add('active');
healerButton.classList.add('active');

// Fügen Sie Event-Listener zu den Buttons hinzu, um die Filter zu aktivieren/deaktivieren
dpsButton.addEventListener('click', () => {
  if (dpsButton.classList.contains('active')) {
    dpsButton.classList.remove('active');
    tierRows.forEach((row) => {
      const dpsCategory = row.querySelector('.tier-category-D');
      if (dpsCategory) {
        row.style.display = 'none';
      }
    });
  } else {
    dpsButton.classList.add('active');
    tierRows.forEach((row) => {
      const dpsCategory = row.querySelector('.tier-category-D');
      if (dpsCategory) {
        row.style.display = 'flex';
      }
    });
  }
});

tankButton.addEventListener('click', () => {
  if (tankButton.classList.contains('active')) {
    tankButton.classList.remove('active');
    tierRows.forEach((row) => {
      const tankCategory = row.querySelector('.tier-category-T');
      if (tankCategory) {
        row.style.display = 'none';
      }
    });
  } else {
    tankButton.classList.add('active');
    tierRows.forEach((row) => {
      const tankCategory = row.querySelector('.tier-category-T');
      if (tankCategory) {
        row.style.display = 'flex';
      }
    });
  }
});

healerButton.addEventListener('click', () => {
  if (healerButton.classList.contains('active')) {
    healerButton.classList.remove('active');
    tierRows.forEach((row) => {
      const healerCategory = row.querySelector('.tier-category-H');
      if (healerCategory) {
        row.style.display = 'none';
      }
    });
  } else {
    healerButton.classList.add('active');
    tierRows.forEach((row) => {
      const healerCategory = row.querySelector('.tier-category-H');
      if (healerCategory) {
        row.style.display = 'flex';
      }
    });
  }
});
