import pyfiglet
def game_over_screen(term, score):
    with open('game_over.txt') as game_over:
        print(term.bold + term.green)
        for line in game_over:
            print(line[:-1])
        print(pyfiglet.figlet_format(f" You scored : {score}"))
        
