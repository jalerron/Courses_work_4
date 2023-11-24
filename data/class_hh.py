import json
import requests


class HeadHunterAPI:
    """
    Класc для работы с API_HH
    """

    def get_companies(self, companies: list):
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
                    "company_id": item_["id"],
                    "name": item_["name"],
                    "url": item_["alternate_url"],
                    "open_vacancies": item_["open_vacancies"]
                }
                list_company.append(dict_company)
            json_companies = json.dumps(list_company, indent=4, ensure_ascii=False)

        return json_companies

    def get_vacancies(self, employer_id: int):

        self.url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        data_vacancies = requests.get(self.url).json()["items"]
        # print(data_vacancies)
        vacansies = []
        for item in data_vacancies:
            if item["salary"]:
                salary_from = item["salary"]["from"] if item["salary"]["from"] else 0
                salary_to = item["salary"]["to"] if item["salary"]["to"] else 0
                currency = item["salary"]["currency"] if item["salary"]["currency"] else "null"
            else:
                salary_to = 0
                salary_from = 0
                currency = "null"

            vacancy = {
                "emlpoyer_id": employer_id,
                "vacancy_id": item["id"],
                "name": item["name"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "currency": currency,
                "vacancy_url": item["alternate_url"]
            }

            vacansies.append(vacancy)
        json_vacancies = json.dumps(vacansies, indent=4, ensure_ascii=False)

        return json_vacancies


hh = HeadHunterAPI()
companies = ['yandex', 'сбербанк', 'Газпромбанк', 'Tinkoff']
# companies = list(map(str, input('Введите компании через пробел, которые Вам интересны ').split()))
print(hh.get_companies(companies))
# print(hh.get_vacancies(1809605))
