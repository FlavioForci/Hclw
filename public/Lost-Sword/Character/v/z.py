import os

character_names = [
    "Baylin", "Bedivere", "Catherine", "Christina", "Circe", "Claire",
    "Elaine", "Elisabeth", "Elin", "Enya", "Esmeralda", "Gaheris",
    "Galahad", "Gawain", "Guinevere", "Isabelle", "Isis", "Isolde",
    "Jessie", "Joan-of-Arc", "Kay", "Lisa", "Lilith", "Lucy",
    "Merlin", "Merry", "Mia", "Morgana", "Morgause", "Nymue",
    "Percival", "Rachel", "Ran", "Ray", "Ria-2", "Rita",
    "Rowena", "Sarah", "Tristan", "Viviene", "Neuer"
]

# Dictionaries für die Raritäten und Skill-Informationen
rarities = {
    "Baylin": "SR", "Bedivere": "SR", "Catherine": "SSR", "Christina": "SSR",
    "Circe": "SSR", "Claire": "SSR", "Elaine": "R", "Elisabeth": "SSR",
    "Elin": "R", "Enya": "SSR", "Esmeralda": "SR", "Gaheris": "SR",
    "Galahad": "SSR", "Gawain": "SSR", "Guinevere": "SSR", "Isabelle": "SSR",
    "Isis": "R", "Isolde": "SSR", "Jessie": "R", "Joan-of-Arc": "SSR",
    "Kay": "SSR", "Lisa": "SSR", "Lilith": "SSR", "Lucy": "SSR",
    "Merlin": "SSR", "Merry": "SSR", "Mia": "SR", "Morgana": "SSR",
    "Morgause": "SSR", "Nymue": "SR", "Percival": "SSR", "Rachel": "R",
    "Ran": "SSR", "Ray": "SR", "Ria-2": "SSR", "Rita": "R",
    "Rowena": "SR", "Sarah": "SR", "Tristan": "SSR", "Viviene": "SSR",
    "Neuer": "SSR"
}

# Dictionary für die Formationen
formations = {
    "Baylin": "Front row", "Bedivere": "Back row", "Catherine": "Back row",
    "Christina": "Middle row", "Circe": "Back row", "Claire": "Middle row",
    "Elaine": "Middle row", "Elisabeth": "Front row", "Elin": "Middle row",
    "Enya": "Middle row", "Esmeralda": "Back row", "Gaheris": "Front row",
    "Galahad": "Front row", "Gawain": "Front row", "Guinevere": "Back row",
    "Isabelle": "Middle row", "Isis": "Front row", "Isolde": "Back row",
    "Jessie": "Back row", "Joan-of-Arc": "Back row", "Kay": "Front row",
    "Lisa": "Middle row", "Lilith": "Middle row", "Lucy": "Front row",
    "Merlin": "Middle row", "Merry": "Back row", "Mia": "Front row",
    "Morgana": "Back row", "Morgause": "Back row", "Nymue": "Middle row",
    "Percival": "Front row", "Rachel": "Middle row", "Ran": "Front row",
    "Ray": "Front row", "Ria-2": "Back row", "Rita": "Front row",
    "Rowena": "Back row", "Sarah": "Back row", "Tristan": "Back row",
    "Viviene": "Middle row", "Neuer" : "Middle row" # Füge 'Neuer' hinzu, falls er existiert
}


# Erstelle das Verzeichnis, falls es nicht existiert.
if not os.path.exists("charakter_seiten"):
    os.makedirs("charakter_seiten")

for name in character_names:
    # Ersetze Leerzeichen und Sonderzeichen für gültige Dateinamen
    filename = name.replace(" ", "-").replace("#", "") + ".html"
    filepath = os.path.join("charakter_seiten", filename)

    # Hole die Rarity und Formation aus den Dictionaries.
    rarity = rarities.get(name, "Unknown")  # Standardwert, falls Name nicht gefunden
    formation = formations.get(name, "Unknown") # Standardwert

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content=" {name} Guide , {name} Profile, {name} Skills, ">
    <meta name="keywords" content="{name} Guide , {name} Profile, {name} Skills, Tychara Lost Sword, Tychara gacha ">
    <meta name="author" content="Tychara Team">
    <meta property="og:title" content="Tychara - Lost Sword {name}  ">
    <title>{name}</title>
    <link rel="stylesheet" href="../../Lost-Sword/css/main.css">
    <link rel="stylesheet" href="../../Lost-Sword/css/components/characterlayout.css">
     <script async src="https://www.googletagmanager.com/gtag/js?id=G-C93YVSG1YX"></script>
