class Book:
    def __init__(self, title, author, pages) -> None:
        self.title=title
        self.author=author
        self.pages=pages

    def display_info(self):
        print(f"Info of the book\nTitle: {self.title}\nAuthor: {self.author}\nPages in book: {self.pages}")


b=Book("Three Mistakes of My Life", "Chetan Bhagat", 250)
b.display_info()