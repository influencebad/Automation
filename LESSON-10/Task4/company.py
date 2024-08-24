import requests


class Company:

    def __init__(self, url) -> None:
        self.url = url

    def get_id_company(self):
        """
            Получить ID компании, последней в списке компаний
        """
        id_company = requests.get(self.url + '/company')
        return id_company.json()[-1]['id']