"""# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1."""

class GeneratorFactorial:
    """Generator_Factorial"""
    def __init__(self, stop: int, start: int = 1, step: int = 1) -> None:
        if start > stop:
            raise ValueError
        if start == 0:
            start = 1
        if step == 0:
            raise ValueError
        self.start = start
        self.stop = stop
        self.step = step
        self.last = start
        self.next = start * (start + step)

    def __iter__(self):
        return self

    def __next__(self) -> int:
        while self.next < self.stop: 
            rez = 1
            for index in range(1 , self.next):
                rez *= index
            self.last = self.next
            self.next += self.step
            return rez
        raise StopIteration


GENER = GeneratorFactorial(10 , 1 , 1)
for i in GENER:
    print(i)
