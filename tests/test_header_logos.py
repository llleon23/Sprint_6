import allure
import curl
from pages.main_page import MainPage


class TestHeaderLogos:
    @allure.title("Отображения сайта 'Дзен' при нажатии на лого 'Яндекс'")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_and_click_yandex_logo()
        main_page.switch_to_dzen()
        assert main_page.get_current_url() == curl.dzen_site

    @allure.title("Отображения сайта главной страницы при нажатии на лого 'Самокат'")
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_cookie_banner_close()
        main_page.wait_visibility_and_click_to_order()
        main_page.wait_visibility_and_click_scooter_logo()
        assert main_page.get_current_url() == curl.main_site
