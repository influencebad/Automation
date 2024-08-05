from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.mainpageform import MainPageForm


def test_form(browser: WebDriver):

    main_page = MainPageForm(browser)
    main_page.find_element("first-name", "Иван")
    main_page.find_element("last-name", "Петров")
    main_page.find_element("address", "Ленина, 55-3")
    main_page.find_element("e-mail", "test@skypro.com")
    main_page.find_element("phone", "+7985899998787")
    main_page.find_element("city", "Москва")
    main_page.find_element("country", "Россия")
    main_page.find_element("job-position", "QA")
    main_page.find_element("company", "SkyPro")

    main_page.submit()

    assert "success" in main_page.check("first-name")
    assert "success" in main_page.check("last-name")
    assert "success" in main_page.check("address")
    assert "success" in main_page.check("e-mail")
    assert "success" in main_page.check("phone")
    assert "success" in main_page.check("city")
    assert "success" in main_page.check("country")
    assert "success" in main_page.check("job-position")
    assert "success" in main_page.check("company")
    assert "danger" in main_page.check("zip-code")
