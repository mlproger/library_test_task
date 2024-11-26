import json

from models.book import BookFactory, Book
from services.file_manager import file_manager
from services.index_helper import index_manager
from ui.user_interface import UserInterface


class OutputHandler:
    COMMANDS = [
        "add",
        "del",
        "find",
        "read",
        "edit",
        "help"
    ]

    def __init__(self) -> None:
        self.current_action: str | None = None

    def command_handler(self):
        if self.current_action == "add":
            UserInterface.text_to_add()
            title: str = str(input("Название: "))
            author: str = str(input("Автор: "))
            try:
                year: int = int(input("Год издания: "))

                book: Book = BookFactory.create_book(title, author, year)
                index = index_manager.get_index()
                book_json = json.dumps(book, default=vars, ensure_ascii=False)
                file_manager.write(book=book_json, id=index)
                UserInterface.text_after_add()
            except ValueError:
                UserInterface.wrong_year_data()

            self.current_action = None

        elif self.current_action == "del":
            UserInterface.text_to_delete()
            try:
                id: int = int(input("id: "))
                try:
                    file_manager.delete(id)
                    UserInterface.text_to_delete()
                except KeyError:
                    UserInterface.not_found_id(id)

            except ValueError:
                UserInterface.wrong_id_input()
            self.current_action = None

        elif self.current_action == "read":
            data: list[list[str]] = file_manager.read_all()
            data.insert(0, ["ID", "Название", "Автор", "Год издания", "Статус"])
            widths: list[int] = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]
            row_format: str = " | ".join([f"{{:<{w}}}" for w in widths])
            for row in data:
                print(row_format.format(*row))
            self.current_action = None

        elif self.current_action == "edit":
            UserInterface.text_to_edit()
            try:
                id: int = int(input("id: "))
                status: str = str(input("Новый статус: "))
                edit: bool = file_manager.rewrite_data(id, status)
                if edit:
                    UserInterface.text_after_edit()
                else:
                    UserInterface.not_found_id(id)
            except Exception as e:
                print(e)
                UserInterface.wrong_id_input()

        elif self.current_action == "help":
            UserInterface.commands()
            self.current_action = None

        elif self.current_action == "find":
            UserInterface.text_to_find()
            num: str = str(input("Номер фильтра (1/2/3): "))
            search_val: str = str(input("Искомое значение: "))
            books: list[list[str]] = file_manager.find(num, search_val)
            if books is None:
                UserInterface.wrong_num_filters()
            elif not books:
                UserInterface.empty_result()
            else:
                books.insert(0, ["ID", "Название", "Автор", "Год издания", "Статус"])
                widths = [max(len(str(row[i])) for row in books) for i in range(len(books[0]))]
                row_format = " | ".join([f"{{:<{w}}}" for w in widths])
                for row in books:
                    print(row_format.format(*row))
                self.current_action = None
