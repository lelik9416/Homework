def display_menu():
    return ("""
Ежедневник. Выберете действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выход
"""
)

def call_number():
    while True:
        x = int(input("Введите число: "))
        if x == 1:
            print("Вывести список задач")
        elif x == 2:
            print("Добавить задачу")
        elif x == 3:
            print("Отредактировать задачу")
        elif x == 4:
            print("Завершить задачу")
        elif x == 5:
            print("Начать задачу сначала")
        elif x == 6:
            print("Выход")
        else:
            print(x)
        

print(display_menu())
print(call_number())
