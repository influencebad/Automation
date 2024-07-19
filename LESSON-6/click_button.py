from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )


# Открыть страницу
driver.get("http://uitestingplayground.com/ajax")


# Нажать кнопку
click_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
# Ожидать 16 секунд до окончания поиска
driver.implicitly_wait(20)


# Считать текст с элеманта
find_element = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text


print(find_element)


driver.quit()
