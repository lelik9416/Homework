"""
Задача №2

Реализовать генератор случайных паролей указанной длины.

В пароле можно использовать любые символы в верхнем и нижнем регистре.

Например: password_generator(16), вернет случайный пароль длиной 16 символов.

Пригодится стандартный модуль random

Имя файла
    task_07_02.py
Имя функции-генератора
    password_generator
Возвращаемое значение
    Генератор
"""
import random
import string

def password_generator(n):
    sets = list(digits + ascii_letters + punctuation)
    while 1:
        yield ''.join(random.choice(sets) for i in range(n))    

