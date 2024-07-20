from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_calculator():
     # В поле ввода calculator waits ввести значение
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    # Нажать на кнопки калькулятора
    driver.find_element(By.XPATH, "//span[text() = '7']").click()
    driver.find_element(By.XPATH, "//span[text() = '+']").click()
    driver.find_element(By.XPATH, "//span[text() = '8']").click()
    driver.find_element(By.XPATH, "//span[text() = '=']").click()

    # Ждать появления результата через 45 секунд
    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), "15"))

    # Проверить верность рассчета
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert result == "15"

    driver.quit()
