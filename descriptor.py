# Створіть дескриптор для атрибуту, що зберігає
# розмір файлу. Додайте можливість зберігати розмір
# файлу в байтах, але представляти його у зручному для
# читання форматі (наприклад, КБ або МБ)

class FileSizeDescriptor:
    size_bytes = 0

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("size can not be less than 0")
        self.size_bytes = value
    
    def formatted(self):
        if self.size_bytes < 1024:
            return f'{self.size_bytes} B'
        elif self.size_bytes < 1024 ** 2:
            return f'{self.size_bytes / 1024} KB'
        elif self.size_bytes < 1024 ** 3:
            return f'{self.size_bytes / 1024 ** 2} MB'
        else:
            return f'{self.size_bytes/ 1024 ** 3} GB'
    
class File:
    size = FileSizeDescriptor()


file = File()
file.size = 2033000000
print(file.size.formatted())