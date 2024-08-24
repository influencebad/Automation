from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/cart.html')

    def click_checkout(self):
        """
            Функция находит и нажимает кнопку checkout в корзине с покупками
        """
        self.driver.find_element(By.ID, 'checkout').click()

    def input_infirmation(self, element, value):
        """
            Эта функция находит поле и заполняет информацию о покупателе
        """
        self.driver.find_element(By.ID, element).send_keys(value)

    def go_ahead(self):
        """
            Эта функция находит и нажимает кнопку Continue на карточке информации о покупателе
        """
        self.driver.find_element(By.ID, 'continue').click()

    def find_total(self):
        """
            Эта функция находит и получет сумму покупок добавленных в корзину
        """
        return self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text.replace('Total: $', '')

