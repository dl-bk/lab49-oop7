# Створіть клас для представлення відомостей про
# замовлення. Забезпечте, щоб номер замовлення був
# тільки для читання за допомогою керованих атрибутів,
# але його можна було переглядати.
import random

class Order:
    def __init__(self, product, price, count) -> None:
        self.__id = random.randint(1000000, 100000000)
        self._product = product
        self._price = price
        self._count = count
    
    @property
    def id(self):
        return self.__id
    
    @property
    def product(self):
        return self._product
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._price = value
        else: raise ValueError("price must be integer or float")
        
    
    @property
    def count(self):
        
        return self._count
    
    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise ValueError("count must be integer")
        self._count = value
    
    def __str__(self) -> str:
        return f"id: {self.__id}, product: {self._product}, price: {self._price}, count: {self._count}"


order = Order("a", 12, 4)

print(order.id)
order.price = 32
order.count = 8
print(order)