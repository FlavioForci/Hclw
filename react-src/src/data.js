// src/data.js
export const characters = [
  {
    id: 1,
    name: 'No Name',
    rarity: 'S-Tier',
    type: 'Warrior',
    image: './images/no-name.png', // Replace with actual paths
  },
  {
    id: 2,
    name: 'Witch',
    rarity: 'S-Tier',
    type: 'Mage',
    image: './images/witch.png',
  },
  {
    id: 3,
    name: 'Sword Master',
    rarity: 'S-Tier',
    type: 'Warrior',
    image: './images/sword-master.png',
  },
  {
    id: 4,
    name: 'Light',
    rarity: 'S-Tier',
    type: 'Mage',
    image: './images/light.png',
  },
  {
    id: 5,
    name: 'Constant',
    rarity: 'S-Tier',
    type: 'Support',
    image: './images/constant.png',
  },
  {
    id: 6,
    name: 'Zero',
    rarity: 'S-Tier',
    type: 'Assassin',
    image: './images/zero.png',
  },
  {
    id: 7,
    name: 'Armes',
    rarity: 'S-Tier',
    type: 'Warrior',
    image: './images/armes.png',
  },
  {
    id: 8,
    name: 'Master Swordsman',
    rarity: 'S-Tier',
    type: 'Warrior',
    image: './images/master-swordsman.png',
  },
  {
    id: 9,
    name: 'Heart Heater',
    rarity: 'A-Tier',
    type: 'Support',
    image: './images/heart-heater.png',
  },
  {
    id: 10,
    name: 'Nightmare Drip Soup',
    rarity: 'A-Tier',
    type: 'Assassin',
    image: './images/nightmare-drip-soup.png',
  },
  {
    id: 11,
    name: 'Sad Smile',
    rarity: 'B-Tier',
    type: 'Mage',
    image: './images/sad-smile.png',
  },
  {
    id: 12,
    name: 'Tempest',
    rarity: 'B-Tier',
    type: 'Mage',
    image: './images/tempest.png',
  },
  {
    id: 13,
    name: 'Nathan Han',
    rarity: 'B-Tier',
    type: 'Warrior',
    image: './images/nathan-han.png',
  },
  {
    id: 14,
    name: 'Drip Soup',
    rarity: 'A-Tier',
    type: 'Support',
    image: './images/drip-soup.png',
  },
  {
    id: 15,
    name: 'Feng Xian',
    rarity: 'A-Tier',
    type: 'Warrior',
    image: './images/feng-xian.png',
  },
  {
    id: 16,
    name: 'Choco Bibi',
    rarity: 'A-Tier',
    type: 'Mage',
    image: './images/choco-bibi.png',
  },
  {
    id: 17,
    name: 'Boy Dark',
    rarity: 'B-Tier',
    type: 'Support',
    image: './images/boy-dark.png',
  },
  {
    id: 18,
    name: 'Foodie Sora',
    rarity: 'B-Tier',
    type: 'Warrior',
    image: './images/foodie-sora.png',
  },
  {
    id: 19,
    name: 'Scalion Head',
    rarity: 'B-Tier',
    type: 'Warrior',
    image: './images/scalion-head.png',
  },
  {
    id: 20,
    name: 'Rim',
    rarity: 'B-Tier',
    type: 'Mage',
    image: './images/rim.png',
  },
  {
    id: 21,
    name: 'Dacon',
    rarity: 'B-Tier',
    type: 'Warrior',
    image: './images/dacon.png',
  },
  {
    id: 22,
    name: 'Kyo',
    rarity: 'B-Tier',
    type: 'Assassin',
    image: './images/kyo.png',
  },
  {
    id: 23,
    name: 'Octonash',
    rarity: 'B-Tier',
    type: 'Mage',
    image: './images/octonash.png',
  },
  {
    id: 24,
    name: 'Lazie',
    rarity: 'A-Tier',
    type: 'Support',
    image: './images/lazie.png',
  },
];

// src/App.js
import React from 'react';
import './App.css';
import CharacterCard from './components/CharacterCard';
import { characters } from './data'; // Import the characters array from data.js

function App() {
  const tiers = {
    'S-Tier (Top Tier)': characters.filter((char) => char.rarity === 'S-Tier'),
    'A-Tier (Excellent Choices)': characters.filter((char) => char.rarity === 'A-Tier'),
    'B-Tier (Maybe Usefull)': characters.filter((char) => char.rarity === 'B-Tier'),
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Character Tier List</h1>
        {Object.keys(tiers).map((tier) => (
          <div key={tier} className="tier">
            <h2>{tier}</h2>
            <div className="character-grid">
              {tiers[tier].map((character) => (
                <CharacterCard key={character.id} character={character} />
              ))}
            </div>
          </div>
        ))}
      </header>
    </div>
  );
}

export default App;
