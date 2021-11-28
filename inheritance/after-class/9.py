class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
class paperBook(Book):
    def __init__(self,title, author, year, pages):
        self.pages = pages
        super().__init__(title, author, year)
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nPages: {self.pages}\nType: Paper Book"

class eBook(Book):
    def __init__(self,title, author, year, file):
        self.file = file
        super().__init__(title, author, year)
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nSaved in: {self.file}\nType: eBook"

paperVersion = paperBook("Harry Potter", "J.K. Rowling", "2002", 318)
eVersion = eBook("It", "Stewen King", "2016", "it.pdf")
print(paperVersion)
print(eVersion)