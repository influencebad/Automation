from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )


# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


# Ждать появления надписи DONE
wait = WebDriverWait(driver, 35)
wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), "Done!")
)
 
# Получить список картинок 
imgs = driver.find_elements(By.CSS_SELECTOR, 'img')

# Вывести значение атрибута SRC у третьей картинки
img = imgs[3]

src = img.get_attribute("src")

print(src)


driver.quit()
