with open('shoppinglist.txt', 'w') as f:
    with open('MeatAndFish.txt', 'r') as f1:
        f.write(f1.read())
    with open('GrainsAndBread.txt', 'r') as f2:
        f.write(f2.read())