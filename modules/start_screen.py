import pyfiglet as pfg
def start_screen():
    with open('start_screen.txt') as start_game:
        for line in start_game:
            new_line = line.replace("$", "@")
            print(new_line[:-1])

    try:
        with open('high_score.txt') as top_3:
            scores = top_3.readlines()

            scores.sort(key=lambda x: int(x.split("/")[0]), reverse=True)

            count = 1
            for score in scores[:3]:
                high_score = pfg.figlet_format(f"{count}.   {score[:-1]}")
                print(high_score)
                count += 1
    except FileNotFoundError:
        pass
