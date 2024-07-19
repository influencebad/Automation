from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Клик по кнопке
# Открыть страницу
chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(3)
firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")


# Нажать на кнопку 5 раз
for _ in range(5):
    add_button = chrome.find_element(
        By.CSS_SELECTOR, '[onclick="addElement()"]').click()
    add_button = firefox.find_element(
        By.CSS_SELECTOR, '[onclick="addElement()"]').click()
sleep(3)


# Список элементов
new_elements = chrome.find_elements(
    By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print("Длина списка Chrome " + str(len(new_elements)))
new_elements = firefox.find_elements(
    By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print("Длина списка Firefox " + str(len(new_elements)))


chrome.quit()
firefox.quit()
