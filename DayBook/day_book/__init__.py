import sys
import os.path as Path
from day_book import storage

get_connection = lambda : storage.connect('day_book.sqlite')

def action_task_list():
    """Вывести все задачи"""
    with get_connection() as conn:
        rows = storage.task_list(conn)
    
    template = '{row[id]} - {row[task]} - {row[performance]} - {row[place]} - {row[created]}'
    
    print('\nID - Название задачи - Статус - Место - Время создания')
    print('Статус: 1/0 - задача не выолнена, 1/1 - задача выполнена\n')
    
    for row in rows:
        print(template.format(row=row))

def action_add_task():
    """Добавить задачу"""
    task = input('\nВведите новую задачу: ')
    
    if not task:
        return
    
    with get_connection() as conn:
        task = storage.add_task(conn, task)
    
    print('\nЗадача: "{}" добавлена!'.format(task))

             
def action_change_task():
    """Изменить задачу"""
    pk = input('\nВведите номер задачи: ')
    
    if pk:
        with get_connection() as conn:
            task = storage.find_task_by_pk(conn, pk)
        if task: 
            task1 = input('\nВведите новую задачу: ')   
            with get_connection() as conn:
                task1 = storage.change_task(conn, task1, pk)
                print('\nЗадача "{}" обновлена'.format(pk))
        else:
            print('\nЗадача "{}" не найдена!'.format(pk))
 
    
def action_end_task():
    """Закончить задачу"""
    pk = input('\nВведите номер задачи: ')
    
    if pk:
        with get_connection() as conn:
            task = storage.find_task_by_pk(conn, pk)
        if task:
            id_change = '1/1'
            with get_connection() as conn:
                task = storage.change_performance(conn, pk, id_change)
                print('\nСтатус задачи "{}" изменен!'.format(pk))
        else:
            print('\nЗадача "{}" не найдена!'.format(pk))
                

def action_again_task():
    """Начать задачу сначала"""
    pk = input('\nВведите номер задачи: ')
    
    if pk:
        with get_connection() as conn:
            task = storage.find_task_by_pk(conn, pk)
        if task:
            id_change = '0/1'
            with get_connection() as conn:
                task = storage.change_performance(conn, pk, id_change)
                print('\nСтатус задачи "{}" изменен!'.format(pk))
        else:
            print('\nЗадача "{}" не найдена!'.format(pk))


def action_change_place():
    pk = input('\nВведите номер задачи: ')
    
    if pk:
        with get_connection() as conn:
            place = storage.find_place_by_pk(conn, pk)
        if place:
            place1 = input('\nВведите место задачи: ')
            with get_connection() as conn:
                place1 = storage.change_place(conn, pk, place1)
                print('\nМесто задачи "{}" изменено!'.format(pk))
        else:
            print('\nЗадча "{}" не найдена!'.format(pk))
                
    
def action_menu():
    """Показать меню"""
    print("""
Ежедневник:

1. Вывести список задач
2. Добавить задачу
3. Изменить задачу
4. Закончить задачу
5. Начать задачу сначала
6. Изменить место задачи
m. Показать меню
q. Выйти""")

def action_exit():
    """Выйти из программы"""
    sys.exit(0)

def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )
    
    with get_connection() as conn:
        storage.initialize(conn, creation_schema)
        
    actions = {
        '1': action_task_list,
        '2': action_add_task,
        '3': action_change_task,
        '4': action_end_task,
        '5': action_again_task,
        '6': action_change_place,
        'm': action_menu,
        'q': action_exit
    }
    
    action_menu()
    
    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        
        if action:
            action()
        else:
            print('\nНеизвестная команда!')
