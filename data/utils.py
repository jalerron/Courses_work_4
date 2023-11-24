import psycopg2
from data.class_hh import HeadHunterAPI

conn = psycopg2.connect(host="localhost", database="postgres",
                        user="postgres", password="12345", client_encoding="utf-8")


def create_database(conn):
    """Создание базы данных, если её нет"""

    conn.autocommit = True
    cur = conn.cursor()

    # Проверка существования базы данных
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", ('courses_work_5',))
    exists = cur.fetchone()

    if not exists:
        # Создание базы данных, если она не существует
        cur.execute("CREATE DATABASE course_work_5")

    conn.close()

def create_tables(conn):

