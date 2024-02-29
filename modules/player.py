import random
import string
import pyfiglet as pfg

def get_player_name(term):
    name = ""
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.clear)
            print(term.yellow)
            print(pfg.figlet_format(f"Enter player name: {name}"))
            c = term.inkey()
            if c.isalpha():
                name += c
            elif c.name == "KEY_ENTER":
                if name.strip():
                    print('return')
                    return name
            elif c.name == "KEY_BACKSPACE":
                name = name[:-1]

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length)).strip()

player_attacks = [
    {
        "name": "Lunch break",
        "description": "Forces the opponent to stop working.",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Code review",
        "description": "Destroys the opponents self-confidence.",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Kick-Off",
        "description": "Inflicts major boredom.",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Headbutt",
        "description": "Giving the opponent head",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Bottle flip",
        "description": "Flipping a bottle",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Wheelchair",
        "description": "Puts you in a wheelchair",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Code quality",
        "description": "Checks your talent",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Discipline class",
        "description": "Puts the opponent in discipline class",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Code session",
        "description": "Wasting some time",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "CSS responsive (NOS)",
        "description": "Gives the opponent gridding issues",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Pair programming",
        "description": "No mate found",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Bugs",
        "description": "Good luck",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Frank wil Vliegen",
        "description": "Zo grijs als de grijze otto",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Tibor Kleinman Derksen",
        "description": "Net zoveel haar op het hoofd als op de ballen",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Ivo van Hurne",
        "description": "Iets te goed in nakijken",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Dick Heijink",
        "description": "It's in the name",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Remko Boschker",
        "description": "Wie?",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Stijn Kerst",
        "description": "It's beginning to look a lot like christmas",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Joost van Veenhuizen",
        "description": "Joost mag het niet weten",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Timothy Sealy",
        "description": "Brocoli TV",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Flamethrower",
        "description": "Straight fire",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Exam request",
        "description": "Waiting...",
        "damage": 30,
        "limit": 1
    },
    {
        "name": "Looking for teachers",
        "description": "Can you find a teacher?",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Water halen",
        "description": "Voor de koffie machine",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Stage",
        "description": "Teleports you to working camp",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "Bananen",
        "description": "Verhoog je libido",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Skip leg day",
        "description": "We don't need our legs",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Sound of silence",
        "description": "Hello darkness my old friend",
        "damage": 30,
        "limit": 1
    },
    {
        "name": get_random_string(6),
        "description": "Yup",
        "damage": 150,
        "limit": 1
    },
    {
        "name": get_random_string(12),
        "description": "Toxic",
        "damage": 200,
        "limit": 1
    },
    {
        "name": "Bel de wouten",
        "description": "Het is keiglad",
        "damage": 112,
        "limit": 1
    },
    {
        "name": "Zwarte piet",
        "description": "Pepernoten strooien",
        "damage": 30,
        "limit": 1
    },
    {
        "name": "Craigslist",
        "description": "Car insurance (cheap)",
        "damage": 25,
        "limit": 1
    },
    {
        "name": "Tiny-tinkerers",
        "description": "You know what's also tiny",
        "damage": 30,
        "limit": 1
    },
    {
        "name": "Morning music",
        "description": "Never gonna give you up",
        "damage": 50,
        "limit": 1
    },
    {
        "name": "website.hack()",
        "description": "Goodbye my lover",
        "damage": 30,
        "limit": 1
    }
]

def level_up(player: dict, xp: int):
    # gives the player xp and increases attack damage/ player hp if a certain amount of xp is reached.
    player["xp"] += xp
    player["hp"] += 50

    for attack in player["attacks"]:
        attack["damage"] += 10

    return player

def get_player():
    player = {
        "max_hp": 100,
        "hp": 100,
        "attacks": random.sample(player_attacks, 4),
        "xp": 0
    }
    
    for attack in player['attacks']:
        attack["limit"] = 1

    return player