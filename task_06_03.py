"""
Задача №3

Требуется реализовать декоратор с параметрами return_namedtuple, 
который в случае, если функция возвращает кортеж, подменяет его именованным кортежем. 
Имена задаются в параметрах декоратора.

Для проверки типа данных переменной использовать функцию isinstance(переменная, тип).

Именованный кортеж находится в стандартном модуле collections.

(!) Декоратор универсальный, количество имен в кортеже переменное.

Имя файла
    task_06_03.py
Имя функции-декоратора
    return_namedtuple
Пример использования №1

    @return_namedtuple('one', 'two')
    def func():
        return 1, 2
                

Пример использования №2

    @return_namedtuple('one', 'two', 'three')
    def func():
        return 1, 2, 3
"""
from collections import namedtuple


def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                n = namedtuple('n', names)
                return n(*result)
            return result
        return wrapper
    return decorator

        
        
