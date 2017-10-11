import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, task, description, performance, created
    FROM day_book
"""

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_TASK_BY_DESCRIPTION = SQL_SELECT_ALL + " WHERE description=?"

SQL_SELECT_TASK_BY_PERFORMANCE = SQL_SELECT_ALL + " WHERE performance=?"

SQL_SELECT_TASK_BY_CREATED = SQL_SELECT_ALL + " WHERE created=?"

SQL_INSERT_TASK = """
    INSERT INTO day_book (task) VALUES (?)
"""

SQL_UPDATE_PERFOMANCE = """
    UPDATE day_book SET performance=? WHERE id=?  
"""

def connect(day_book):    
    conn = sqlite3.connect(day_book)
    return conn

def initialize(conn, creation_shema):
    with conn, open(creation_shema) as f:
        conn.executescript(f.read())

def task_list(conn, task, domain=''):
    """Возвращает список задач"""

def find_description(conn, description):
    """Возвращает описание задачи"""    

def find_performance(conn, performance):
    """Возвращает статус выполнения"""

