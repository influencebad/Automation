from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.authorization import Authorization
from Pages.mainpagestore import Catalog
from Pages.cart import Cart


def test_shopping(browser: WebDriver):

    authorization = Authorization(browser)
    authorization.username('user-name', "standard_user")
    authorization.password('password', "secret_sauce")
    authorization.login()

    catalog = Catalog(browser)
    catalog.add_to_cart('add-to-cart-sauce-labs-backpack')
    catalog.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    catalog.add_to_cart('add-to-cart-sauce-labs-onesie')

    cart = Cart(browser)
    cart.click_checkout()
    cart.input_infirmation('first-name', "Александра")
    cart.input_infirmation('last-name', "Сулейманова")
    cart.input_infirmation('postal-code', "352800")
    cart.go_ahead()
    cart.find_total()

    assert '58.29' in cart.find_total()
