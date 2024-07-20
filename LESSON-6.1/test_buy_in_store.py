from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Открыть страницу
driver.get(" https://www.saucedemo.com/")


def test_buy_in_store():
    # Авторизоваться
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()

    driver.implicitly_wait(10)

    # Положить товары в корзину
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Перейти в корзину
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()

    # Заполнить форму информации
    driver.find_element(By.ID, 'first-name').send_keys("Александра")
    driver.find_element(By.ID, 'last-name').send_keys("Сулейманова")
    driver.find_element(By.ID, 'postal-code').send_keys("352800")
    driver.find_element(By.ID, 'continue').click()

    # Найти сумму
    price_total = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    total = price_total.text.replace('Total: $', '')

    # Сравнить сумму из корзины с ожидаемым результатом
    assert total == '58.29'
    
    driver.quit()
