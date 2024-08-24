from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(" https://www.saucedemo.com/")

    def username(self, element, value):
        """
            Найти поле Username и заполнить значением
        """
        self.driver.find_element(By.ID, element).send_keys(value)

    def password(self, element, value):
        """
            Найти поле Password и заполнить значением
        """
        self.driver.find_element(By.ID, element).send_keys(value)

# Подтвердить
    def login(self):
        """
            Найти кнопку Login и нажать
        """
        self.driver.find_element(By.ID, 'login-button').click()
