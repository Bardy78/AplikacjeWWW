class FileManager:
    file_path = ""

    def __init__(self, path):
        self.file_path = f'{path}.txt'
        try:
            x = open(self.file_path, 'x')
        except:
            pass

    def add(self, text):
        x = open(self.file_path, 'a')
        x.write(text)
        x.close()

    def read(self):
        x = open(self.file_path, "r")
        result = x.read()
        x.close()
        return result