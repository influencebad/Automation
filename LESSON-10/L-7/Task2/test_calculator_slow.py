from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.mainpage import CalculatorSlow
import allure


@allure.title("Медленный калькулятор")
@allure.description("Задать время работы калькулятора, посчитать сумму и сверить что результат соответствует ожидаемому")
@allure.feature("Calculator")
@allure.severity("blocker")
def test_slow_calculator(browser: WebDriver):

    main_page = CalculatorSlow(browser)
    with allure.step("Отчистить поле установленного ожидания"):
        main_page.clean_waits("#delay")
    with allure.step("Заполнить поле установленного ожидания"):
        main_page.waits("#delay", "45")
    with allure.step("Нажать кнопки калькулятора"):
        main_page.press_button("//span[text() = '7']")
        main_page.press_button("//span[text() = '+']")
        main_page.press_button("//span[text() = '8']")
        main_page.press_button("//span[text() = '=']")
    with allure.step("Ожидаем время установленное в поле установленного ожидания"):
        main_page.waiting_element(browser, 55, 'div.screen', '15')
    with allure.step("Проверяем результат"):
        main_page.check_result('div.screen', '15')
