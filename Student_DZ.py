""" Создайте класс студента.
    Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
    Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых."""


class FIO:
    """Класс дескриптор для проверки ФИО на первую заглавную букву и наличие только букв"""

    def __set_name__(self, owner, name):
        self.param_name = name

    def __set__(self, instance, value: str):
        if not str.istitle(value):
            raise ValueError(f'Bad {value}')
        for char in value:
                if not char.isalpha():
                    raise ValueError(f'Bad {value}')
        setattr(instance, self.param_name, value)
        

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Ocenka:
    def __init__(self, min: int = None, max: int = None) -> None:
        if min > max:
            min, max = max, min
        self.min = min
        self.max = max

    def __set_name__(self, owner, name):
        self.param_name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    # def __set__(self, instance, value):
    #     if not isinstance(value, int):
    #         raise TypeError(f'Значение {value} должно быть целым числом')
    #     if self.min is not None and value < self.min:
    #         raise ValueError(f'Значение {value} должно быть больше 18 или равно {self.min}')
    #     if self.max is not None and value >= self.max:
    #         raise ValueError(f'Значение {value} должно быть меньше {self.max}')
    #     setattr(instance, self.param_name, value)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min is not None and value < self.min:
            raise ValueError(
                f'Значение {value} должно быть больше или равно {self.min}')
        if self.max is not None and value > self.max:
            raise ValueError(
                f'Значение {value} должно быть меньше или равно {self.max}')
        setattr(instance, self.param_name, value)


class Student:
    """Класс Учись студент Кто не работает тот ЕСТ"""
    first_name = FIO
    name = FIO
    last_name = FIO
    num = int#Ocenka(2,5)

    def __init__(self, first_name, name, last_name , num) -> None:
        self.first_name = first_name
        self.name = name
        self.last_name = last_name
        self.num = num

    def __str__(self) -> str:
        return f'Студент : {self.first_name} {self.name} {self.last_name}'


PETIA = Student('иванов', 'Петр', 'Горлович' , 3)
print(PETIA)

if str.istitle('Uорлович'):
    print(1)
else:
    print(None)
