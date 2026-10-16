class book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrowed(self):
        self.is_borrowed = True
        print("is_borrowed has been set to true for now.")

    def return_book(self):
        self.is_borrowed = False
        print("is_borrowed has been set to false.")

        book1 = book("The Great Gatsby", "F. Scott Fitzgerald", False)
        book2 = book("To Kill a Mockingbird", "Harper Lee", False)
        book3 = book("1984", "George Orwell", False)


obj = book()