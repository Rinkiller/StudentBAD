"""
    Доработайте класс прямоугольник из прошлых семинаров.
    Добавьте возможность изменять длину и ширину
    прямоугольника и встройте контроль недопустимых значений
    (отрицательных).
    Используйте декораторы свойств.


    Доработаем прямоугольник и добавим экономию памяти
    для хранения свойств экземпляра без словаря __dict__.

    Изменяем класс прямоугольника.
    Заменяем пару декораторов проверяющих длину и ширину
    на дескриптор с валидацией размера.


"""


class Descript_Plozit:
    """Descriptor проверяет что числа положительные и попадают в размеры"""

    def __init__(self, min: int = None, max: int = None) -> None:
        if min > max:
            min, max = max, min
        self.min = min
        self.max = max

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min is not None and value < self.min:
            raise ValueError(
                f'Значение {value} должно быть больше или равно {self.min}')
        if self.max is not None and value >= self.max:
            raise ValueError(f'Значение {value} должно быть меньше {self.max}')


class Square_New:
    """Square_New"""
    #__slots__ = ('a', 'b')
    a = Descript_Plozit(2, 100)
    b = Descript_Plozit(2, 100)

    def __init__(self, a: int, b: int = None) -> None:
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a
    # @property
    # def a(self) -> int:
    #     return self.a

    # @property
    # def b(self) -> int:
    #     return self.b

    # @a.setter
    # def a(self , a:int) -> None:
    #     if a > 0:
    #         self.a = a
    #     else:
    #         raise ValueError

    # @b.setter
    # def b(self , b:int) -> None:
    #     if b > 0:
    #         self.b = b
    #     else:
    #         raise ValueError

    # def square(self) -> int:
    #     return self.a * self.b

    def perimetr(self) -> int:
        return 2*(self.a + self.b)

    def _add__(self, other):
        newa = self.a + other.a
        newb = self.b + other.b
        return Square_New(newa, newb)

    def __sub__(self, other):
        if self.a < other.a or self.b < other.b:
            raise ValueError
        return Square_New(self.a - other.a, self.b - other.b)

    def __eq__(self, other) -> bool:
        return self.perimetr() == other.perimetr()

    def __gt__(self, other) -> bool:
        return self.perimetr() > other.perimetr()

    def __str__(self) -> str:
        return f'Прямоугольник со сторонами: а = {self.a} сторона b = {self.b}'


kvadr = Square_New(5)
priam = Square_New(10, 6)
print(kvadr)
print(priam)
kvadr.a = 12
priam.a = priam.b
print(kvadr)
print(priam)