</head>
<body>
    <div class="logo-container">
        <a href="../../index.html"><div class="logo">
            <img src="../../Lost-Sword/img/Subtract.png" alt="Logo">
            <span class="logo-text">ychara</span></a>
    </div>
    <div class="kofi"> <a href='https://ko-fi.com/P5P819R853' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi3.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a></div>
        <button class="toggle-button" id="toggle-button">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </button>
    </div>
    <nav id="navbar">
        <ul> <li><a href="../../Lost-Sword/index.html"><img src="../../Lost-Sword/img/home_button.png" alt="Icon 1"> Home</a></li>
            <li><a href="#"><img src="../../Lost-Sword/img/Guide_button.png" alt="Icon 2"> Guides</a></li>
            <li><a href="../../Lost-Sword/Character/index.html"><img src="../../Lost-Sword/img/Character_button.png" alt="Icon 3"> Character</a></li>
            <li><a href="#"><img src="../../Lost-Sword/img/Info_button.png" alt="Icon 4"> About us </a></li>
        </ul>
    </nav>
    <div class="background-container">
        <div class="bg-layer layer-1">
            <video autoplay loop muted playsinline>
                <source src="../../Lost-Sword/img/main-bg.mp4" type="video/mp4">
                Dein Browser unterstützt das Video-Tag nicht.
            </video>
        </div>
    </div>
    <div><br><br></div>

    <div class="content-container">
        <div class="Character-banner">
            <div class="Character-Name"><h1>{name}</h1><p>Data and Guide</p></div>
                <div class="Character-Image"><img src="../../Lost-Sword/img/{name}.png" alt="{name}"></div>
        </div>

    <div class="Caracterinfocard">
        <div class="info-row">
            <span class="info-label">Rarity:</span>
            <span class="info-value">{rarity}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Attribute:</span>
            <span class="info-value">Nature</span>
        </div>
        <div class="info-row">
            <span class="info-label">Profession:</span>
            <span class="info-value">Knights</span>
        </div>
        <div class="info-row">
            <span class="info-label">Formation:</span>
            <span class="info-value {formation.lower().replace(' ', '-')}">{formation}</span>
        </div>
    </div>

    <h2>Character-Skills</h2>
        <div class="Character-Skills">
            <div class="skill-item">
                <div class="Skill-1"><img src="../../Lost-Sword/img/{name}Skill1.png" alt="Blade Dance"></div>
                <div class="skill-description">
                    <div class="skill-name">Blade Dance</div>
                    <div class="skill-level">Ultimate</div>
                    <div class="skill-section">
                        <div class="section-title">[Damage Dealt]</div>
                        <div>Inflict damage equal to [494/532/570/646/703]% of Attack</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Target]</div>
                        <div>All Enemies</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Effect: Apply Debuff]</div>
                        <div>Attribute Stack: Per stack: Decreases by Target's Defense 1%</div>
                        <div>(Max 6 stacks)</div>
                        <div>Duration: 3Second(s)</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Cooldown]</div>
                        <div>40Second(s)</div>
                    </div>
                </div>
            </div>
            <div class="skill-item">
                <div class="Skill-2"><img src="../../Lost-Sword/img/{name}Skill2.png" alt="Whirlwind"></div>
                <div class="skill-description">
                    <div class="skill-name">Whirlwind</div>
                    <div class="skill-level">Active</div>
                    <div class="skill-section">
                        <div class="section-title">[Damage Dealt]</div>
                        <div>Inflict damage equal to [322/336/350/364/385]% of Attack</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Target]</div>
                        <div>All Enemies</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Effect: Lifesteal]</div>
                        <div>Target: Self</div>
                        <div>Recover HP equal to 6% of damage inflicted.</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Cooldown]</div>
                        <div>16Second(s)</div>
                    </div>
                </div>
        </div>

        <div class="skill-item">
            <div class="Skill-3"><img src="../../Lost-Sword/img/{name}Skill3.png" alt="Valor"></div>
            <div class="skill-description">
                <div class="skill-name">Valor</div>
                <div class="skill-level">Passive</div>
                    <div class="skill-section">
                        <div class="section-title">[Effect 1: Apply Buff]</div>
                        <div>Target: Self</div>
                        <div>Effect: Attack Increase [18/24/30/38/46]%</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Effect 2: Apply Buff]</div>
                        <div>Target: Self</div>
                        <div>Effect: Attack Speed Increase [10/15/20/25/30%]</div>
                    </div>
                </div>
            </div>

            <div class="skill-item">
                <div class="Skill-4"><img src="../../Lost-Sword/img/{name}Skill4.png" alt="Whirlwind"></div>
                <div class="skill-description">
                    <div class="skill-name">Whirlwind</div>
                    <div class="skill-level">Active</div>
                    <div class="skill-section">
                        <div class="section-title">[Damage Dealt]</div>
                        <div>Inflict damage equal to [322/336/350/364/385]% of Attack</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Target]</div>
                        <div>All Enemies</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Effect: Lifesteal]</div>
                        <div>Target: Self</div>
                        <div>Recover HP equal to 6% of damage inflicted.</div>
                    </div>
                    <div class="skill-section">
                        <div class="section-title">[Cooldown]</div>
                        <div>16Second(s)</div>
                    </div>
                </div>
            </div>
        </div>

    <h2>Card information</h2>
        <div class="cards-container">
            <div class="Character-Card-Section">
            <div class="Character-Card-Name">
                <h3>Instant Counter</h3>
            </div>
            <div class="Character-Card">
                <img src="../img/{name}Card.jpg" alt="Character Card Image">
            </div>
            <div class="Card-Description">
                <p> Melee Attack Increase <br> [18.4/20.8/23.2/25.6/28/30.4/32.8/35.23//40]%</p>
            </div>
        </div>

        <div class="Card-Skill-Section">
            <div class="Card-Skill-Name">
                <h3>Counter Attackk</h3>
            </div>
            <div class="Card-Skill">
                <img src="../img/{name}CardSkill.jpg" alt="Card Skill Image">
            </div>
            <div class="Card-Skill-Description">
                <p>[Effects: Reflex damage] <br> Trigger conditions: When hit by the target attack equivalent to
                    5/10/15/20/25/30/35/40/45/50% of the additional damage.</p>
            </div>
        </div>
    </div>
<script src="../../Lost-Sword/script/script.js" defer></script>
</body>
</html>
""")

print("Dateien erstellt!")