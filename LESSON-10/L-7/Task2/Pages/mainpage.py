from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorSlow:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def clean_waits(self, element):
        """
            Эта функция находит поле ввода времени ожидания и очищает это поле
        """
        self.driver.find_element(By.CSS_SELECTOR, element).clear()

    def waits(self, element, value):
        """
            Эта функция находит поле ввода времени ожидания и заполняет необходимым значением
        """
        self.driver.find_element(By.CSS_SELECTOR, element).send_keys(value)

    def press_button(self, element):
        """
            Эта функция находит заданную кнопку калькулятора и нажимает ее
        """
        self.driver.find_element(By.XPATH, element).click()

    def waiting_element(self, driver, time, element, value):
        """
            Эта функция устанавливает необходимое время ожидания,
            которое должно быть больше, чем величина значения,
            указанная в функции, которая находит поле ввода времени ожидания и заполняет необходимым значением
        """
        wait = WebDriverWait(driver, time)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, element), value))

    def check_result(self, element, value):
        """
            Функция сравнения верности рассчета
        """
        result = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert result == value
