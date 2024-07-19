from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()



# Клик по кнопке с CSS классом
chrome.get("http://uitestingplayground.com/classattr")
sleep(3)
firefox.get("http://uitestingplayground.com/classattr")
sleep(3)


blue_button = chrome.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()
sleep(3)
blue_button = firefox.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
blue_button.click()
sleep(3)


chrome.switch_to.alert.accept()
sleep(3)
firefox.switch_to.alert.accept()
sleep(3)


count = 0


for _ in range(3):
    blue_button = chrome.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    chrome.switch_to.alert.accept()
    blue_button = firefox.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    firefox.switch_to.alert.accept()
    count = count + 1
    print(count)


chrome.quit()
firefox.quit()
