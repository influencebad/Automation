from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


chrome.get("http://the-internet.herokuapp.com/login")
firefox.get("http://the-internet.herokuapp.com/login")


input_username = chrome.find_element(By.CSS_SELECTOR, '#username')
input_username.send_keys("tomsmith")
input_password = chrome.find_element(By.CSS_SELECTOR, '#password')
input_password.send_keys("SuperSecretPassword!")
sleep(3)
log_in = chrome.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
sleep(3)


input_username = firefox.find_element(By.CSS_SELECTOR, '#username')
input_username.send_keys("tomsmith")
input_password = firefox.find_element(By.CSS_SELECTOR, '#password')
input_password.send_keys("SuperSecretPassword!")
sleep(3)
log_in = firefox.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
sleep(3)


chrome.quit()
firefox.quit()
