"""
Задача №2

Требуется реализовать декоратор с параметрами pause, который приостанавливает выполнение функции на указанное количество секунд.

В решении пригодится стандартный модуль time.

Имя файла
    task_06_02.py
Имя функции-декоратора
    pause
Пример использования

    @pause(2)
    def func():
        print('Фунция выполняется с задержкой!')
"""

import time


def pause(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            return func(*args, **kwargs)
        return wrapper
    return decorator   
