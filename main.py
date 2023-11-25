from data.utils import create_database, create_tables, add_to_table
import psycopg2


create_database_data1 = psycopg2.connect(host="localhost", database="postgres",
                        user="postgres", password="Swtbme666^^^", client_encoding="utf-8")


create_database(create_database_data1)

conn_data = psycopg2.connect(host="localhost", database="course_work_5",
                        user="postgres", password="Swtbme666^^^", client_encoding="utf-8")

create_tables(conn_data)
add_to_table(conn_data, ['Сбербанк'])
