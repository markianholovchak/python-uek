with open('powers.txt', 'w') as f:
    for i in range(1, 11):
        if i == 10:
            f.write(f"{i},{i**2},{i**3}")
        else:
            f.write(f"{i},{i**2},{i**3}\n")