from ApiEmployee import ApiEmployee
from company import Company
from DbEmployee import DbEmployee
import allure

db = DbEmployee("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

company = Company("https://x-clients-be.onrender.com")

param_id = "?company=" + str(company.get_id_company())

company_id = company.get_id_company()

api = ApiEmployee("https://x-clients-be.onrender.com")

body = {
      "id": 1010108711,
      "firstName": "string",
      "lastName": "string",
      "middleName": "string",
      "companyId": company_id,
      "email": "string@bl.yu",
      "url": "string",
      "phone": "string",
      "birthdate": "2023-08-14T11:02:45.622Z",
      "isActive": "true"
  }


@allure.title("Получить список сотрудников")
@allure.description("Получить список сотрудников методом API и получить список сотрудников из БД, спавнить результат")
@allure.feature("Действия с работниками из БД и API")
@allure.severity("normal")
def test_get_list_employee2():
    with allure.step("Получить API список сотрудников"):
        api_result = api.get_list_employee2(param_id)
        api_result = api_result.json()
    with allure.step("Получить список сотрудников из БД"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Сравнить длину списка из API  и списка из БД"):
        assert len(api_result) == len(db_result)


@allure.title("Добавить нового сотрудника")
@allure.description("Получить список сотрудников из БД, добавить нового сотрудника, получить список сотрудников методом API и поситать что список из БД меньше списка API")
@allure.feature("Действия с работниками из БД и API")
@allure.severity("normal")
def test_add_employee2():
    with allure.step("Получить список сотрудников из БД"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Добавить нового сотрудника методом API"):
        api.add_new_employee2(body)
    with allure.step("Получить список сотрудников API"):
        api_response = api.get_list_employee2(param_id)
        api_response = api_response.json()
    with allure.step("Сравнить два списка"):
        assert len(api_response)-len(db_result) == 1


@allure.title("Получить id нового сотрудника")
@allure.description("Получить id последнего сотрудника методом API, получит id нового сотрудника из БД, сравнить, что они равны")
@allure.feature("Действия с работниками из БД и API")
@allure.severity("normal")
def test_get_new_employee2():
    with allure.step("Получить id нового сотрудника API"):
        resp = api.get_list_employee2(param_id)
        api_new_employee = resp.json()[-1]['id']
    with allure.step("Получить id нового сотрудника из БД"):
        db_new_employee = db.get_id_new_employee()
    with allure.step("Сравнить ID"):
        assert api_new_employee == db_new_employee


@allure.title("В БД создать нового сотрудника")
@allure.description("Добавить нового сотрудника по заданным параметрам в БД, затем получить данные о новом сотруднике методом API, сравнить, что значения соврадают, удалить нового сотрудника")
@allure.feature("Действия с работниками из БД и API")
@allure.severity("normal")
def test_create_employee():
    with allure.step("Добавить нового сотрудника в БД"):
        db.add_new_employee("Мария", "Уставшая", "0987654321", True, company_id)
    with allure.step("Получить нового сотрудника методом API"):
        data_employee = api.get_new_employee2(db.get_id_new_employee())
        data_employee = data_employee.json()
    with allure.step("Сравнить данные нового сотрудника полученные методом API с внесенными в БД"):
        assert data_employee["firstName"] == "Мария"
        assert data_employee["lastName"] == "Уставшая"
        assert data_employee["phone"] == "0987654321"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    with allure.step("Получить ID нового сотрудника"):
        id = db.get_id_new_employee()
    with allure.step("Удалить нового сотрудника"):
        db.delete(id)


@allure.title("В БД редактировать нового сотрудника")
@allure.description("Добавить нового сотрудника в БД, получить Id нового сотрудника, изменить данные нового сотрудника, удалить нового сотрудника")
@allure.feature("Действия с работниками из БД и API")
@allure.severity("normal")
def test_edit_employee():
    with allure.step("Добавить нового сотрудника в БД"):
        db.add_new_employee("Мария", "Уставшая", "0987654321", True, company_id)
    with allure.step("Получить ID нового сотрудника"):
        id = db.get_id_new_employee()
    with allure.step("Заменить информацию о новом сотруднике новыми данными"):
        db.edit_employee("Вася", "Васин", "0987654321", True, company_id, id)
    with allure.step("Получить новые данные о сотруднике"):
        data_employee = api.get_new_employee2(id)
        data_employee = data_employee.json()
    with allure.step("Сравнить новые данные сотрудника полученные методом API с внесенными в БД"):
        assert data_employee["firstName"] == "Вася"
        assert data_employee["lastName"] == "Васин"
        assert data_employee["phone"] == "0987654321"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    with allure.step("Удалить нового сотрудника"):
        db.delete(id)
