from data.utils import create_database, create_tables, add_to_table
from tabulate import tabulate
from data.dbmanager import DBManager

def main():

    db = DBManager()
    while True:
        user_input = input(
                'Выберетине необходимый пункт:\n'
                '1 - Получить список компаний с количеством открытых вакансий\n'
                '2 - Получить список всех вакансий\n'
                '3 - Получить среднюю зарплату по всем вакансиям\n'
                '4 - Получить список вакансий с зарплатой вышего среднего\n'
                '5 - Поиск вакансий по ключевому слову\n'
                '0 - Завершенить программу\n'
              )

        if user_input == '0':
            print('До свидания!')
            break
        elif user_input == '1':
            print(tabulate(db.get_companies_and_vacancies_count(), headers=['Компания', 'Кол-во вакансий']))
            print()
            user_answer = input('Хотите продолжить?\n(1-продолжить, 2-завершить программу)\n')
            if user_answer == '1':
                print()
                continue
            else:
                print('До свидания!')
                break
        elif user_input == '2':
            print(tabulate(db.get_all_vacancies(),
                           headers=['Название компании', 'Название вакансии', 'Зарплата от', 'Зарплата до',
                                    'Валюта', 'Ссылка на вакансию']))
            print()
            user_answer = input('Хотите продолжить?\n(1-продолжить, 2-завершить программу)\n')
            if user_answer == '1':
                print()
                continue
            else:
                print('До свидания!')
                break
        elif user_input == '3':
            print(tabulate(db.get_avg_salary(), headers=['Средняя зарплата по всем вакансиям']))
            print()
            user_answer = input('Хотите продолжить?\n(1-продолжить, 2-завершить программу)\n')
            if user_answer == '1':
                print()
                continue
            else:
                print('До свидания!')
                break
        elif user_input == '4':
            print(tabulate(db.get_vacancies_with_higher_salary(),
                           headers=['Название вакансии', 'Зарплата от',
                                    'Зарплата до', 'Валюта', 'Ссылка на вакансию']))
            print()
            user_answer = input('Хотите продолжить?\n(1-продолжить, 2-завершить программу)\n')
            if user_answer == '1':
                print()
                continue
            else:
                print('До свидания!')
                break
        elif user_input == '5':
            word = input('Введите ключевое слово: ')
            print(tabulate(db.get_vacancies_with_keyword(word), headers=['Название компании', 'Название вакансии',
                                                                             'Зарплата от', 'Зарплата до', 'Валюта',
                                                                             'Ссылка на вакансию']))
            print()
            user_answer = input('Хотите продолжить?\n(1-продолжить, 2-завершить программу)\n')
            if user_answer == '1':
                print()
                continue
            else:
                print('До свидания!')
                break
        else:
            print('Данного пункта нет')



if __name__ == "__main__":
    companies = ['Сбербанк', 'Google', 'Контур', 'Магнит', 'Яндекс', 'Додо', 'МТС', 'Тинькофф', 'ИнфоТеКС', '2ГИС']
    create_database()
    create_tables()
    add_to_table(companies)
    main()

