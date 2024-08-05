from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.mainpage import CalculatorSlow


def test_slow_calculator(browser: WebDriver):

    main_page = CalculatorSlow(browser)
    main_page.clean_waits("#delay")
    main_page.waits("#delay", "45")
    main_page.press_button("//span[text() = '7']")
    main_page.press_button("//span[text() = '+']")
    main_page.press_button("//span[text() = '8']")
    main_page.press_button("//span[text() = '=']")
    main_page.waiting_element(browser, 55, 'div.screen', '15')
    main_page.check_result('div.screen', '15')
