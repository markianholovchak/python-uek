class eBook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.currentPage = 1
        self.isOpen = False
    def open(self):
        if(self.isOpen):
            print("The book is already open!")
        else:
            self.isOpen = True
            print("Book has been opened!")
    def close(self):
        if(not self.isOpen):
            print("The book is already closed!")
        else:
            self.isOpen = False
            print("Book has been closed!")
    def displayStatus(self):
        print(f"Book title: {self.title}, Author: {self.author}, Pages: {self.pages}, Current Page: {self.currentPage}")
    def goToNextPage(self):
        if(self.currentPage < self.pages and self.isOpen):
            self.currentPage += 1
    def goToPrevPage(self):
        if self.currentPage > 0 and self.isOpen:
            self.currentPage -= 1

