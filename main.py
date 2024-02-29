from modules.player import get_player, level_up, get_player_name
from modules.enemies import get_enemy
from modules.rules import explain_rules
from modules.game_over_screen import game_over_screen
from modules.start_screen import start_screen
from blessed import Terminal
from wouter import render_box, check_spelling
import time
import threading
import random
from modules.audio_player import play_music, stop_music

FILE = "high_score.txt"
BOX_SIZE = 60
SPELL_ERRORS_ALLOWED: int = 0
CASE_SENSITIVE_SPELLING: bool = True

glob_text = ''
def deal_damage(damage: int, target: dict):
    # inflicts damage on an enemy or player
    target["hp"] -= damage
    return target


def check_win(player: dict, enemy: dict) -> bool:
    # if the enemy or player is dead
    return player["hp"] <= 0 or enemy["hp"] <= 0


def add_high_score(score: int, name: str):
    with open(FILE, "a") as f:
        f.write(f"{str(score)}/{name}\n")


def load_high_score() -> dict:
    high_scores = {}
    try:
        with open(FILE) as f:
            for line in f:
                parts = line.strip().split("/")
                score = int(parts[0])
                name = parts[1]
                high_scores[name] = score

        return dict(sorted(high_scores.items(), key=lambda item: item[1], reverse=True))
    except FileNotFoundError as error:
        print(error)
        exit()


def draw_box(term, x, y, box_width, box_height, text):
    # Draw the box
    print(term.move(y, x) + "╔" + "═" * (box_width - 2) + "╗")
    for i in range(1, box_height - 1):
        print(term.move(y + i, x) + "║" + " " * (box_width - 2) + "║")
    print(term.move(y + box_height - 1, x) + "╚" + "═" * (box_width - 2) + "╝")

    # Print the text inside the box
    print(term.move(y + 1, x + 2) + text)


def create_hp_bar(player):
    if type(player["hp"]) is int and type(player["max_hp"]) is int:
        hp = "█" * player["hp"]
        lost_hp = " " * (player["max_hp"] - player['hp'])
        return hp + lost_hp
    return None

def attack_computer(player: dict, enemy: dict, word: str):
    global glob_text
    for attack in player['attacks']:
        if check_spelling(word, attack['name'], SPELL_ERRORS_ALLOWED, CASE_SENSITIVE_SPELLING):
            if attack['limit'] <= 0:
                return
            # deal damage to computer
            enemy['hp'] -= attack['damage']

            attack['limit'] -= 1

            glob_text = f"You inflicted {attack['name']} on {enemy['name']}, dealing {attack['damage']} damage"
            print(term.clear)
            break
    else:
        # deal 5 damage to self
        print(term.bold_red)
        player['hp'] -= 5
        glob_text = "NOOOB! 5 damage on yourself for a typo!"

def get_attack_names(player: dict):
    res = []
    for attack in player['attacks']:
        res.append(f"{attack['name']}{' '*(BOX_SIZE- len(attack['name'])-8)}{attack['damage']} DMG\n{attack['description']}")
    return res

def attack_player(player, enemy, interval):
    global glob_text
    while True:
        time.sleep(interval)
        attack = enemy['attacks'][random.randint(0, 4)]
        print(term.orange)
        player['hp'] -= attack['damage']
        glob_text = f"SHIT!!!!!!!!!! {enemy['name']} inflicts {attack['name']} on you, dealing {attack['damage']} damage."
        render_box(term, glob_text, 0, 0+32, BOX_SIZE*2, 3)
        render_box(term, f"HP:[{player['hp']*'█'+ ' ' * (player['max_hp'] - player['hp'])}]\nType your attack: "+ word, 0, 45, BOX_SIZE*2, 4)
        
        if type(enemy['hp']) is int and enemy['hp'] <= 0:
            break

        if type(player['hp']) is int and player['hp'] <= 0:
            break

def get_pp(player, attack_num):
    return player['attacks'][attack_num]['limit']
    
