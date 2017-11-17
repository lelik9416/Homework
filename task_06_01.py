"""
Задача №1

Требуется реализовать три декоратора: run_on_linux, run_on_macos, run_on_windows.

Декоратор должен проверять на какой операционной системе запущена программа и выполнять декорируемую функцию только в том случаи, если условие выполняется, в противном случаи функция обертка возвращает None

Необходимо самостоятельно найти, как определить имя текущей ОС.

Имя файла
    task_06_01.py
Имя функций-декораторов:
    - run_on_linux
    - run_on_macos
    - run_on_windows 
Пример использования

    @run_on_linux
    def func():
        print('Функция выполняется только на Linux!')
"""

import sys
 
def run_on_linux(system):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if sys.platform == 'linux':
                return result
        return wrapper
    return decorator


def run_on_windows(system):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if sys.platform == 'win32' or sys.platform == 'cygwin':
                return result
        return wrapper
    return decorator




def run_on_macos(system):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if sys.platform == 'darwin':
                return result
        return wrapper
    return decorator
