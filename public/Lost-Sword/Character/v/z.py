import os

def parse_skill_data(skill_dict):
    skill_info = {
        "name": "",
        "damage": "",
        "effect": [],
        "target": "",
        "cooldown": "",
        "level": "",
        "duration": "",
        "additional_effects": []
    }
    
    if not skill_dict:
        return skill_info

    # Extract name
    if "name" in skill_dict:
        skill_info["name"] = skill_dict["name"]
    elif "type" in skill_dict:
        skill_info["name"] = skill_dict.get("type", "N/A")

    # Extract damage
    if "Damage" in skill_dict:
        damage_str = skill_dict["Damage"]
        if isinstance(damage_str, str) and "%" in damage_str:
            if "Causes" in damage_str:
                damage_values = damage_str.split("Causes ")[-1].split("%")[0]
            else:
                damage_values = damage_str.split("%")[0]
            skill_info["damage"] = f"{damage_values}%"
    elif "Causes" in skill_dict:
        damage_str = skill_dict["Causes"]
        if isinstance(damage_str, str) and "%" in damage_str:
            damage_values = damage_str.split("%")[0]
            skill_info["damage"] = f"{damage_values}%"

    # Extract effects
    effects = []
    if "Effect" in skill_dict:
        if isinstance(skill_dict["Effect"], str):
            effects.append(skill_dict["Effect"])
        elif isinstance(skill_dict["Effect"], dict):
            for key, value in skill_dict["Effect"].items():
                effects.append(f"{key}: {value}")
    elif "introduce" in skill_dict:
        effects.append(skill_dict["introduce"])
    elif "If in a state of inaction or more severe condition, it will be triggered when successfully resisting." in skill_dict:
        effects.append(skill_dict["If in a state of inaction or more severe condition, it will be triggered when successfully resisting."])

    # Additional effects
    for key in ["First effect", "Second effect"]:
        if key in skill_dict:
            if isinstance(skill_dict[key], str):
                effects.append(skill_dict[key])
            elif isinstance(skill_dict[key], dict):
                for k, v in skill_dict[key].items():
                    effects.append(f"{k}: {v}")

    # Recovery amount
    if "Recovery amount" in skill_dict:
        recovery_amount = skill_dict["Recovery amount"]
        if isinstance(recovery_amount, str) and "%" in recovery_amount:
            recovery_values = recovery_amount.split("%")[0]
            effects.append(f"Recovers {recovery_values}% of max health")
        else:
            effects.append(f"Recovers {recovery_amount} health")

    # Defensive strength increased
    if "Defensive strength increased by" in skill_dict:
        defensive_strength = skill_dict["Defensive strength increased by"]
        if isinstance(defensive_strength, str) and "%" in defensive_strength:
            defensive_values = defensive_strength.split("%")[0]
            effects.append(f"Increases defensive strength by {defensive_values}%")

    skill_info["effect"] = effects

    # Extract target and duration
    skill_info["target"] = skill_dict.get("Target unit", "N/A")
    skill_info["duration"] = skill_dict.get("Duration", "N/A")

    # Extract cooldown
    if "Cooling time" in skill_dict:
        cooldown = skill_dict["Cooling time"]
        if isinstance(cooldown, str) and "seconds" not in cooldown.lower():
            cooldown += " seconds"
        skill_info["cooldown"] = cooldown

    # Determine skill level
    skill_type = skill_dict.get("type", "").lower()
    if "ultimate" in skill_type:
        skill_info["level"] = "Ultimate"
    elif "active" in skill_type:
        skill_info["level"] = "Active"
    else:
        skill_info["level"] = "Passive"

    return skill_info




def generate_skill_html(skill, index, name):
    effects_html = ""
    if skill['effect']:
        effects_html = "<br>".join(skill['effect'])

    return f"""
    <div class="skill-item">
        <div class="Skill-{index}">
            <img src="../../Lost-Sword/Character/V/charakter_bilder/{name}/{name}Skill{index}.webp" alt="{skill['name']}">
        </div>
        <div class="skill-description">
            <div class="skill-name">{skill['name']}</div>
            <div class="skill-level">{skill['level']}</div>
            <div class="skill-section">
                <div class="section-title">[Damage]</div>
                <div>{skill['damage']}</div>
            </div>
            <div class="skill-section">
                <div class="section-title">[Target]</div>
                <div>{skill['target']}</div>
            </div>
            <div class="skill-section">
                <div class="section-title">[Effect]</div>
                <div>{effects_html}</div>
            </div>
            <div class="skill-section">
                <div class="section-title">[Duration]</div>
                <div>{skill['duration']}</div>
            </div>
            <div class="skill-section">
                <div class="section-title">[Cooldown]</div>
                <div>{skill['cooldown']}</div>
            </div>
        </div>
    </div>
    """


