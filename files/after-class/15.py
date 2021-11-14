fileName = input("Enter a file name: ")
with open(fileName, 'r') as f:
    print(f"File name: {fileName}")
    print(f"Number of lines: {len(f.readlines())}")