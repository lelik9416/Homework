"""
Задача на самостоятельное изучение дополнительного материала

Python - язык с динамической типизацией. Часто это приводит к неочевидным ошибках, 
а так же необходимости добавлять дополнительный код с проверкой входных параметров.
Начиная с версии 3.5, в Python была добавлена возможность "подсказывать" 
типы аргументов функций и тип возвращаемого значения.
 
def summa(a:int, b:int) -> int:
    return a + b
    
Но этот механизм, как следует из названия, в момент выполнения программы 
не будет выбрасывать исключения, если тип данных переданного аргумента отличается от ожидаемого.
Требуется реализовать два декоратора: strict_argument_types и strict_return_type.
Декоратор strict_argument_types выбрасывает исключение TypeError с сообщением об ошибке 
'The argument "{}" must be "{}", passed "{}"', если один из типов данных аргументов функции не соответствует ожидаемому типу.
Декоратор strict_return_type выбрасывает исключение TypeError с сообщением об ошибке 
'The return value must be "{}", not "{}"' если функция возвращает значение, отличное от ожидаемого.

    Рефлексия - это способность компьютерной программы изучать и модифицировать свою структуру 
    и поведение (значения, мета-данные, свойства и функции) во время выполнения.
Воспользуемся рефлексией для того, чтобы получить имена аргументов функции и уточнения типов.
Для этого в Python есть стандартный модуль inspect
Из этого модуля нам нужен метод signature
Нужно самостоятельно по документации изучить какие свойства содержит объект, 
возвращаемый методом signature и какие из этих свойств необходимы для решения задачи.
Для проверки типа данных переменной использовать функцию isinstance(переменная, тип).
 например, isinstance(a, int).

Имя файла
    task_07_03.py
Имя функций-декораторов:
    - strict_argument_types
    - strict_return_type 
Пример использования №1

    @strict_argument_types
    @strict_return_type
    def summa(a:int, b:int) -> int:
        return a + b
                

Пример использования №2

    @strict_argument_types
    @strict_return_type
    def splitext(path:str) -> (str, str):
        filename, ext = os.path.splitext(path)
        return filename, ext.strip('.').lower()
"""
from inspect import signature

def strict_argument_types(func):
    def wrapper(*args):
        result = func(*args)
        for i in signature(func).parameters:
            sig = signature(func).parameters[i].annotation
        for j in args:
            par = type(j)
            if not isinstance(j, sig):
                return 'The argument "{}" must be "{}", passed "{}"'.format(args, sig, par)
        
        return result    
    return wrapper

"""
@strict_argument_types
def summa(a:int, b:int) -> int:
    return a + b

print(summa(1, 2))
"""


def strict_return_type(func):
    def wrapper(*args):
        result = func(*args)
        tp_result = type(result)
        
        for i in signature(func).parameters:
            sig = signature(func).parameters[i].annotation
                     
        if not tp_result == sig:
            return 'The return value must be "{}", not "{}"'.format(sig, tp_result)
        
        return result
    return wrapper


"""
@strict_argument_types
@strict_return_type
def summa(a:int, b:int) -> int:
    return a + b

print(summa(1, 2))
"""