character_data = {

    "Aidan": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Speeding",
            "Damage": "Causes 372/408/432/480/528% damage",
            "Effect": "Attack power 20/30/40/50/70",
            "Target unit": "All enemies ahead",
            "Duration": "10 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "type": "Active",
            "name": "Upward spinning slash",
            "Damage": "Causes 304/312/328/344/368% damage",
            "Target unit": "All enemies ahead",
            "Cooling time": "14 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Leader",
            "Effect": "Equipment Proficiency",
            "Target unit": "",
            "The main attribute efficiency of equipment increases by 80%": "Only suitable for equipment with prop level below 160"
        },
        "Skill 4": {
            "[Effect 1": "Give gain]",
            "Target unit": "itself",
            "Effect": "Increased critical resistance rate by 10/10/10/15/20%",
            "[Effect 2": "Give gain]"
        },
        "card": {
            "The Sacred Sword": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Health increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "[Disappearance Sword Paranoid\" Passive",
            "[Effect 1": "Give gain]",
            "Trigger condition": "near death",
            "Target unit": "itself",
            "Immune damage": "Immune damage.",
            "Duration": "3 seconds",
            "Spell attribute": "Unable to remove",
            "[Effect 2": "Immortal]",
            "Save death when subjected to a fatal attack.": "[Cooldown time] 360 seconds"
        }
    },
    "Baylin": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Dance",
            "Damage": "Causes 494/532/570/646/703% damage",
            "Target unit": "All enemies",
            "Effect - Apply debuff": "",
            "Capacity value superposition": "Each layer reduces the defense of the target unit by 1% (up to 2 layers)",
            "Duration": "3 seconds",
            "Cooling time": "40 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 322/336/350/364/385% damage",
            "Target unit": "",
            "Effect": "Blood sucking",
            "Recovery is equivalent to 2% of the damage bearing capacity.": "Cooling time",
            "16 seconds": ""
        },
        "Skill 3": {
            "[Effect 1": "Give gain]",
            "Target unit": "",
            "Effect": "Attack speed increased by 10/15/20/25/30%",
            "[Effect 2": "Give gain]"
        },
        "card": {
            "Counterattack immediately": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Melee attack power increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "Counterattack",
            "[Effect": "Reflection Damage]",
            "Trigger condition": "When hit by the target",
            "Inflicts 1 additional damage equivalent to 5/10/15/20/25/30/35/40/45/50% of the attack power.": ""
        }
    },
    "Bedivere": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Prayer of the Stars",
            "Recovery amount": "Obtain 216/384/416/456/504% recovery",
            "Target unit": "All of us",
            "Cooling time": "28 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 145/155/165/180/195% damage",
            "Target unit": "All enemies ahead",
            "Cooling time": "11 seconds"
        },
        "Skill 3": {
            "Effect": "Ranged attack power increased by 18/24/30/38/46%",
            "Target unit": ""
        },
        "Skill 4": {
            "Effect": "Additional treatment",
            "Target unit": "1 of us",
            "(Target details": "Target units with high health)",
            "Trigger probability": "20%",
            "Recover the current health equivalent to 60% of the attack power.": ""
        },
        "card": {
            "The breath of the tree of the world": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Ranged attack power increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "[Root\" Passive",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "When the current health is above 100%",
            "Trigger target unit": "itself",
            "Effect": "Defensive power increased 3/6/9/12/15/18/21/24/27/30%",
            "Spell attribute": "Cannot be removed"
        }
    },
    "Catherine": {
        "Skill 1": {
            "Damage": "Causes 675%/725%/775%/850%/925% damage",
            "Target unit": "All enemies",
            "Effect": "Freezing",
            "Freezing": "No action can be carried out.",
            "Duration": "4 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 275%/303%/331%/367%/404% damage",
            "Target unit": "itself Effect: Critical hit rate increased by 6%/8%/10%/14%/18% Duration: 5 seconds",
            "First effect": "extra damage due to abnormal status",
            "When attacking target units that are frozen, the damage increases by 30%/45%/60%/75%/90%": "",
            "Second effect": "Give gain",
            "Cooling time": "10 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Amplitude",
            "Effect": "Give gain",
            "Trigger condition": "When a critical strike is caused",
            "Target unit": "",
            "Ability value superposition": "Each layer increases the critical damage of the target unit by 3%/5%/7%/10%/15% (maximum 10 layers)"
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Seal",
            "Effect 1": "Give Buffer",
            "Target unit": "",
            "Effect": "Attack power increased by 32%/44%/56%/72%/88%",
            "Effect 2": "Give Buffer"
        },
        "card": {
            "Ice Queen": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "Ignore damage reduction 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "LV1 Ice Dragon's Shelter": "",
            "【Effect": "Give gain】",
            "Target unit": "itself",
            "Effect": "When the current vitality is 100%/90%/80%/70%/60%/50%/40%/30%/20%/10%, the magic attack power increases by 15%/20%/25%/30%/35%/40%/45%/50%/55%/60%."
        }
    },
    "Christina": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Meteorite Shock",
            "Damage": "Causes 536%/580%/628%/696%/764% damage",
            "Target unit": "All enemies",
            "Effect": "Burning",
            "Continuous damage": "Takes damage equivalent to 100% of the caster's attack power every 1 second.",
            "Duration": "12 seconds",
            "Cooling time": "34 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 239%/263%/287%/319%/351% damage",
            "Target unit": "All enemies",
            "Effect": "Burning",
            "Continuous damage": "Takes damage equivalent to 100% of the caster's attack power every 1 second.",
            "Duration": "12 seconds",
            "Cooling time": "9 seconds"
        },
        "Skill 3": {
            "Effect": "Attack power increased by 24%/30%/36%/44%/56%",
            "Target unit": "Our"
        },
        "Skill 4": {
            "Effect": "Increased bondage resistance by 30%/35%/40%/45%/50%",
            "Target unit": "Our"
        },
        "card": {
            "Rose flame": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "Attack speed 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "Temperament-passive": "",
            "【Effect": "Give team gain】",
            "Target unit": "Our",
            "Effect": "Increase the critical hit rate by 0.5%/1%/1.5%/2%/2.5%/3%/3.5%/4%/4.5%/5%"
        }
    },
    "Circe": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Dream Demon",
            "Damage": "Causes 654%/708%/756%/834%/912% damage",
            "Target unit": "All enemies",
            "Effect": "Horror",
            "Terror": "No action can be carried out.",
            "Duration": "4 seconds",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 150%/165%/180%/200%/220% damage",
            "Target unit": "All enemies",
            "Effect": "Horror",
            "Terror": "No action can be carried out",
            "Duration": "1.5 seconds",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "Effect": "Increased status abnormal resistance by 5%/6%/7%/8%/10%",
            "Target unit": ""
        },
        "Skill 4": {
            "Effect": "Increase the critical hit rate by 6%/8%/10/%/14%/18%",
            "Target unit": "itself"
        },
        "card": {
            "Live in the present": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24%/28%/32%/36%/44%/48%/52%/56%/60%": "Live in the present",
            "Effect": "Attack power is reduced by 1.5/3/4.5/6/7.5/9/10.5/12/13.5/15%",
            "Target unit": "All enemies",
            "Spell attribute": "Unable to remove"
        }
    },
    "Claire": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Holy Gun, Longinus",
            "Damage": "Causes 820%/896%/960%/1066%/1170% damage",
            "Target unit": "All of us",
            "The first effect": "fainting",
            "Faint": "No action can be taken.",
            "Duration": "4 seconds",
            "Second effect": "additional treatment",
            "Recover the current health equivalent to 50% of the health.": "Cooling time",
            "38 seconds": ""
        },
        "Skill 2": {
            "Recovery amount": "Obtain 90%/105%/120%/140%/160% of attack power",
            "Target unit": "All of us",
            "Cooling time": "8 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Sacrifice",
            "The first effect": "fainting",
            "Trigger condition": "near death",
            "Target unit": "All of us except the caster",
            "Faint": "No action can be taken.",
            "Duration": "4 seconds",
            "Second effect": "additional treatment",
            "Recover the current health equivalent to 100% of the health.": "",
            "The third effect": "Give gain",
            "Effect": "Attack power increased by 24%",
            "Cooling time": "40 seconds"
        },
        "Skill 4": {
            "Effect": "terrorist resistance increased by 30%/35%/40%/45%/50%",
            "Target unit": "Our"
        },
        "card": {
            "Body training": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Melee attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "Blind - Passive",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Trigger when the current health is above 50%.",
            "Target unit": "itself",
            "Effect": "The resistance to abnormal status is increased by 2.5%/5%/7.5%/10%/12.5%/15%/17.5%/20%/22.5%/25%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Elaine": {
        "Skill 1": {
            "Damage": "Causes 425/450/475/510/550% damage",
            "Target unit": "All enemies",
            "Effect - Freezing": "",
            "Freezing": "No action can be carried out.",
            "Duration": "2 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 242/250/259/272/286% damage",
            "Effect": "Extra damage due to abnormal status",
            "Target unit": "itself",
            "When attacking target units that are frozen, damage increases by 10/15/20/30/40%": "Cooling time",
            "20 seconds": "Target unit",
            "All enemies ahead": ""
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Intuition",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Increased critical resistance rate by 2/4/6/9/12%",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "The essence of water": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Magic attack power increased by 11/12/13/14/15/16/17/18/19/20%": "resonance",
            "[Damage]": "Causes 180/210/240/270/300/330/360/3990/420/450% damage",
            "[Target Unit]": "All enemies",
            "[Effect": "Apply debuff]",
            "Effect": "1% reduction in attack power",
            "Duration": "10 seconds",
            "[Cooldown time]": "48 seconds"
        }
    },
    "Elin": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Sunbeam",
            "Damage": "Causes 270%/279%/297%/324%/351% damage",
            "Target unit": "All enemies",
            "Effect": "Extra damage due to abnormal status",
            "Increases damage by 20% when attacking target units that are bound": "Cooling time",
            "36 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 110%/114%/118%/124%/130% damage",
            "Target unit": "1 of all enemies ahead",
            "(Target details": "Target units with a distance)",
            "Effect": "Bondage",
            "Bondage": "No action can be carried out.",
            "Duration": "1 second",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Bondage",
            "[Effect": "Give gain]",
            "Target unit": "",
            "Effect": "Bound hit increases by 4%/8%/12%/18%/24%"
        },
        "card": {
            "Agile dodge": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Attack speed increased by 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%": "LV.1 Elves' Shelter",
            "[Effect": "Give gain]",
            "Specific triggering conditions": "Trigger when the current health is below 30%.",
            "Target unit": "itself",
            "Effect": "Get healing improvement 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "Spell attribute": "Cannot be removed"
        }
    },
    "Elizabeth": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Earthquake Sword",
            "Damage": "Causes 360/392/424/472/520% damage",
            "Target unit": "All enemies",
            "Effect - fainting": "",
            "Faint": "No action can be taken. Duration: 1 second",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "type": "Active",
            "name": "Upward spinning slash",
            "Damage": "Causes 315/348/381/423/468% damage",
            "Target unit": "All enemies ahead",
            "Cooling time": "8 seconds"
        },
        "Skill 3": {
            "Effect 1": "Give Buffer",
            "Target unit": "",
            "Effect": "Defensive strength increased by 32/44/56/72/88%",
            "Effect 2": "Give Buffer"
        },
        "Skill 4": {
            "Effect": "Defensive strength increased by 20/25/30/40/50%",
            "Specific trigger conditions": "Triggered when the current health is below 25%.",
            "Target unit": "",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "Absolute Armor": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Melee attack power increased 24/28/32/36/40/44/48/52/56/60%": "Health Recovery 110/120/130/140/150/160/170/180/190/200",
            "story": "\"Hey!\"",
            "Elizabeth, wearing red underwear, waving a giant sword, made me think a lot.": "\"Elizabeth, when you put on that bikini, it feels like you're becoming another person.\"",
            "\"Aidan! This is called absolute armor, not a bikini! Also, you will feel this way because the armor exerts its true power!\"": "\"Oh, I know, I know~\"",
            "\"And... only if you work hard, you won't feel so ashamed...!\"": "\"Um?\"",
            "Absolute armor seems to improve the wearer's swordsmanship.": "LV.1 Absolute Armor",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Trigger when the current health is below 50%.",
            "Target unit": "itself",
            "Effect": "Damage reduction 0.5/1/1.5/2/2.5/3/3.5/4/4.5/5%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Enya": {
        "Skill 1": {
            "Damage": "Causes 72%/81%/90%/102%/114% damage",
            "Target unit": "itself Change appearance: transform into a form suitable for combat.  Duration: 12 seconds Spell attribute: Unable to remove",
            "Effect": "Give gain",
            "Cooling time": "32 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 360%/420%/480%/560%/640% damage",
            "Target unit": "All enemies ahead",
            "Effect": "fainting",
            "Faint": "No action can be taken.",
            "Duration": "2 seconds",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Assassination",
            "Effect": "Increased critical hit rate by 6%/8%/10%/14%/18%",
            "Target unit": "itself"
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Adrenaline",
            "Effect": "Attack speed is increased by 5%/10%/15%/20%/25%",
            "Target unit": "itself"
        },
        "card": {
            "The manager's character": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Attack speed increased by 2%/4%/6%/8%/10%/12%/14%/16%/18%/20%": "Additional damage 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "Egg rice-passive": "",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Additional damage 0.5%/1%/1.5%/2%/2.5%/3%/3.5%/4%/4.5%/5%"
        }
    },
    "Esmeralda": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Dean Kate",
            "Recovery amount": "Obtain 385/440/485/565/640% recovery",
            "Effect": "Get 4/6/8/10/12% improvement",
            "Target unit": "All enemies",
            "Duration": "12 seconds",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "Recovery amount": "Get 85/91/96/105/114% recovery",
            "Target unit": "3 of us",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Health increase by 16/20/24/30/36%",
            "Spell attribute": "Unable to remove"
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Guardian",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Damage reduction 2/4/6/8/10%",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "Incarnation": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Magic attack power increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "Healing avatar",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Getting healing improvement 1.5/3/4.5/6/7.5/9/10.5/12/13.5/15%"
        }
    },
    "Gaheris": {
        "Skill 1": {
            "Damage": "Causes 434/462/504/546/602% damage",
            "Target unit": "All enemies",
            "Effect": "Burning",
            "Continuous damage": "Takes damage equivalent to the caster's attack every 1 second. Duration: 8 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Effect": "Critical hit rate increased by 10/12/14/16/20%",
            "Attack speed increased by 20/21/22/23/25%": "",
            "Duration": "10 seconds",
            "Cooling time": "15 seconds",
            "Target unit": "itself"
        },
        "Skill 3": {
            "[Effect": "Give gain]",
            "Target unit": "",
            "Effect": "Attack power increased by 18/24/30/38/46%"
        },
        "card": {
            "Knitting expert": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Melee attack power increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "craft",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Critical damage increased by 1/2/3/4/5/6/7/8/9/10%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Galahad": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "The Messenger of Light",
            "Effect 1": "Give Buffer",
            "Target unit": "All mage professions in our side",
            "Immune Damage": "Immune Damage.",
            "Duration": "20 seconds",
            "Effect 2": "Give Buffer",
            "Effect": "Magic, Attack Power Increased 160/180/200/225/250%",
            "Effect 3": "Give Buffer",
            "Cooling time": "30 seconds"
        },
        "Skill 2": {
            "Target unit": "All of us",
            "Effect": "Damage reduction 4/8/12/16/20%",
            "Duration": "10 seconds",
            "Cooling time": "10 seconds"
        },
        "Skill 3": {
            "introduce": "Triggers when an enemy tries to impose a negative effect (debuff).",
            "If in a state of inaction or more severe condition, it will be triggered when successfully resisting.": "Damage",
            "Causes 510/540/570/600/630% damage": "Target unit",
            "All enemies ahead": "Cooling time",
            "1 second": ""
        },
        "Skill 4": {
            "Effect": "Give teams a bonus",
            "Target unit": "All of us",
            "Defensive strength increased by 24/30/36/44/52%": ""
        },
        "card": {
            "Pure Knight": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Improved defense power 24/28/32/36/40/44/48/52/56/60%": "Get healing improvement 6/8/10/12/14/16/18/20/22/24%",
            "story": "Sunny weather.",
            "The four-leaf clover found in the field was handed over to Galahad.": "Come on, Galahad, will bring you good luck.",
            "\"Wow, brother. Thank you so much for giving me such an expensive gift!\"": "(…The first time I saw that weeding was given as a gift. What is this, is it kidding?)",
            "Galahad said carefully, putting the four-leaf clover in his arms.": "\"I will treasure my brother's gift.\"",
            "(Haah, it's so Sense...)": "Looking at Galahad's radiance, I felt happy.",
            "Purified Shield - Passive": "",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Shield": "Generates shields that absorb 20/40/60/80/100/120/140/160/180/200% damage equivalent to the caster's health increase."
        }
    },
    "Gawain": {
        "Skill 1": {
            "Damage": "Causes 420%/456%/496%/548%/604% damage",
            "Target unit": "All enemies",
            "The first effect": "fainting",
            "Faint": "No action can be taken.",
            "Duration": "4 seconds",
            "Second effect": "Superimposed bonus damage",
            "The beneficial buff effect on the target unit increases damage by 10% per layer": "Cooling time",
            "38 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 474%/516%/558%/618%/672% damage",
            "Target unit": "All enemies",
            "The first effect": "fainting",
            "Faint": "No action can be taken.",
            "Duration": "1.5 seconds",
            "Second effect": "Superimposed bonus damage",
            "The beneficial buff effect on the target unit increases damage by 10% per layer": "Cooling time",
            "12 seconds": ""
        },
        "Skill 3": {
            "Effect": "Health increase by 32%/44%/56%/72%/88%",
            "Target unit": ""
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Decision",
            "Effect": "Get 5%/10%/15%/20%/25%",
            "Target unit": "itself"
        },
        "card": {
            "Green belt": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Defensive strength increased by 24%/28%/32%/36%/40%/44%/46%/48%/52%/56%/60%": "Damage reduction 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "Green Belt - Active": "",
            "[Effect": "Remove debuff]",
            "Target unit": "",
            "Removes 1 random effect from the included debuff spell.": "[Cooldown time]",
            "30 seconds": ""
        }
    },
    "Guinevere": {
        "Skill 1": {
            "Recovery amount": "Get 480/550/619/724/828% recovery",
            "Target unit": "All of us",
            "The first effect": "resurrection",
            "Resurrect our teammates who were killed in the end and restore 100% of their health. The buff of the target character will not be removed.": "",
            "Second effect": "Give gain",
            "Continuous healing": "Recovery of 60% of the caster's attack power every 1 second",
            "Health.": "",
            "Duration": "4 seconds",
            "Cooling time": "48 seconds"
        },
        "Skill 2": {
            "Recovery amount": "Obtain 138/161/184/215/246% recovery",
            "Target unit": "All of us",
            "Effect": "Remove debuffs",
            "Remove all included debuff spells.": "Cooling time",
            "16 seconds": ""
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Melody",
            "Effect": "The status abnormal resistance is increased by 30/40/50/60/70%",
            "Target unit": ""
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Fire",
            "Effect": "Burning resistance increased by 30/35/40/45/50%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "The first strategy": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24/28/32/36/40/44/48/52/56/60%": "Abnormal resistance increased by 1/2/3/4/5/6/7/8/9/10%",
            "First Strategy - Passive": "",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Critical resistance rate increased by 1.5/3/4.5/6/7.5/9/10.5/12/13.5/15%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Isabelle": {
        "Skill 1": {
            "Damage": "Causes 456/496/536/600/656% damage",
            "Effect": "Attack power is reduced by 6/9/12/15/18%",
            "Duration": "10 seconds",
            "Cooling time": "30 seconds",
            "Target unit": "All enemies"
        },
        "Skill 2": {
            "Damage": "Causes 300/330/360/400/440% damage",
            "Target unit": "All enemies",
            "Effect": "Reduced critical hit rate by 6/8/10/14/18%",
            "Duration": "8 seconds",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "Effect": "Give gain",
            "Target unit": "itself",
            "Immune damage": "Immune to 20 damages."
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Storm",
            "Effect": "Ranged attack power increased by 32/44/56/72/88%",
            "Target unit": "itself"
        },
        "card": {
            "quality": "gold",
            "Star rating": "★★★★★",
            "property": "Attack speed increased by 3/6/9/12/15/18/21/24/27/30%",
            "Ignore damage reduction 2/4/6/8/10/12/14/16/18/20%": ""
        }
    },
    "Isis": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Dance under the Moon",
            "Damage": "Causes 432/456/480/516/552% damage",
            "Target unit": "3 of all enemies",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Damage": "Causes damage of 110/114/118/124/130% of attack power",
            "Target unit": "3 of all enemies ahead",
            "Cooling time": "8 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Meat shield",
            "[Effect": "Give gain]",
            "Target unit": "",
            "Effect": "Health increase by 2/4/6/8/10%"
        },
        "card": {
            "The will of the barbarian": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Melee attack power increased by 11/12/13/14/15/16/17/18/19/20%": ""
        }
    },
    "Isolde": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Healing Wind",
            "Recovery amount": "Get 200/225/250/289/331% recovery",
            "Target unit": "All of us",
            "Cooling time": "30 seconds"
        },
        "Skill 2": {
            "Target unit": "All of us",
            "Effect": "Damage reduction 4/8/12/16/20%",
            "Duration": "20 seconds",
            "Cooling time": "20 seconds"
        },
        "Skill 3": {
            "Effect": "Magic attack power increased by 32/44/56/72/88%",
            "Target unit": "itself"
        },
        "Skill 4": {
            "Effect": "Electric shock resistance increased by 30/35/40/45/50%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "Peerless medical skills": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "The amount of cure increased by 6/8/10/12/14/16/18/20/22/24%": "Defensive strength increased by 6/8/10/12/14/16/18/20/22/24%",
            "LV1 Healing Wind": "",
            "[Effect": "Additional treatment]",
            "Trigger condition": "When the battle begins",
            "Target unit": "All of us",
            "Recovering the current health equivalent to 11/12/13/14/15/16/17/18/19/20% of the health.": ""
        }
    },
    "Jessie": {
        "Skill 1": {
            "Damage": "Causes 170%/180%/190%/205%/220% damage",
            "Target unit": "All enemies",
            "Cooling time": "28 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 168%/174%/180%/189%/198% damage",
            "Target unit": "1 enemy",
            "Cooling time": "8 seconds"
        },
        "Skill 3": {
            "[Effect": "Give team gain]",
            "Target unit": "Our effect: Defense 8/12/16/20/24"
        },
        "Skill 4": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Defense 20/24/28/32/36"
        },
        "card": {
            "Preparation": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Ranged attack power increased by 11%/12%/13%/14%/15%/16%/17%/18%/19%20%": ""
        }
    },
    "Joan of Arc": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Sunburst",
            "Damage": "Causes 544/584/632/704/768% damage",
            "Effect": "Extra damage due to abnormal status",
            "When attacking target units that are imposed on a dull, the damage will be increased by 50/75/100/125/150%": "Cooling time",
            "36 seconds": "Target unit",
            "All enemies": ""
        },
        "Skill 2": {
            "Damage": "Causes 268/296/322/356/392% damage",
            "Effect": "Extra damage due to abnormal status",
            "When attacking a target unit that has been fainted, the damage will be increased by 30/45/60/75/90%": "Cooling time",
            "12 seconds": "Target unit",
            "All enemies": ""
        },
        "Skill 3": {
            "Effect": "Health increase by 24/30/36/44/52%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Dissolve",
            "Effect": "Freezing resistance increased by 30/35/40/45/50%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "The spirit of struggle": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Ranged attack power increased by 24/28/32/36/40/44/48/52/56/60%": "LV1 Physical Defense Passive",
            "Effect": "melee defense is increased by 18/24/30/36/42/48/54/60/66/72%, long-range defense is increased by 18/24/30/36/42/48/54/60/66/72%",
            "Specific trigger conditions": "Trigger when the current health is above 50%.",
            "Target unit": "",
            "Spell attribute": "Unable to remove"
        }
    },
    "Kay": {
        "Skill 1": {
            "Damage": "Causes 100%/150%/200%/300%/400% damage",
            "Target unit": "itself",
            "Effect": "Give gain",
            "Change appearance": "Transform into a form suitable for combat.",
            "Duration": "10 seconds",
            "Trigger at the end of the effect": "Burn",
            "Cooling time": "30 seconds"
        },
        "Skill 2": {
            "Target unit": "itself",
            "First effect": "Give gain",
            "Effect": "Critical damage increased by 16%/24%/32%/40%/48%",
            "Duration": "10 seconds",
            "Second effect": "Give gain",
            "Cooling time": "20 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Charge",
            "Effect 1": "Give Buffer",
            "Target unit": "itself",
            "Effect": "3%/6%/9%/12%/15% reduction in damage",
            "Effect 2": "Give Buffer"
        },
        "Skill 4": {
            "Effect 1": "Give Buffer",
            "Trigger condition": "near death",
            "Target unit": "",
            "Immune Damage": "Immune Damage.",
            "Duration": "5 seconds",
            "Spell attribute": "Unable to remove",
            "Effect 2": "Not dead",
            "Safe from death when subjected to a fatal attack": "Cooling time",
            "60 seconds": ""
        },
        "card": {
            "Flame Emperor": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "LV.1 violent",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Attack speed increased by 10%/10.5%/11%/11.5%/12%/12.5%/13%/13.5%/14%/14.5%/15%",
            "Duration": "10 seconds",
            "[Cooldown time]": "30 seconds"
        }
    },
    "Lilith": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Dance wildly!",
            "Damage": "Causes 549%/594%/639%/711%/783% damage",
            "Target unit": "All enemies",
            "Effect": "Superimposed Buffer Additional Damage",
            "The buff effect on the target unit increases damage by 5% per layer": "Cooling time",
            "33 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 224%/246%/272%/300%330% damage",
            "Target unit": "All enemies ahead",
            "Effect": "Superimposed Buffer Additional Damage",
            "The buff effect on the target unit increases damage by 5% per layer": "Cooling time",
            "18 seconds": ""
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Abuse",
            "Effect": "Give gain",
            "Trigger condition": "When killing",
            "Target unit": "itself",
            "Ability value superposition": "Each layer increases the attack power of the target unit by 3%/3%/3%/4%/4% (maximum 12 layers)"
        },
        "Skill 4": {
            "Effect": "2%/4%/6%/8%/10% attack power reduction",
            "Target unit": "Enemy"
        },
        "card": {
            "Charming": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Abnormal status hits increase by 16%/17%/18%/19%/20%/21%/22%/23%/24%/25%": "LV.1 dopamine",
            "[Effect": "Apply debuff]",
            "Target unit": "Enemy",
            "Effect": "Reduce critical resistance rate by 1.5%/3%/4.5%/6%/7.5%/9%/10.5%/12%/13.5%/15%"
        }
    },
    "Lisa": {
        "Skill 1": {
            "Skill Duration": "2.16 seconds",
            "Damage/recovery": "",
            "lv1-lv5": "Deals 480.0%/540.0%/600.0%/660.0%/720.0% damage",
            "Target unit": "All enemies",
            "Cooling time": "32 seconds"
        },
        "Skill 2": {
            "Duration": "2 seconds",
            "Target unit": "All enemies",
            "Damage": "",
            "lv1-lv5": "Causes attack power of 270.0%/",
            "288.0%/306.0%/324.0%/342.0% damage": "Cooling time",
            "6 seconds": ""
        },
        "Skill 3": {
            "Trigger condition": "When the skill hits",
            "Effect": "",
            "Additional damage when overlapping maximum values": "",
            "Lv1-Lv5 When the cumulative mark on the target reaches more than 6 levels, it will cause additional damage equivalent to attack power of 300.0%/345.0%/390.0%/435.0%/480.0%.": ""
        },
        "Skill 4": {
            "Trigger condition": "Always applicable",
            "Effect": "Give gain, target unit: itself",
            "Attack speed increased by 5.0%/10.0%/15.0%/20.0%": "/25.0%"
        },
       
    },
    "Lua": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Lightning Slash",
            "Damage": "Causes 522/567/621/684/756% damage",
            "Effect": "Apply debuff",
            "The target is inductive, and the damage to the target is inductive is increased by 5%, and the duration is 6 seconds.": "Cooling time",
            "32 seconds": "Target unit",
            "All enemies": ""
        },
        "Skill 2": {
            "Damage": "Causes 186/204/222/252/276% damage",
            "The first effect": "apply debuff",
            "The target is inductive and the damage to the target is increased by 5%, and the duration is 3 seconds.": "",
            "Second effect": "Give gain",
            "Target unit": "All enemies",
            "Effect": "Defensive strength increased by 32/44/56/72/88%",
            "Duration": "3 seconds",
            "Cooling time": "6 seconds"
        },
        "Skill 3": {
            "Effect": "Additional damage",
            "Inflicts 1 extra damage equivalent to 60/67.5/75/82/90% of attack power.": ""
        },
        "Skill 4": {
            "The first effect": "increase the attack target",
            "Target unit": "itself",
            "The target unit of the general attack will be added 1 additional person.": "",
            "Second effect": "Give gain",
            "Effect": "Attack power increased by 32/44/56/72/88%",
            "Effective in the following weather": "Rain"
        },
        "card": {
            "Elgrad Swordsman Diary": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Additional damage 6/7/8/9/10/11/12/13/14/15%": "Critical damage increased by 55/60/65/70/75/80/85/90/95/100%",
            "LV.1 reaction": "",
            "[Effect": "Change the cooldown time]",
            "Target unit": "",
            "Change the cooldown time of the active skill to 0 seconds.": "",
            "Cooldown time": "30 seconds"
        }
    },
    "Lucy": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Predation",
            "Damage": "Causes 462/497/532/588/637% damage",
            "Effect": "Extra damage due to abnormal status",
            "When attacking a target unit that is subjected to terror, the damage will be increased by 50/75/100/125/150%": "Target unit",
            "All enemies": "Cooling time",
            "38 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 177/195/213/237/261% damage",
            "Effect": "Extra damage due to abnormal status",
            "When attacking target units that are subject to terror, the damage increases by 30/45/60/75/90%": "Target unit",
            "All enemies": "Cooling time",
            "7 seconds": ""
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Gas storage",
            "Effect": "Critical damage increased by 32/44/56/72/88%",
            "Target unit": "itself"
        },
        "Skill 4": {
            "First effect": "Give gain",
            "Target unit": "",
            "Effect": "Critical hit rate increased by 3/4/5/7/9%",
            "Second effect": "Give gain"
        },
        "card": {
            "The strength of tenacity": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Melee attack power increased by 24/28/32/36/40/44/48/52/56/60%": "LV1 Fighter",
            "【Effect": "Give gain】",
            "Trigger condition": "When killing",
            "Target unit": "itself",
            "Ability value superposition": "Each layer increases the attack power of the target unit by 0.5/1/1.5/2/2.5/3/3.5/4/4.5/5% (up to 20 layers)"
        }
    },
    "Maryy": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Fierce rushing",
            "Damage": "Causes 488%/528%/568%/624%/688% damage",
            "Target unit": "itself",
            "Effect": "Extra damage due to abnormal status",
            "When attacking target units that are bound, the damage will increase by 20%/40%/60%/80%/100%": "Cooling time",
            "32 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 195%/202%/210%/222%/234% damage",
            "Target unit": "All enemies",
            "Effect": "Remove the gain",
            "Removes 1 random effect from the included buff spell.": "Cooling time",
            "12 seconds": ""
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Photosynthesis",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Health value increased by 18%/24%/30%/38%/46%"
        },
        "card": {
            "Reflex nerve": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Health value increased by 18.4%/20.8%/23.2%/25.6%/28%/30.4%/32.8%/35.2%/37.6%/40%": "LV.1 Asian",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Triggered when the current health is below 20%.",
            "Target unit": "itself",
            "Effect": "Dodge rate increased by 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Merlin": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Water Dragon, Ethel",
            "Damage": "Causes 450/485/520/575/630% damage",
            "Target unit": "All enemies",
            "Effect": "Freezing",
            "Freezing": "No action can be carried out.",
            "Duration": "4 seconds",
            "Cooling time": "35 seconds"
        },
        "Skill 2": {
            "Damage": "Causes damage of 303/331/358/395/432% of attack power",
            "Target unit": "All enemies ahead",
            "Effect": "Freezing",
            "Freezing": "No action can be performed",
            "Duration": "1.5 seconds",
            "Cooling time": "9 seconds"
        },
        "Skill 3": {
            "Effect": "Attack power increased by 32/44/56/72/88%",
            "Target unit": "itself"
        },
        "Skill 4": {
            "Effect": "Critical hit rate increased by 5/7.5/10/12.5/15%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "The protection of the water dragon": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24/28/32/36/40/44/48/52/56/60%": "Magic critical hit rate increased by 1/2/3/4/5/6/7/8/9/10%",
            "LV.1 Sage": "",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Attack power increased by 9/12/15/18/21/24/27/30/33/36%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Mia": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Flash",
            "Damage": "Causes 711/765/819/900/990% damage",
            "Effect": "Additional damage",
            "When the target unit is a lord, it causes 1 additional damage equivalent to 120/140/160/180/200% of the attack power.": "Target unit",
            "All enemies": "Cooling time",
            "32 seconds": ""
        },
        "Skill 2": {
            "Damage": "Causes 210/228/246/270/300% damage",
            "Effect": "Additional damage",
            "When the target unit is a lord, it will cause 1 additional damage equivalent to 20/40/60/80/100% of the attack power.": "Target unit",
            "All enemies": "Cooling time",
            "12 seconds": ""
        },
        "Skill 3": {
            "Effect": "Lord's Attack Power 120/180/240/320/400",
            "Target unit": ""
        },
        "Skill 4": {
            "Effect": "Critical resistance rate increases by 6/8/10/14/18%",
            "Target unit": ""
        },
        "card": {
            "Flowing water": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "The lord's attack power has increased by 24/28/32/36/40/44/48/52/56/60%": "Ignore damage reduction 1/2/3/4/5/6/7/8/9/10%",
            "LV.1 Duel": "",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Triggered when the current health is above 100%.",
            "Target unit": "itself",
            "Effect": "Melee critical strike rate increased by 1.5/3/4.5/6/7.5/9/10.5/12/13.5/15%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Morgana": {
        "Skill 1": {
            "Damage": "Causes 792%/864%/920%/1008%/1096% damage",
            "Target unit": "All enemies",
            "Effect": "Remove the gain",
            "Remove all included buff spells": "Cooling time",
            "32 seconds": "Effect",
            "Increase damage to fearful enemies by 50%/75%/100%/125%/150%": ""
        },
        "Skill 2": {
            "Damage": "Causes 269%/296%/323%/356%/395% damage",
            "Target unit": "All enemies",
            "Effect": "Remove the gain",
            "Remove all included buff spells.": "Cooling time",
            "8 seconds": ""
        },
        "Skill 3": {
            "Effect": "Increase attack power by 20%/40%/60%/80%/100%",
            "Specific trigger conditions": "Trigger when the current health is above 50%.",
            "Target unit": "itself",
            "Spell attribute": "Unable to remove"
        },
        "Skill 4": {
            "Effect": "Increase critical hit rate by 8%/10%/12%/16%/20%",
            "Target unit": "itself"
        },
        "card": {
            "Elf King": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24%/28%/32%/36%/44%/48%/52%/56%/60%": "LV.1 Elf",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Triggered when the current health is above 100%.",
            "Target unit": "",
            "Effect": "Magic critical hit rate increased by 1.5%/3%/4.5%/6%/7.5%/9.0%/10.5%/12%/13.5%/15%",
            "Spell attribute": "Unable to remove"
        }
    },

    "Morgan": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Big Bang",
            "Damage": "Causes 712%/768%/824%/904%/984% damage",
            "Target unit": "All enemies",
            "Effect": "Extra damage due to abnormal status",
            "When attacking a target unit that is burned": ", damage increased by 50%/75%/100%/125%/150%",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 272%/300%/328%/364%/404% damage",
            "Target unit": "All enemies ahead",
            "Effect": "Extra damage due to abnormal status",
            "When attacking a target unit that is burned": ", damage increased by 30%/45%/60%/75%/90%",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "Effect": "Increased critical hit rate by 6%/8%/10%/14%/18%",
            "Target unit": ""
        },
        "Skill 4": {
            "Effect": "Give gain",
            "Trigger condition": "When hit by the target",
            "Target unit": "itself",
            "Each layer increases the attack power of the target unit by 3%/3%/3%/4%/4% (maximum 12 layers)": ""
        },
        "card": {
            "obey": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "Damage reduction 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "LV.1 was abused": "",
            "[Effect": "Give gain]",
            "Trigger condition": "When hit by the target",
            "Target unit": "itself",
            "Capacity value superposition": "Each layer increases the defense of the target unit by 1/2/3/4/5/6/7/8/9/10% (maximum 12 layers)"
        }

    },
        "Nymue": {

        "Skill 1": {
            "Damage": "Causes 490%/530%/570%/630%/690% damage",
            "Target unit": "All enemies",
            "Effect": "Freezing",
            "Freezing": "No action can be carried out.",
            "Duration": "3 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Magic attack power increased by 18%/24%/30%/38%/46%"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Snowflake shelter",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Burning resistance increased by 20%/30%/40%/50%/60%"
        },
        "card": {
            "Snowflake Contract": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Magic attack power increased by 18.4%/20.8%/23.2%/25.6%/28%/30.4%/32.8%/35.2%/37.6%/40%": "[LV.1 Spiritual Blessings,"
            "[Effect; Remove debuff]" "cv",
            "Target Unit": "1 of us will remove the included debuff element in one random intra-agent.",
            "【Cooldown time】40 seconds": ""
        }
    },
    "Percival": {
        "Skill 1": {
            "Damage": "Dealing 434%/469%/511%/567%/623% damage",
            "Effect": "10%/12%/14%/18%/24% attack power",
            "Duration": "8 seconds",
            "Target unit": "All enemies",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "Cooling time": "18 seconds",
            "Target unit": "All of us",
            "Effect": "Give gain",
            "Shield": "Generates a shield that absorbs 30%/40%/50%/65%/80% damage equivalent to the caster's health.",
            "Duration": "10 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Guardian",
            "Effect": "Defensive strength increased by 24%/30%/36%/44%/52%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "Skill 4": {
            "Effect": "Damage reduction of 5%/7%/9%/11%/13%",
            "Target unit": "itself"
        },
        "card": {
            "Amethyst Holy Shield": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Health increase by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "LV.1 Amethyst Holy Shield",
            "[Effect": "Give team gain]",
            "Target unit": "Our",
            "Effect": "Defensive strength increased by 9%/12%/15%/18%/21%/24%/27%/30%/33%/36%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Rachel": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Healing Wind",
            "Damage": "Obtain 250%/260%/270%/290%/310% recovery",
            "Target unit": "All of us",
            "Effect": "Get healing improvement by 1%/2%/3%/5%/7%",
            "Duration": "12 seconds",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "type": "Active",
            "name": "All cure",
            "Recovery amount": "Obtain 66%/70%/74%/80%/86% recovery",
            "Target unit": "3 of us",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Increase the amount of healing by 2%/4%/6%/8%/10%"
        },
        "Skill 4": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Increase the critical resistance rate by 2%/4%/6%/8%/10%"
        },
        "card": {
            "Oriental medical skills": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Magic Attack power increased by 11%/12%/13%/14%/15%/16%/17%/18%/19%20%": ""
        }
    },
    "Ran": {
        "Skill 1": {
            "Damage": "Causes 768%/832%/896%/992%/1088% damage",
            "The first effect": "apply debuff",
            "Effect": "Defensive power is reduced by 6%/8%/10%/12%/14%",
            "Duration": "10 seconds",
            "Second effect": "extra damage due to abnormal status",
            "When attacking the target unit where the electric shock is applied, the damage will increase by 50%/75%/100%/125%/150%": "Target unit",
            "All enemies": "Cooling time",
            "33 seconds": ""
        },
        "Skill 2": {
            "Effect": "Extra damage due to abnormal status",
            "When attacking the target unit where the electric shock is applied, the damage will increase by 35%/45%/60%/75%/90%": "Damage",
            "Causes 476%/518%/560%/616%672% damage": "Target unit",
            "All enemies ahead": "Cooling time",
            "10 seconds": ""
        },
        "Skill 3": {
            "Effect": "Attack power increased by 32%/44%/56%/72%/88%",
            "Target unit": ""
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Pressure",
            "Effect": "Defensive power is reduced by 2%/4%/6%/8%/10%",
            "Target unit": "Enemy"
        },
        "card": {
            "Sword dance under the moon": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Melee attack power increased by 24%/28%/32%/36%/40%/44%/48%/52%/56%/60%": "Melee critical strike rate increased by 1%/2%/3%/4%/5%/6%/7%/8%/9%/10%",
            "LV. January sword dance": "",
            "[Effect": "Reflection Damage]",
            "Trigger condition": "When hit by the target",
            "Inflicts 1 additional damage equivalent to 10%/20%/30%/40%/50%/60%/70%/80%/90%/100% of attack power.": ""
        }
    },
    "Rey": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Tornado",
            "Damage": "Causes 280%/302%/324%/358%/392% damage",
            "Target unit": "All enemies",
            "Cooling time": "30 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 138%/144%/150%/159%/168% damage",
            "Target unit": "All enemies",
            "Cooling time": "9 seconds"
        },
        "Skill 3": {
            "type": "Passive",
            "name": "Faith",
            "[Effect": "Give gain]",
            "Target unit": "",
            "Effect": "4%/6%/8%/10%/12% damage reduction"
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Crazy",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Increased critical hit rate by 2%/4%/6%/8%/12%"
        },
        "card": {
            "Torture kill": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Critical damage increased by 10%/12%/14%/16%/18%/20%/22%/24%/26%/28%": "Attack speed increased by 3%/3%/4%/4%/5%/5%/6%/6%/7%/7%/7%"
        }
    },
    "Ria": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Room Service",
            "Effect": "Attack power increased by 30/40/50/60/75%",
            "Duration": "10 seconds",
            "Target unit": "All of us",
            "Cooling time": "28 seconds"
        },
        "Skill 2": {
            "Effect": "Attack power increased by 10/15/20/30/40%",
            "Duration": "10 seconds",
            "Target unit": "All of us",
            "Cooling time": "20 seconds"
        },
        "Skill 3": {
            "Effect": "Defensive strength increased by 32/44/56/72/88%",
            "Target unit": "itself"
        },
        "Skill 4": {
            "Effect": "Critical damage increased by 20/30/40/55/70%",
            "Target unit": "Our",
            "Spell attribute": "Unable to remove"
        },
        "card": {
            "Absolute Armor": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24/28/32/36/40/44/48/52/56/60%": "Ignore damage reduction 1/2/3/4/5/6/7/8/9/10%",
            "LV.1 Diner": "",
            "Target unit": "All of us",
            "Effect": "Granting Buff: Attack Power Increase by 10/11/12/13/14/15/16/17/18/20%",
            "Duration": "10 seconds",
            "Cooldown time": "20 seconds"
        }
    },
    "Rita": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Slash",
            "Damage": "Causes 344%/360%/384%/416%/448% damage",
            "Target unit": "All enemies",
            "Effect": "Reduce critical resistance rate by 4%/6%/8%/10%/12%",
            "Duration": "5 seconds",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "type": "Active",
            "name": "Instant step",
            "Damage": "Causes 142%/148%/153%/161%/168% damage",
            "Target unit": "All enemies ahead",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "[Effect": "Give gain]",
            "Target unit": "",
            "Effect": "Increase critical hit rate by 2%/4%/6%/10%/15%"
        },
        "card": {
            "Barista": "quality",
            "White": "Star rating",
            "3 stars": "property",
            "Improved defense power 11%/12%/13%/14%/15%/16%/17%/18%/19%20%": "LV.1 Barista",
            "[Effect": "Additional treatment]",
            "Trigger condition": "When the battle begins",
            "Target unit": "itself",
            "Recovering the current health equivalent to 0.5%/1%/1.5%/2%/2.5%/3%/3.5%/4%/4.5%/5% of health.": ""
        }
    },
    "Rowena": {
        "Skill 1": {
            "Damage": "Causes 413%/448%/483%/532%/581% damage",
            "Target unit": "All enemies",
            "Effect": "Horror",
            "Terror": "No action can be carried out.",
            "Duration": "3 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 207%/213%/222%/234%/249% damage",
            "Target unit": "All enemies",
            "Effect": "Defense -10/-15/-20/-25/-30",
            "Duration": "8 seconds",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "[Effect": "Blood sucking]",
            "Target unit": "",
            "Recovery is equivalent to 1%/2%/3%/4%/5% of the health value.": ""
        },
        "card": {
            "Devil's Contract": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Magic attack power increased by 18.4%/20.8%/23.2%/25.6%/28%/30.4%/32.8%/35.2%/37.6%/40%": "[LV.1 Demon Contract\"",
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Attack power is increased by 10%/12%/14%/17%/20%/22%/24%/26%/28%/30%",
            ", Defensive power is reduced by 30%/27%/24%/21%/18%/15%/12%/9%/6%/3%": "",
            "Duration": "12 seconds",
            "[Cooldown time] 24 seconds": ""
        }
    },
    "Sarah": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Volcano Arrow",
            "Damage": "Causes 297/319/341/385/418% damage",
            "Effect": "Extra damage due to abnormal status",
            "When attacking target units that are burned, the damage increases by 20/30/40/60/80%": "Cooling time",
            "38 seconds": "Target unit",
            "All enemies": ""
        },
        "Skill 2": {
            "Damage": "Causes 185/190/200/210/220% damage",
            "Target unit": "All enemies ahead",
            "Cooling time": "10 seconds"
        },
        "Skill 3": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Health increase by 18/24/30/38/46%"
        },
        "card": {
            "Big stomach king": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Health increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "[Glutty\" passive",
            "[Effect": "Extravasation of the diaphragm]",
            "Trigger condition": "When the battle begins",
            "Target unit": "itself",
            "Recovering the current health equivalent to 1/2/3/4/5/6/7/8/9/10% of the health.": ""
        }
    },
    "Tristan": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "crack shot! The arrow is empty!",
            "Damage": "Causes 410/445/485/535/590% damage",
            "Target unit": "All enemies",
            "Effect": "Bondage",
            "Bondage": "No action can be carried out.",
            "Duration": "4 seconds",
            "Cooling time": "38 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 225/246/270/300/330% damage",
            "Target unit": "All enemies",
            "Effect": "Bondage",
            "Bondage": "No action can be carried out.",
            "Duration": "1.5 seconds",
            "Cooling time": "9 seconds"
        },
        "Skill 3": {
            "Damage": "Causes 248/273/298/331/365% damage",
            "Target unit": "All enemies",
            "Effect": "Bondage",
            "Bondage": "No action can be carried out.",
            "Duration": "1.5 seconds",
            "Cooling time": "20 seconds"
        },
        "Skill 4": {
            "First effect": "Give gain",
            "Target unit": "",
            "Effect": "Critical hit rate increased by 3/4/5/7/9%",
            "Second effect": "Give gain"
        },
        "card": {
            "Arrows are shot without silence": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Ranged strike force increased by 24/28/32/36/40/44/48/52/56/60%": "Ignore damage reduction 1/2/3/4/5/6/7/8/9/10%",
            "LV.1 Pernott": "",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "Triggered when the current health is above 100%.",
            "Target unit": "itself",
            "Effect": "The ranged critical hit rate is increased by 1.5/3/4.5/6/7.5/9/10/12/13.5/15%",
            "Spell attribute": "Unable to remove"
        }
    },
    "Urien": {
        "Skill 1": {
            "type": "Ultimate",
            "name": "Thousand Arrows At One Time",
            "Damage": "Causes damage of 222/240/258/288/318% of attack power",
            "Target unit": "All enemies",
            "Effect": "Critical hit rate is reduced by 4/6/8/10/12%",
            "Duration": "8 seconds",
            "Cooling time": "36 seconds"
        },
        "Skill 2": {
            "Effect": "Attack power 20/40/60/90/120",
            "Duration": "10 seconds",
            "Cooling time": "16 seconds",
            "Target unit": "All enemies"
        },
        "Skill 3": {
            "[Effect": "Give gain]",
            "Target unit": "itself",
            "Effect": "Health 500/1000/1500/2000/3000"
        },
        "card": {
            "Snowflake Contract": "quality",
            "Purple": "Star rating",
            "4 stars": "property",
            "Defensive strength increased by 18.4/20.8/23.2/25.6/28/30.4/32.8/35.2/37.6/40%": "[Magic Defense\" Passive",
            "[Effect": "Give gain]",
            "Specific trigger conditions": "When the current health is above 50%",
            "Trigger target unit": "itself",
            "Effect": "Magic Defensive power increased 9/12/15/18/21/24/27/30/33/36%",
            "Spell attribute": "Cannot be removed"
        },

        "Skill 1": {
            "type": "Ultimate",
            "name": "Eye of Tiamat",
            "Damage": "Causes 720/774/816/876/936% damage",
            "Target unit": "itself",
            "First effect": "extra damage due to abnormal status",
            "When attacking target units that are bound, the damage increases by 50/75/100/125/150%": "",
            "Second effect": "Give gain",
            "Effect": "Critical damage increased by 24/32/40/48/56%",
            "Duration": "20 seconds",
            "Cooling time": "34 seconds"
        },
        "Skill 2": {
            "Damage": "Causes 244/270/294/326/360% damage",
            "Target unit": "All enemies ahead",
            "First effect": "extra damage due to abnormal status",
            "When attacking target units that are bound, the damage increases by 30/45/60/75/90%": "",
            "Second effect": "apply debuff",
            "Effect": "Attack power is reduced by 2/4/6/8/10%",
            "Duration": "6 seconds",
            "Cooling time": "12 seconds"
        },
        "Skill 3": {
            "Effect": "Magic attack power increased by 32/44/56/72/88%",
            "Target unit": ""
        },
        "Skill 4": {
            "type": "Passive",
            "name": "Mark",
            "First effect": "Give gain",
            "Target unit": "itself",
            "Effect": "Critical hit rate increased by 3/4/5/7/9%",
            "Second effect": "Give gain"
        },
        "card": {
            "Madness": "quality",
            "gold": "Star rating",
            "5 stars": "property",
            "Magic attack power increased by 24/28/32/36/40/44/48/52/56/60%": "Magic critical hit rate increased by 1/2/3/4/5/6/7/8/9/10%",
            "LV.1 Madness": "",
            "[Effect": "Give gain]",
            "Target unit": "Our",
            "Effect": "Critical damage increased by 9/12/15/18/21/24/27/30/33/36%",
            "Spell attribute": "Unable to remove"
        }
    }
}


