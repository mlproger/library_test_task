class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = "В наличии"


class BookFactory:
    @staticmethod
    def create_book(title: str, author: str, year: int) -> Book:
        return Book(title, author, int(year))

