from selenium.webdriver.common.by import By


class Catalog:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, element):
        """
            Найти товар и положить в корзину
        """

        self.driver.find_element(By.ID, element).click()