character_names = [
    "Baylin", "Bedivere", "Catherine", "Christina", "Circe", "Claire",
    "Elaine", "Elisabeth", "Elin", "Enya", "Esmeralda", "Gaheris",
    "Galahad", "Gawain", "Guinevere", "Isabelle", "Isis", "Isolde",
    "Jessie", "Joan-of-Arc", "Kay", "Lisa", "Lilith", "Lucy",
    "Merlin", "Merry", "Mia", "Morgana", "Morgause", "Nymue",
    "Percival", "Rachel", "Ran", "Ray", "Ria-2", "Rita",
    "Rowena", "Sarah", "Tristan", "Viviene", "Neuer"
]

# Dictionaries für die Raritäten
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

# Dictionary für die Professionen
professions = {
    "Claire": "Knight", "Christina": "Mage", "Circe": "Mage",
    "Elisabeth": "Knight", "Enya": "Shooter", "Galahad": "Knight",
    "Gawain": "Knight", "Guinevere": "Spiritual Doctor", "Isabelle": "Shooter",
    "Isolde": "Spiritual Doctor", "Joan-of-Arc": "Shooter", "Lisa": "Shooter",
    "Lilith": "Mage", "Merlin": "Mage", "Morgana": "Mage", "Morgause": "Mage",
    "Percival": "Knight", "Tristan": "Shooter", "Viviene": "Mage",
    "Catherine": "Knight", "Baylin": "Knight", "Bedivere": "Knight",
    "Elaine": "Mage", "Elin": "Mage", "Esmeralda": "Mage",
    "Gaheris": "Knight", "Isis": "Mage", "Jessie": "Shooter",
    "Kay": "Knight", "Lucy": "Knight", "Merry": "Mage",
    "Mia": "Knight", "Nymue": "Mage", "Rachel": "Shooter",
    "Ran": "Knight", "Ray": "Knight", "Ria-2": "Mage",
    "Rita": "Mage", "Rowena": "Mage", "Sarah": "Mage",
    "Neuer": "Mage"
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
    "Viviene": "Middle row", "Neuer": "Middle row"
}

