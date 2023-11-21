# Створіть клас Calculator, який може виконувати
# операції додавання, віднімання, множення та ділення.
# Кожна операція буде реалізована як метод класу.
# Об'єкт класу Calculator буде функтором, що може
# викликатися для виконання обраної операції.


class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b
    
    def multi(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("You can not divide by zero")
        return  a / b

    def __call__(self, *args, **kwargs):
        match args[0]:
            case "+": return self.add(args[1], args[2])
            case "-": return self.sub(args[1], args[2])
            case "*": return self.multi(args[1], args[2]) 
            case "/": return self.divide(args[1], args[2])
            case _  : return "invalid operation"


calcutate = Calculator()
print(calcutate("/", 4, 2))
print(calcutate("*", 4, 2))
print(calcutate("-", 4, 2))
print(calcutate("+", 4, 2))