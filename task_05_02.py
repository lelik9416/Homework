"""
Задача №2

Напишите функцию get_quadrant_number, которая принимает координаты точки X и Y 
и возвращает номер четверти, которой эта точка принадлежит. 
Помните, что если точка лежит на оси, то она не принадлежит ни одной четверти, 
в этом случаи нужно выбросить исключение типа ValueError без сообщения об ошибке.
Имя файла: task_05_02.py
Имя функции: get_quadrant_number
Тестовый набор данных №1:
Входные данные: 1 1
Выходные данные: 1
Тестовый набор данных №2:
Входные данные: -1 1
Выходные данные: 2
Тестовый набор данных №3:
Входные данные: -1 -1
Выходные данные: 3
Тестовый набор данных №4:
Входные данные: 1 -1
Выходные данные: 4
Тестовый набор данных №5:
Входные данные: 0 0
Исключение: ValueError
"""

x = int(input())
y = int(input())

def get_quadrant_number(x, y):
    if x!= 0 and y != 0:
        if x > 0 and y > 0:
            return 1
        elif x > 0 and y < 0:
            return 4
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
    else:
        raise ValueError()
    

          
print(get_quadrant_number(x, y))
