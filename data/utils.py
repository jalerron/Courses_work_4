import psycopg2
from data.class_hh import HeadHunterAPI


def create_database(conn_data):
    """Создание базы данных"""

    conn_data.autocommit = True
    cur = conn_data.cursor()

    # Проверка существования базы данных
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", ('course_work_5',))
    exists = cur.fetchone()

    if not exists:
        # Создание базы данных
        cur.execute("CREATE DATABASE course_work_5")

    cur.close()


def create_tables(conn_data):
    with conn_data as conn_:
        with conn_.cursor() as cur:
            # Создание таблиц

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS companies (
                        company_id INTEGER PRIMARY KEY,
                        company_name varchar(255),
                        url varchar(30),
                        open_vacancies INTEGER
                        )""")

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS vacancies (
                        vacancy_id SERIAL PRIMARY KEY,
                        vacancies_name varchar(255),
                        salary_from INTEGER,
                        salary_to INTEGER,
                        currency varchar(10),
                        requirement TEXT,
                        vacancies_url TEXT,
                        company_id INTEGER REFERENCES companies(company_id)
                        )""")

            conn_.commit()


def add_to_table(conn_data, companies):
    data_hh = HeadHunterAPI()
    companies_data = data_hh.get_companies(companies)
    with conn_data as conn_:
        with conn_.cursor() as cur:
            for company in companies_data:
                # print(company)
                # Получение данных о компании по API
                # Добавление компании в таблицу с игнорированием конфликта
                cur.execute('INSERT INTO companies (company_id, company_name, url, open_vacancies) '
                            'VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING RETURNING company_id',
                            (company['company_id'], company['company_name'],
                             company['url'], company['open_vacancies']))

                # Получение вакансий для компании по API
                vacancies_list = data_hh.get_vacancies(company['company_id'])

                for vacancy_data in vacancies_list:
                    # Добавление вакансии в таблицу с игнорированием конфликта
                    cur.execute('INSERT INTO vacancies (vacancy_id, vacancies_name, '
                                'salary_from, salary_to, currency, '
                                'requirement, vacancies_url, company_id) '
                                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING',
                                (vacancy_data['vacancy_id'], vacancy_data['vacancies_name'],
                                 int(vacancy_data['salary_from']), int(vacancy_data['salary_to']), vacancy_data['currency'],
                                 vacancy_data['requirement'], vacancy_data['vacancy_url'],
                                 vacancy_data['company_id']))

            conn_.commit()
