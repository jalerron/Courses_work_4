from data.utils import create_database, create_tables, add_to_table
from tabulate import tabulate
from data.dbmanager import DBManager
import psycopg2


create_database_data1 = psycopg2.connect(host="localhost", database="postgres",
                        user="postgres", password="Swtbme666^^^", client_encoding="utf-8")


# create_database(create_database_data1)

conn_data = psycopg2.connect(host="localhost", database="course_work_5",
                        user="postgres", password="Swtbme666^^^", client_encoding="utf-8")





# create_tables(conn_data)
# add_to_table(conn_data, ['Сбербанк'])
db = DBManager(conn_data)
# print(tabulate(db.get_companies_and_vacancies_count(conn_data), headers=['Компания', 'Кол-во вакансий']))
# print(tabulate(db.get_all_vacancies(), headers=['Название компании', 'Название вакансии', 'Зарплата от', 'Зарплата до',
#                                                 'Валюта', 'Ссылка на вакансию']))
# print(tabulate(db.get_avg_salary(), headers=['Средняя зарплата по всем вакансиям']))
# print(tabulate(db.get_vacancies_with_higher_salary(), headers=['Название вакансии', 'Зарплата от',
#                                                                'Зарплата до', 'Валюта', 'Ссылка на вакансию']))

print(tabulate(db.get_vacancies_with_keyword(word), headers=['Название компании', 'Название вакансии',
                                                                 'Зарплата от', 'Зарплата до', 'Валюта',
                                                                 'Ссылка на вакансию']))

# for item in db.get_companies_and_vacancies_count(conn_data):
#     print(item)


def main():


    db = DBManager()



if __name__ == "__main__":
