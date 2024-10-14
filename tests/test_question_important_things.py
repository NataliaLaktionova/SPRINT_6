from pages.main_page import MainPage
from conftest import driver
from data import TestData
import pytest
import allure

class Test_question_important_things:
    @allure.title('Тестирование выпадающего списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question_number, pending_answer', TestData.Pending_answers)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, pending_answer):
        main_page = MainPage(driver)
        main_page.scrolling_to_FAQ_section()
        main_page.wait_visibility_question_of_FAQ_section(question_number)
        main_page.click_on_question_in_FAQ_section(question_number)
        main_page.wait_visibility_answer_of_FAQ_section(question_number)
        assert main_page.get_display_text_from_answer_of_FAQ_section(question_number) == pending_answer