# main function
if __name__ == "__main__":

    while True:
        term = Terminal()
        score = 0
        interval = 10
        username = get_player_name(term)
        print(term.clear + term.white)
        start_screen()
        input()
        print(term.clear)
        explain_rules()
        player = get_player()
        enemy = get_enemy()
        glob_text = f"A WILD {enemy['name']} APPEARED!!"
        word = ""
        player_attacks = get_attack_names(player)

        attack_thread = threading.Thread(target=attack_player, args=(player, enemy, interval), daemon=True)
        attack_thread.start()
        play_music("battle_music.mp3")

        with term.cbreak(), term.hidden_cursor():
            while True:
                print(term.clear)
                print(term.bold)
                if type(player['hp']) is int:
                    if player['hp'] <= 40:
                        print(term.red3)
                    elif player['hp'] <= 60:
                        print(term.orange)
                    elif player['hp'] <= 80:
                        print(term.green)
                enemy_hp_bar = create_hp_bar(enemy)

                render_box(term, f"{enemy['name']}\nHP:[{enemy_hp_bar}]", 0, 0, BOX_SIZE*2, 4)

                if type(enemy['sprite']) is str:
                    e_h = enemy['sprite'].count('\n')
                
                print(term.move(5, 0) + enemy['sprite'])
                render_box(term, f"Score: {score}", 0, 29, BOX_SIZE, 3)
                render_box(term, glob_text, 0, 32, BOX_SIZE*2, 3)
                # dialog box
                # draw enemy
                # attacks in boxes
                old_hp = player['hp']
                if get_pp(player, 0) == 0 and get_pp(player, 1) == 0 and get_pp(player, 2) == 0 and get_pp(player, 3) == 0:
                    player = get_player()
                    player_attacks = get_attack_names(player)
                    player['hp'] = old_hp
                if get_pp(player, 0) != 0:
                    render_box(term, player_attacks[0], 0, 35, BOX_SIZE, 5)
                if get_pp(player, 1) != 0:
                    render_box(term, player_attacks[1], BOX_SIZE, 35, BOX_SIZE, 5)
                if get_pp(player, 2) != 0:
                    render_box(term, player_attacks[2], 0, 40, BOX_SIZE, 5)
                if get_pp(player, 3) != 0:
                    render_box(term, player_attacks[3], BOX_SIZE, 40, BOX_SIZE, 5)


                # box the user can type in
                hp_bar = create_hp_bar(player)
                render_box(term, f"HP:[{hp_bar}]\nType your attack: "+ word, 0, 45, BOX_SIZE*2, 4)

                new_char = term.inkey()

                if new_char.name == "KEY_BACKSPACE":
                    if word:
                        word = word[:-1]
                        print(term.pink)

                elif new_char.name == "KEY_ENTER":
                    attack_computer(player, enemy, word)
                    word = ""
                else:
                    print(term.white)
                    word += new_char

                if type(player['hp']) is int and player['hp'] <= 0:
                    stop_music()
                    print(term.clear)
                    game_over_screen(term, score)
                    if score > 0:
                        add_high_score(score, username)
                    high_scores = load_high_score()
                    time.sleep(3)
                    print(term.clear)
                    break
                

                elif type(enemy['hp']) is int and enemy['hp'] <= 0:
                    if type(player['hp']) is int:
                        score += player['hp'] + 100
                    enemy = get_enemy()
                    if enemy['name'] == "CEO of Programming":
                        enemy['hp'] = 200
                    else:
                        enemy['hp'] = 100
                    player = get_player()
                    player['hp'] = 100
                    player_attacks = get_attack_names(player)
                    for i in range(4):
                        player['attacks'][i]['limit'] = 1
                    interval -= .5
                    attack_thread = threading.Thread(target=attack_player, args=(player, enemy, interval), daemon=True)
                    attack_thread.start()

                    glob_text = f"A WILD {enemy['name']} APPEARED!!"

                print(flush=True)
