import psycopg2

class DBManager:
    """
    Класс для работы с базой данных
    """
    def __init__(self, conn_data):
        self.conn_data = conn_data

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        with self.conn_data as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT company_name, COUNT(vacancies_name) AS count_vacancies "
                            f"FROM companies "
                            f"JOIN vacancies USING(company_id)"
                            f"GROUP BY companies.company_name")
                data = cur.fetchall()
            conn.commit()
        return data

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn_data as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT companies.company_name, vacancies.vacancies_name, "
                            f"vacancies.salary_from, vacancies.salary_to, "
                            f"vacancies.currency, vacancies.vacancies_url "
                            f"FROM companies "
                            f"JOIN vacancies USING (company_id)")

                data = cur.fetchall()
            conn.commit()
        return data

    def get_avg_salary(self):
        with self.conn_data as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT AVG(salary_to) as avg_payment FROM vacancies")
                data = cur.fetchall()
            conn.commit()
        return data

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        with self.conn_data as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT vacancies.vacancies_name, "
                            f"vacancies.salary_from, vacancies.salary_to, "
                            f"vacancies.currency, vacancies.vacancies_url FROM vacancies "
                            f"WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)")
                data = cur.fetchall()
            conn.commit()
        return data


    def get_vacancies_with_keyword(self, word):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        """
        with self.conn_data as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT companies.company_name, vacancies.vacancies_name, "
                            f"vacancies.salary_from, vacancies.salary_to, "
                            f"vacancies.currency, vacancies.vacancies_url "
                            f"FROM companies "
                            f"JOIN vacancies USING (company_id) "
                            f"WHERE lower(vacancies_name) LIKE '%{word}%' "
                            f"OR lower(vacancies_name) LIKE '%{word}'"
                            f"OR lower(vacancies_name) LIKE '{word}%'")
                data = cur.fetchall()
            conn.commit()
        return data