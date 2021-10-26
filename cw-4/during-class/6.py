def phonePad():
    for i in range(0, 7, 3):
        for j in range(1, 4):
            print(f"{i+j}", end=" ")
        print()


phonePad()
