"""Создайте класс-функцию, который считает факториал числа при
    вызове экземпляра.
    Экземпляр должен запоминать последние k значений.
    Параметр k передаётся при создании экземпляра.
    Добавьте метод для просмотра ранее вызываемых значений и
    их факториалов.


    Доработаем задачу 1.
    Создайте менеджер контекста, который при выходе
    сохраняет значения в JSON файл."""

import json


class Factorial:
    """FACTorial"""

    def __init__(self, count: int = 0, file_name: str = '') -> None:
        self.count = count
        self.results = []
        self.file_name = file_name
        self.file = None

    def __call__(self, number: int = 0) -> int:
        result = 1
        for i in range(1, number + 1):
            result *= i
        if len(self.results) == self.count:
            self.results.pop(0)
        self.results.append((number, result))
        return result

    def __str__(self) -> str:
        return str(self.results)

    def __enter__(self):
        self.file = open(self.file_name, 'w', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        dic = {}
        for ind, val in enumerate(self.results):
            dic[ind] = val
        print(dic)
        json.dump(dic, self.file)
        self.file.close()


FACT = Factorial(3, 'data.json')
print(FACT(2))
print(FACT(8))
print(FACT(5))
print(FACT(4))
print(FACT(2))
print(FACT(2))
print(FACT)

with FACT as a:
    print(a(5))
    print(a(3))
print()
print(FACT)
