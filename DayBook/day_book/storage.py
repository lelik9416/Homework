import os.path as Path
import sqlite3
import pendulum

SQL_SELECT_ALL = """
    SELECT id, task, performance, place, created
    FROM day_book
"""

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_TASK_BY_PERFORMANCE = SQL_SELECT_ALL + " WHERE performance=?"

SQL_SELECT_PLACE_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_INSERT_TASK = """
    INSERT INTO day_book (task) VALUES (?)
"""

SQL_UPDATE_TASK = """
    UPDATE day_book SET task=? WHERE id=?
"""

SQL_UPDATE_PERFORMANCE = """
    UPDATE day_book SET performance=? WHERE id=?
"""

SQL_INSERT_PLACE = """
    INSERT INTO day_book (place) VALUES (?)
"""

SQL_UPDATE_PLACE = """
    UPDATE day_book SET place=? WHERE id=?
"""

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect(day_book):    
    conn = sqlite3.connect(day_book)
    conn.row_factory = dict_factory
    return conn

def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())

def add_task(conn, task):
    if not task:
        print('Задача не можеть быть пустой!')
        return
    
    with conn:
        found = find_task_by_pk(conn, task)
        
        if found:
            return found.get('task')
    
    cursor = conn.execute(SQL_INSERT_TASK, (task, ))
        
    pk = cursor.lastrowid #последний сгенерированный запросом insert РК
          
    conn.execute(SQL_UPDATE_TASK, (task, pk))
    return pk, task

def task_list(conn):
    """Возвращает список задач"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL) 
        return cursor.fetchall()

def find_task_by_pk(conn, pk):
    """Возвращает задачу по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk, ))
        return cursor.fetchone()

def change_task(conn, task, pk):
    with conn:
        conn.execute(SQL_UPDATE_TASK, (task, pk))
    
def change_performance(conn, pk, performance):
    with conn:
        conn.execute(SQL_UPDATE_PERFORMANCE, (performance, pk))

def find_place_by_pk(conn, pk):
    with conn:
        return conn.execute(SQL_SELECT_PLACE_BY_PK, (pk, )).fetchone()
    
def change_place(conn, pk, place):
    with conn:
        conn.execute(SQL_UPDATE_PLACE, (place, pk))
    
