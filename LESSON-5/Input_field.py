from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


chrome.get(" http://the-internet.herokuapp.com/inputs")
firefox.get(" http://the-internet.herokuapp.com/inputs")


input_field = chrome.find_element(By.CSS_SELECTOR, '[type="number"]')
input_field.send_keys('1000')
sleep(3)
input_field.clear()
sleep(3)
input_field.send_keys('999')


input_field = firefox.find_element(By.CSS_SELECTOR, '[type="number"]')
input_field.send_keys('1000')
input_field.clear()
sleep(3)
input_field.send_keys('999')


chrome.quit()
firefox.quit()
