from employee import Employee


employee = Employee("https://x-clients-be.onrender.com/")

body = {
      "id": 1010108711,
      "firstName": "string",
      "lastName": "string",
      "middleName": "string",
      "companyId": 460,
      "email": "string@bl.yu",
      "url": "string",
      "phone": "string",
      "birthdate": "2023-08-14T11:02:45.622Z",
      "isActive": "true"
  }


def test_get_list_employee():
    result = employee.get_list_employee('?company=460')
    assert result.status_code == 200


def test_add_employee():
    response = employee.get_list_employee('?company=460')
    resp1 = response.json()
    len_before = len(resp1)

    employee.add_new_employee(body)

    response = employee.get_list_employee('?company=460')
    resp2 = response.json()
    len_after = len(resp2)
    assert len_after-len_before == 1


def test_get_new_employee():
    resp = employee.get_list_employee('?company=460')
    new_employee = resp.json()[-1]['id']
    info = employee.get_new_employee(new_employee)
    assert info.status_code == 200


def test_change_new_employee():
    resp = employee.get_list_employee('?company=460')
    new_employee = resp.json()[-1]['id']
    new_body = {
        "lastName": "Васильев",
        "phone": "97654332",
        "isActive": True
    }
    response = employee.change_new_employee(new_employee, new_body)
    assert response.status_code == 200
    resp = employee.get_new_employee(new_employee)
    assert resp.json()['lastName'] == 'Васильев'
