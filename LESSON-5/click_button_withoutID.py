from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


# Клик по кнопке без ID
# Перейти на страницу
chrome.get("http://uitestingplayground.com/dynamicid")
sleep(3)
firefox.get("http://uitestingplayground.com/dynamicid")


# Нажать на синюю кнопку
find_button = chrome.find_element(
        By.XPATH, "//button[text() = 'Button with Dynamic ID']").click()
find_button = firefox.find_element(
        By.XPATH, "//button[text() = 'Button with Dynamic ID']").click()
sleep(5)


# Повторить 3 раза
count = 0
for _ in range(3):
    find_button = chrome.find_element(
        By.XPATH, "//button[text() = 'Button with Dynamic ID']").click()
    find_button = firefox.find_element(
        By.XPATH, "//button[text() = 'Button with Dynamic ID']").click()
    count = int(count + 1)
    print(count)


chrome.quit()
firefox.quit()
