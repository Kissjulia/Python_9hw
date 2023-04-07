# 1) реализовать дескрипторы для любых двух классов
# Класс 1:

class Celsius:
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)
class Temperature:
    celsius = Celsius()
    def __init__(self, celsius):
        self.celsius = celsius
t = Temperature(25)
print(t.celsius) # Output: 25
t.celsius = 30
print(t.celsius) # Output: 30

# Класс 2:

class Password:
    def __init__(self, value):
        self._value = value
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Password must be a string')
        elif len(value) < 6:
            raise ValueError('Password must be at least 6 characters long')
        self._value = value
class User:
    password = Password('')
    def __init__(self, username, password):
        self.username = username
        self.password = password
u = User('John', 'password123')
print(u.password) # Output: password123
u.password = 'pass'
# Output: ValueError: Password must be at least 6 characters long
