from selenium.webdriver.common.by import By


class Catalog:

    def __init__(self, driver):
        self.driver = driver

# Положить товары в корзину
    def add_to_cart(self, element):
        self.driver.find_element(By.ID, element).click()
