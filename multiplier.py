# Створіть клас Multiplier, який при ініціалізації
# отримує множник. Забезпечте можливість викликати
# цей об'єкт з аргументом та повертати множене
# значення.




class Multiplier:
    def __init__(self, x) -> None:
        if isinstance(x, (int, float)):
            self._multi = x
        else: raise ValueError("value must be a number")
    
    def __call__(self, x, *args, **kwds):
        if isinstance(x, (int, float)):
            result = self._multi * x
            return result
        else: raise ValueError("value must be a number")
    
    

m = Multiplier(3)
print(m(5))
