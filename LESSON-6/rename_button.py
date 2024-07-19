from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )


driver.implicitly_wait(20)


# Открыть страницу
driver.get("http://uitestingplayground.com/textinput")


# В поле ввода ввести название
input_name = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
new_name = input_name.send_keys("SkyPro")


# Нажать на кнопку для переименования
click_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text


# Вывести новое название кнопки
print(new_button)


driver.quit()
