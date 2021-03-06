"""
Задача №3.
Напишите функцию average(lst), которая принимает список из чисел, и вычисляет среднее арифметическое элементов этого списка.
Среднее арифметическое определяется как сумма элементов, деленная на их количество.
С помощью встроенной функции round, округлите возвращаемое значение до тысячных.
Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
Имя файла: task_02_03.py
Имя функции: average
Возвращаемое значение: float
Тестовый набор данных №1:
Входные данные: [14, 8, 3, 1, 89, 2, 45]
Выходные данные: 23.143
Тестовый набор данных №2:
Входные данные: [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
Выходные данные: 0.411
"""

a = [14, 8, 3, 1, 89, 2, 45]
b = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]

def average(lst):
    aver = sum(lst) / len(lst)
    return round(aver, 3)


