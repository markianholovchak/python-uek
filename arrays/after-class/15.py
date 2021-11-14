arr = ["red","black","purple"]
with open('./arrays/after-class/colors.txt', 'w') as f:
    for color in arr:
        f.write(f"{color}\n")
    