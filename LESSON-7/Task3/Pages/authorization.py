from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(" https://www.saucedemo.com/")

# Вессти логин
    def username(self, element, value):
        self.driver.find_element(By.ID, element).send_keys(value)

# Ввести пароль
    def password(self, element, value):
        self.driver.find_element(By.ID, element).send_keys(value)

# Подтвердить
    def login(self):
        self.driver.find_element(By.ID, 'login-button').click()
