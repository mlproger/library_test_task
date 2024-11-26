class IndexHelper:
    def __init__(self, path: str):
        self.path = path

    def get_index(self):
        with open(self.path, 'r') as file:
            index = int(file.read().strip())

        with open(self.path, 'w') as file:
            file.write(str(index + 1))

        return index


index_manager: IndexHelper = IndexHelper(path="db/index.txt")
