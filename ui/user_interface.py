class UserInterface:

    @staticmethod
    def greeting() -> None:
        print(
            "Добро пожаловать в программу по имитации электронной библиотеки!\n"
            "Для работы используйте следующие команды:\n"
            "   add -> Добавить книгу в библиотеку\n"
            "   del -> Удалить книгу\n"
            "   find -> Поиск книги по фильтрам\n"
            "   all -> Вывод всех книг из библиотеки\n"
            "   edit -> Редактировать книгу\n"
            "   help -> Список доступных команд"
        )


    @staticmethod
    def commands() -> None:
        print(
            "   add -> Добавить книгу в библиотеку\n"
            "   del -> Удалить книгу\n"
            "   find -> Поиск книги по фильтрам\n"
            "   all -> Вывод всех книг из библиотеки\n"
            "   edit -> Редактировать книгу\n"
            "   help -> Список доступных команд"
        )

    @staticmethod
    def wrong_command() -> None:
        print(
            "Извините, но такой команды не существует\n"
            "Напишите help для просмотра доступных команд"
        )

    @staticmethod
    def text_to_add() -> None:
        print("Чтобы добавить новую книгу, введите название, автора и год издания")


    @staticmethod
    def text_after_add() -> None:
        print("Книга успешно добавлена в библиотеку!")


    @staticmethod
    def text_to_delete() -> None:
        print("Для удаления книгии введите ее id")


    @staticmethod
    def text_after_delete() -> None:
        print("Книга успешно удалена!")


    @staticmethod
    def text_to_edit() -> None:
        print("Для изменения статуса книги введите ее id и новый статус")



    @staticmethod
    def wrong_count_data() -> None:
        print("Ошибка. Для добавления книги введите 3 характеристики: название, автор, год издания через пробел")


    @staticmethod
    def wrong_year_data() -> None:
        print("Ошибка. Год издания книги должен быть числом")

    @staticmethod
    def wrong_id_input() -> None:
        print("id книги должен быть числом")

    @staticmethod
    def not_found_id(id: int) -> None:
        print(f"Ошибка. Книга с id {id} не найдена")


    @staticmethod
    def text_after_edit() -> None:
        print("Статус книги успешно изменен!")


    @staticmethod
    def text_to_find() -> None:
        print(
            "Осуществить поиск по ...\n"
            "   1. Названию\n"
            "   2. Автору\n"
            "   3. Году издания"
        )

    @staticmethod
    def wrong_num_filters() -> None:
        print("Неверный номер фильтра. Вводить следует только 1, 2 или 3")

    @staticmethod
    def empty_result() -> None:
        print("По найденым фильтрам найденно 0 книг")

