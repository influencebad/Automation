from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.mainpageform import MainPageForm
import allure


@allure.title("Заполнить форму")
@allure.description("Заполнить форму, нажать подтвердить и проверить, что система указывает цветом, если обязательное поле не заполнено")
@allure.feature("Fill form")
@allure.severity("blocker")
def test_form(browser: WebDriver):

    main_page = MainPageForm(browser)

    with allure.step("Заполнить поле first-name"):
        main_page.find_element("first-name", "Иван")
    with allure.step("Заполнить поле last-name"):
        main_page.find_element("last-name", "Петров")
    with allure.step("Заполнить поле e-mail"):
        main_page.find_element("address", "Ленина, 55-3")
    with allure.step("Заполнить поле address"):
        main_page.find_element("e-mail", "test@skypro.com")
    with allure.step("Заполнить поле phone"):
        main_page.find_element("phone", "+7985899998787")
    with allure.step("Заполнить поле city"):
        main_page.find_element("city", "Москва")
    with allure.step("Заполнить поле country"):
        main_page.find_element("country", "Россия")
    with allure.step("Заполнить поле job-position"):
        main_page.find_element("job-position", "QA")
    with allure.step("Заполнить поле company"):
        main_page.find_element("company", "SkyPro")

    with allure.step("Нажать кнопку подтвердить"):
        main_page.submit()

    with allure.step("Сравнить результат по полю first-name"):
        assert "success" in main_page.check("first-name")
    with allure.step("Сравнить результат по полю last-name"):
        assert "success" in main_page.check("last-name")
    with allure.step("Сравнить результат по полю address"):
        assert "success" in main_page.check("address")
    with allure.step("Сравнить результат по полю e-mail"):
        assert "success" in main_page.check("e-mail")
    with allure.step("Сравнить результат по полю phone"):
        assert "success" in main_page.check("phone")
    with allure.step("Сравнить результат по полю city"):
        assert "success" in main_page.check("city")
    with allure.step("Сравнить результат по полю country"):
        assert "success" in main_page.check("country")
    with allure.step("Сравнить результат по полю job-position"):
        assert "success" in main_page.check("job-position")
    with allure.step("Сравнить результат по полю company"):
        assert "success" in main_page.check("company")
    with allure.step("Сравнить результат по полю zip-code"):
        assert "danger" in main_page.check("zip-code")
