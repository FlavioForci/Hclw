// src/components/CharacterCard.js
import React from 'react';

const CharacterCard = ({ character }) => {
  return (
    <div className="character-card">
      <img src={character.image} alt={character.name} className="character-image" />
      <div className="character-info">
        <h3>{character.name}</h3>
        
      </div>
    </div>
  );
};

export default CharacterCard;
