import requests


class Employee:

    def __init__(self, url) -> None:
        self.url = url

# Авторизация
    def auth(self, login="leonardo", password="leads"):
        body = {
          "username": login,
          "password": password
        }
        response = requests.post(self.url + '/auth/login', json=body)
        return response.json()["userToken"]

# Получить список сотрудников компании
    def get_list_employee(self, params=None):
        response = requests.get(self.url + '/employee' + params)
        return response

# Добавить нового сотрудника
    def add_new_employee(self, body):
        headers = {'x-client-token': self.auth()}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        return response

# Получить сотрудника по id
    def get_new_employee(self, id):
        response = requests.get(self.url + '/employee/' + str(id))
        return response

# Изменить данные о новом сотруднике
    def change_new_employee(self, id, new_body):
        headers = {'x-client-token': self.auth()}
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)
        return response
