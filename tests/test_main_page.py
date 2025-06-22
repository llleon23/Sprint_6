import allure
import pytest
from data import TestData
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Проверка отображения текста на главной странице при нажатии на вопрос")
    @pytest.mark.parametrize("question_number, answers_text", TestData.important_answers_text)
    def test_click_questions_and_get_answers(self, driver, question_number, answers_text):
        main_page = MainPage(driver)
        main_page.wait_visibility_scroll_to_questions8(question_number)
        main_page.wait_visibility_and_click_to_questions(question_number)
        main_page.wait_visibility_and_click_to_answers(question_number)
        assert main_page.get_text_answers(question_number) == answers_text