# Character Stats Dictionary
character_stats = {
    "Claire": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4055, "attack_rank": 22, "defense": 3303, "defense_rank": 12},
        "250": {"health": 45936, "health_rank": 9, "attack": 5518, "attack_rank": 22, "defense": 4545, "defense_rank": 12}
    },
    "Christina": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4113, "attack_rank": 9, "defense": 3269, "defense_rank": 20},
        "250": {"health": 45936, "health_rank": 9, "attack": 5576, "attack_rank": 9, "defense": 4511, "defense_rank": 20}
    },
    "Circe": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4076, "attack_rank": 17, "defense": 3271, "defense_rank": 19},
        "250": {"health": 45936, "health_rank": 9, "attack": 5539, "attack_rank": 17, "defense": 4513, "defense_rank": 19}
    },
    "Elisabeth": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4067, "attack_rank": 18, "defense": 3280, "defense_rank": 17},
        "250": {"health": 45936, "health_rank": 9, "attack": 5530, "attack_rank": 19, "defense": 4522, "defense_rank": 17}
    },
    "Enya": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4090, "attack_rank": 11, "defense": 3257, "defense_rank": 26},
        "250": {"health": 45936, "health_rank": 9, "attack": 5553, "attack_rank": 14, "defense": 4499, "defense_rank": 26}
    },
    "Galahad": {
        "200": {"health": 36780, "health_rank": 1, "attack": 4370, "attack_rank": 4, "defense": 3720, "defense_rank": 1},
        "250": {"health": 49930, "health_rank": 1, "attack": 5960, "attack_rank": 4, "defense": 5070, "defense_rank": 1}
    },
    "Gawain": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4078, "attack_rank": 15, "defense": 3269, "defense_rank": 20},
        "250": {"health": 45936, "health_rank": 9, "attack": 5541, "attack_rank": 16, "defense": 4511, "defense_rank": 20}
    },
    "Guinevere": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4058, "attack_rank": 21, "defense": 3294, "defense_rank": 15},
        "250": {"health": 45936, "health_rank": 9, "attack": 5520, "attack_rank": 21, "defense": 4536, "defense_rank": 15}
    },
    "Isabelle": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4067, "attack_rank": 18, "defense": 3280, "defense_rank": 17},
        "250": {"health": 45936, "health_rank": 9, "attack": 5530, "attack_rank": 19, "defense": 4522, "defense_rank": 17}
    },
    "Isolde": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4021, "attack_rank": 25, "defense": 3312, "defense_rank": 11},
        "250": {"health": 45936, "health_rank": 9, "attack": 5484, "attack_rank": 25, "defense": 4554, "defense_rank": 11}
    },
    "Joan-of-Arc": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4085, "attack_rank": 12, "defense": 3262, "defense_rank": 23},
        "250": {"health": 45936, "health_rank": 9, "attack": 5548, "attack_rank": 15, "defense": 4504, "defense_rank": 23}
    },
    "Lisa": {
        "200": {"health": 35309, "health_rank": 5, "attack": 4272, "attack_rank": 5, "defense": 3408, "defense_rank": 5},
        "250": {"health": 47933, "health_rank": 5, "attack": 5799, "attack_rank": 5, "defense": 4704, "defense_rank": 5}
    },
    "Lilith": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4067, "attack_rank": 18, "defense": 3292, "defense_rank": 14},
        "250": {"health": 45936, "health_rank": 9, "attack": 5530, "attack_rank": 19, "defense": 4534, "defense_rank": 14}
    },
    "Merlin": {
        "200": {"health": 36780, "health_rank": 1, "attack": 4490, "attack_rank": 1, "defense": 3590, "defense_rank": 3},
        "250": {"health": 49930, "health_rank": 1, "attack": 6080, "attack_rank": 1, "defense": 4940, "defense_rank": 3}
    },
    "Morgana": {
        "200": {"health": 35309, "health_rank": 5, "attack": 4253, "attack_rank": 7, "defense": 3428, "defense_rank": 7},
        "250": {"health": 47933, "health_rank": 5, "attack": 5780, "attack_rank": 7, "defense": 4724, "defense_rank": 7}
    },
    "Morgause": {
        "200": {"health": 35309, "health_rank": 5, "attack": 4244, "attack_rank": 8, "defense": 3423, "defense_rank": 8},
        "250": {"health": 47933, "health_rank": 5, "attack": 5770, "attack_rank": 8, "defense": 4719, "defense_rank": 8}
    },
    "Percival": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4044, "attack_rank": 24, "defense": 3303, "defense_rank": 12},
        "250": {"health": 45936, "health_rank": 9, "attack": 5507, "attack_rank": 24, "defense": 4545, "defense_rank": 12}
    },
    "Tristan": {
        "200": {"health": 33838, "health_rank": 9, "attack": 4085, "attack_rank": 12, "defense": 3262, "defense_rank": 23},
        "250": {"health": 45936, "health_rank": 9, "attack": 5548, "attack_rank": 15, "defense": 4504, "defense_rank": 23}
    },
    "Viviene": {
        "200": {"health": 35309, "health_rank": 5, "attack": 4272, "attack_rank": 5, "defense": 3408, "defense_rank": 5},
        "250": {"health": 47933, "health_rank": 5, "attack": 5799, "attack_rank": 5, "defense": 4704, "defense_rank": 5}
    }
}

