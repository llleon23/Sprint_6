
import allure
from data import TestData
from locators.locators_order_page import LocatorsOrder
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнение заказа в окне №1")
    def first_part_order(self):
        self.wait_visibility_element(LocatorsOrder.name)
        self.send_keys_text(LocatorsOrder.name, TestData.user_name)
        self.send_keys_text(LocatorsOrder.surname, TestData.user_surname)
        self.send_keys_text(LocatorsOrder.address, TestData.user_address)
        self.click_on(LocatorsOrder.metro)
        self.click_on(LocatorsOrder.metro_choose)
        self.send_keys_text(LocatorsOrder.telephone, TestData.user_telephone)
        self.scroll_to_element(LocatorsOrder.next_button)
        self.wait_visibility_element(LocatorsOrder.next_button)
        self.click_on(LocatorsOrder.next_button)

    @allure.step("Продолжение заполнение заказа в окне №2")
    def second_part_order(self):
        self.click_on(LocatorsOrder.where_bring_scooter)
        self.click_on(LocatorsOrder.calendar)
        self.click_on(LocatorsOrder.rental_period)
        self.click_on(LocatorsOrder.day_rental_period)
        self.click_on(LocatorsOrder.checkbox_black)
        self.send_keys_text(LocatorsOrder.comment, TestData.user_comment)
        self.click_on(LocatorsOrder.button_order_order)
        self.wait_visibility_element(LocatorsOrder.button_yes)
        self.click_on(LocatorsOrder.button_yes)
        self.wait_visibility_element(LocatorsOrder.button_check_status)

    @allure.step("Отображение кнопки 'Посмотреть статус'")
    def check_button_check_status(self):
        return self.display_element(LocatorsOrder.button_check_status)
