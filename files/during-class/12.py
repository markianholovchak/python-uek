with open('shopping.txt', 'a') as f:
    newItem = input("Enter a new item to buy: ")
    f.write(f"{newItem}\n")