## Hauptcode
os.makedirs("charakter_seiten", exist_ok=True)

for name in character_names:
    try:
        filename = f"{name.replace(' ', '-').replace('#', '')}.html"
        filepath = os.path.join("charakter_seiten", filename)
        
        rarity = rarities.get(name, "Unknown")
        formation = formations.get(name, "Unknown")
        profession = professions.get(name, "Unknown")
        stats_200 = character_stats.get(name, {}).get("200", {})
        stats_250 = character_stats.get(name, {}).get("250", {})

        # Stats-Sektion nur für SSR-Charaktere
        level_stats_section = ""
        if rarity == "SSR":
            level_stats_section = f"""
            <div class="info-row level-stats">
                <span class="info-label">Level 200:</span>
                <div class="info-value">
                    <span class="stat-item">Health: {stats_200.get('health', 'N/A')} <span class="rank">(Rank {stats_200.get('health_rank', 'N/A')})</span></span> 
                    <span class="stat-item">Attack: {stats_200.get('attack', 'N/A')} <span class="rank">(Rank {stats_200.get('attack_rank', 'N/A')})</span></span> 
                    <span class="stat-item">Defense: {stats_200.get('defense', 'N/A')} <span class="rank">(Rank {stats_200.get('defense_rank', 'N/A')})</span></span> 
                </div>
            </div>
            <div class="info-row level-stats">
                <span class="info-label">Level 250:</span>
                <div class="info-value">
                    <span class="stat-item">Health: {stats_250.get('health', 'N/A')} <span class="rank">(Rank {stats_250.get('health_rank', 'N/A')})</span></span> 
                    <span class="stat-item">Attack: {stats_250.get('attack', 'N/A')} <span class="rank">(Rank {stats_250.get('attack_rank', 'N/A')})</span></span> 
                    <span class="stat-item">Defense: {stats_250.get('defense', 'N/A')} <span class="rank">(Rank {stats_250.get('defense_rank', 'N/A')})</span></span> 
                </div>
            </div>"""

        # Generate skills HTML
        skills_html = ""
        if name in character_data:
            for idx, skill_key in enumerate(["Skill 1", "Skill 2", "Skill 3", "Skill 4"], 1):
                if skill_key in character_data[name]:
                    skill = parse_skill_data(character_data[name][skill_key])
                    # Pass all three required arguments
                    skills_html += generate_skill_html(skill, idx, name)  # name added here
        # HTML-Template
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Gacha Guides, Tier Lists, Reward codes, Tier List and Tipps.">

    <meta name="keywords" content="Gacha Guides, Tier Lists and more , {name} Build , {name} Guide , {name} Info , lost sword Charaktere, lost sword , Progression Guide ,">

    <meta name="author" content="Tychara Team">
    <meta property="og:title" content="Lost Sword  - {name} Guide">

    <title>Lost sword {name}</title>
    <link rel="stylesheet" href="../../Lost-Sword/css/main.css">
    <link rel="stylesheet" href="../../Lost-Sword/css/components/characterlayout.css">

    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HHK5DQPT94"></script>
    
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
            
            <div class="Character-Image"><img src="../../Lost-Sword/img/{name}.png" alt="{name} Png"></div>
        </div>


        <div class="Caracterinfocard">
           
            {level_stats_section}
            <div class="info-row">
                <span class="info-label">Rarity:</span>
                <span class="info-value">{rarity}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Profession:</span>
                <span class="info-value">{profession}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Formation:</span>
                <span class="info-value {formation.lower().replace(' ', '-')}">{formation}</span>
            </div>
        </div>

        <h2>Character Skills</h2>
        <div class="Character-Skills">
            {skills_html}
        </div>
    </div>

     
        <script src="../../Lost-Sword/script/script.js" defer></script>
</body>
</html>"""

        # Schreibe die HTML-Datei
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Created file for {name}")

    except Exception as e:
        print(f"Error processing character {name}: {e}")

print("All files created successfully!")