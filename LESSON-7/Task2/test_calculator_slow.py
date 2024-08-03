from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.mainpage import CalculatorSlow


def test_slow_calculator(browser: WebDriver):

    mainpage = CalculatorSlow(browser)
    mainpage.clean_waits("#delay")
    mainpage.waits("#delay", "45")
    mainpage.press_button("//span[text() = '7']")
    mainpage.press_button("//span[text() = '+']")
    mainpage.press_button("//span[text() = '8']")
    mainpage.press_button("//span[text() = '=']")
    mainpage.waiting_element(browser, 55, 'div.screen', '15')
    mainpage.check_result('div.screen', '15')
