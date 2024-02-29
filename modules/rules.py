def explain_rules():
    with open('rules.txt') as rules:
        for line in rules:
            new_line = line.replace("$", "@")
            print(new_line[:-1])
        
        start = input("")
        if start:
            pass
