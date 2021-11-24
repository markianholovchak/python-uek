import json
book = {
    "name": "Miss Peregrine's home for peculiar children",
    "author": "Ransom Riggs",
    "genre": "Fiction",
    "publishYear": "2011",
    "pages": 352,
    "hasSequel": True
}

# with open("favourite2.json", "w") as f:
#     json.dump(book,f, indent=2)

with open("favourite.json", "w") as f:
    f.write(json.dumps([book], indent=2))