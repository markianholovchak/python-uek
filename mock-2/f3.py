import re
def f3(t):
    pattern = r"\b\d{2,3}\b"
    suma = 0
    for foundNum in re.findall(pattern, t):
        # if len(foundNum) in range(2,4):
        suma+= int(foundNum)
    return suma

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))
