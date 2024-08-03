from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorSlow:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Отчистить поле ввода времени ожидания
    def clean_waits(self, element):
        self.driver.find_element(By.CSS_SELECTOR, element).clear()

# В поле ввода calculator waits ввести значение
    def waits(self, element, value):
        self.driver.find_element(By.CSS_SELECTOR, element).send_keys(value)

# Нажать на кнопки калькулятора
    def press_button(self, element):
        self.driver.find_element(By.XPATH, element).click()

# Подождать выполнения условия
    def waiting_element(self, driver, time, element, value):
        wait = WebDriverWait(driver, time)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, element), value))
        
# Проверить верность рассчета
    def check_result(self, element, value):
        result = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert result == value
