"""
Задача №1

Реализовать генератор чисел Фибоначчи.

Генератор принимает один обязательный аргумент - количество элементов последовательности.

Имя файла
    task_07_01.py
Имя функции-генератора
    fibonacci
Возвращаемое значение
    Генератор
Тестовый набор данных

    Входные данные
        10
    Выходные данные
        1 1 2 3 5 8 13 21 34 55
"""
def fibonacci(n):
    n1, n2 = 1, 1
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2