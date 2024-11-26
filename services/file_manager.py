import json


class FileManager:

    def __init__(self, path: str) -> None:
        self.path = path

    def write(self, book: dict, id: int) -> None:
        with open(self.path, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) > 2 and lines[-2].strip()[-1] != ',':
            lines[-2] = lines[-2].strip() + ",\n"
        data = f'"{id}": {book}\n'
        lines.insert(-1, data)

        with open(self.path, mode="w", encoding='utf-8') as file:
            file.writelines(lines)

    def delete(self, id: int):
        with open(self.path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            del data[str(id)]

        with open(self.path, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=1)

    def read_all(self) -> list[list[str]]:
        with open(self.path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            books = []
            for i in data:
                books.append([i, *data[i].values()])
            return books

    def edit_data(self, id: int, new_status: str) -> dict | None:
        with open(self.path, mode='r+', encoding='utf-8') as file:
            data: dict = json.load(file)
            try:
                data[str(id)]["status"] = new_status
                return data
            except:
                return None

    def rewrite_data(self, id: int, new_status: str) -> bool:
        data = self.edit_data(id,new_status)
        if data:
            with open(self.path, mode='w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=1)
            return True
        return False

    def find(self, num: str, search_val: str) -> list[list[str]] | None:
        filters = {
            "1": "title",
            "2": "author",
            "3": "year"
        }
        books = []
        try:
            key = filters[num]
        except:
            return None
        with open(self.path, mode='r', encoding='utf-8') as file:
            data: dict = json.load(file)

            for id, item in data.items():
                if str(item.get(key)) == search_val:
                    books.append([id, *data[id].values()])
            return books



file_manager = FileManager("db/data.json")
