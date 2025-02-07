import React from 'react';
import './App.css';
import CharacterCard from './components/CharacterCard';
import characters from './components/CharacterList'; // Importiere die Charakterliste

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1></h1>
        {Object.keys(characters).map((tier) => (
          <div key={tier} className="tier">
            <h2>{tier}</h2>
            <div className="character-grid">
              {characters[tier].map((character, index) => (
                <CharacterCard key={index} character={character} />
              ))}
            </div>
          </div>
        ))}
      </header>
    </div>
  );
}

export default App;


