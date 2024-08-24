from selenium.webdriver.common.by import By


class MainPageForm:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def find_element(self, element, velue):
        """
            Эта функция находит и заполняет поля формы, в функцию передаем element по которому ищем поле для заполнения
             и velue - значение, которое мы вводим в это поле
        """
        self.driver.find_element(By.NAME, element).send_keys(velue)

    def submit(self):
        """
            Эта функция находит и нажимае кнопку подтвердить
        """
        self.driver.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    def check(self, element):
        """
            Эта функция находит поле и сравнивает соответсвие цвета поля ожидаемому результату,
             в функцию передаем element по которому ищем поле
        """
        return self.driver.find_element(By.ID, element).get_attribute("class")
