# Створіть клас для представлення користувача з
# атрибутами: ім'я та вік. Додайте властивості для
# валідації віку користувача. Наприклад, вік повинен
# бути у межах від 0 до 120.

class User:

    _name = None
    _age = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be integer") 
        elif 0 > value or value > 120:
            raise ValueError("age must be more than 0 and less than 120")
        
        self._age = value
    
    def __str__(self) -> str:
        return f"name: {self._name}, age: {self._age}"

user = User()

user.name  = 'Bobby'
user.age = 12
print(user)