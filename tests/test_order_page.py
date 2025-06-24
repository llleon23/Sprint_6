import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Проверка оформления заказа через верхнюю кнопку")
    def test_order_top(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.wait_visibility_cookie_banner_close()
        main_page.wait_visibility_and_click_order_top()
        order_page.first_part_order()
        order_page.second_part_order()
        assert order_page.check_button_check_status()

    @allure.title("Проверка оформления заказа через нижнюю кнопку")
    def test_order_bottom(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.wait_visibility_cookie_banner_close()
        main_page.wait_visibility_scroll_to_questions_text()
        main_page.wait_visibility_and_click_to_order()
        order_page.first_part_order()
        order_page.second_part_order()
        assert order_page.check_button_check_status()
