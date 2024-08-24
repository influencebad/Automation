from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.authorization import Authorization
from Pages.mainpagestore import Catalog
from Pages.cart import Cart
import allure


@allure.title("Покупка товаров в магазине")
@allure.description("Добавить товары в корзину и проверить, что конечная сумма посчитана правильно")
@allure.feature("add to cart")
@allure.severity("blocker")
def test_shopping(browser: WebDriver):

    authorization = Authorization(browser)
    with allure.step("Заполнить поле username"):
        authorization.username('user-name', "standard_user")
    with allure.step("Заполнить поле username"):
        authorization.password('password', "secret_sauce")
    with allure.step("Нажать кнопку Login"):
        authorization.login()

    with allure.step("Перейти в каталог товаров"):
        catalog = Catalog(browser)
    with allure.step("Добавть товары в корзину"):
        catalog.add_to_cart('add-to-cart-sauce-labs-backpack')
        catalog.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
        catalog.add_to_cart('add-to-cart-sauce-labs-onesie')

    with allure.step("Перейти в корзину"):
        cart = Cart(browser)
    with allure.step("Нажать кнопку checkout"):
        cart.click_checkout()
    with allure.step("Заполнить поле first-name"):
        cart.input_infirmation('first-name', "Александра")
    with allure.step("Заполнить поле last-name"):
        cart.input_infirmation('last-name', "Сулейманова")
    with allure.step("Заполнить поле postal-code"):
        cart.input_infirmation('postal-code', "352800")
    with allure.step("Заполнить поле postal-code"):
        cart.go_ahead()
    with allure.step("Найти сумму покупки"):
        cart.find_total()

    with allure.step("Сравнить сумму покупки с ожидаемым результатом"):
        assert '58.29' in cart.find_total()
