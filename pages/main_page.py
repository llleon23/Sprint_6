import allure

from locators.locators_in_main_page import LocatorsMain
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Прогрузка верхней кнопки 'Заказать' и клик по ней")
    def wait_visibility_and_click_order_top(self):
        self.wait_visibility_element(LocatorsMain.top_button_order)
        self.click_on(LocatorsMain.top_button_order)

    @allure.step("Прогрузка лого 'Яндекса' и клик по нему")
    def wait_visibility_and_click_yandex_logo(self):
        self.wait_visibility_element(LocatorsMain.yandex_logo)
        self.click_on(LocatorsMain.yandex_logo)

    @allure.step("Прогрузка лого 'Самоката' и клик по нему")
    def wait_visibility_and_click_scooter_logo(self):
        self.wait_visibility_element(LocatorsMain.scooter_logo)
        self.click_on(LocatorsMain.scooter_logo)

    @allure.step("Скролл до 8-ого вопроса")
    def wait_visibility_scroll_to_questions8(self, data):
        self.wait_visibility_element(LocatorsMain.scooter_logo)
        self.scroll_to_element(LocatorsMain.important_questions[data])

    @allure.step("Прогрузка с кликом по вопросу и получение текста")
    def wait_visibility_and_click_to_questions(self, data):
        self.wait_visibility_element(LocatorsMain.important_questions[data])
        self.click_on(LocatorsMain.important_questions[data])

    @allure.step("Прогрузка ответов")
    def wait_visibility_and_click_to_answers(self, data):
        self.wait_visibility_element(LocatorsMain.important_answers[data])

    @allure.step("Получить текст")
    def get_text_answers(self, data):
        return self.get_text(LocatorsMain.important_answers[data])

    @allure.step("Переключиться на другую вкладку")
    def switch_to_dzen(self):
        self.switch_to_window()
        self.wait_visibility_site_dzen()

    @allure.step("Прогрузка 'заказать' при нажатии")
    def wait_visibility_and_click_to_order(self):
        self.wait_visibility_element(LocatorsMain.bottom_button_order)
        self.click_on(LocatorsMain.bottom_button_order)

    @allure.step("Скролл до Курьер забирает самокат")
    def wait_visibility_scroll_to_questions_text(self):
        self.wait_visibility_element(LocatorsMain.scooter_logo)
        self.scroll_to_element(LocatorsMain.questions_text)

    @allure.step("Закрыть гребаный банер")
    def wait_visibility_cookie_banner_close(self):
        self.wait_visibility_element(LocatorsMain.cookie_banner_close)
        self.click_on(LocatorsMain.cookie_banner_close)
