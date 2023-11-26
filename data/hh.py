import json
import requests


class HeadHunterAPI:
    """
    Класc для работы с API_HH
    """

    def get_companies(self, companies: list) -> list:
        self.url = 'https://api.hh.ru/employers/'

        list_company = []

        for item in companies:
            self.params = {
                'text': item,
                'only_with_vacancies': True
            }
            self.response = requests.get(f'{self.url}', self.params).json()['items']
            for item_ in self.response:
                dict_company = {
                    "company_id": int(item_["id"]),
                    "company_name": item_["name"],
                    "url": item_["alternate_url"],
                    "open_vacancies": int(item_["open_vacancies"])
                }
                list_company.append(dict_company)

        return list_company

    def get_vacancies(self, company_id: int):

        self.url = f"https://api.hh.ru/vacancies?employer_id={company_id}"
        data_vacancies = requests.get(self.url).json()["items"]
        # print(data_vacancies)
        vacancies = []
        for item in data_vacancies:
            if item["salary"]:
                salary_from = int(item["salary"]["from"] if item["salary"]["from"] else 0)
                salary_to = int(item["salary"]["to"] if item["salary"]["to"] else 0)
                currency = item["salary"]["currency"] if item["salary"]["currency"] else "null"
            else:
                salary_to = 0
                salary_from = 0
                currency = "null"

            vacancy = {
                "company_id": company_id,
                "vacancy_id": int(item["id"]),
                "vacancies_name": item["name"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "currency": currency,
                "requirement": item["snippet"]["requirement"],
                "vacancy_url": item["alternate_url"]
            }

            vacancies.append(vacancy)

        return vacancies


# hh = HeadHunterAPI()
# companies = ['сбербанк']
# companies = list(map(str, input('Введите компании через пробел, которые Вам интересны ').split()))
# print(hh.get_companies(companies))
# print(type(hh.get_companies(companies)))
# print(hh.get_vacancies(1809605))
