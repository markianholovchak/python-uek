import re

with open('grades.txt', 'r') as f:
    content = f.read()
    grades = []
    for match in re.findall(r'\d.\d', content):
        grades.append(float(match))
    print(f"Arithmetic mean of grades: {round(sum(grades)/len(grades), 2)}")