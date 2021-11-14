filmTitles = ['Red notice', "6 Underground", "Never give up", "Work it", "Deadpool"]
with open("films.txt", 'w') as f:
    for film in filmTitles:
        f.write(f"{film}\n")