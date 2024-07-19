from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()


chrome.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)
firefox.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

modal_window = chrome.find_element(By.XPATH, "//p[text() = 'Close']").click()
sleep(5)
modal_window = firefox.find_element(By.XPATH, "//p[text() = 'Close']").click()
sleep(5)


chrome.quit()
firefox.quit()
