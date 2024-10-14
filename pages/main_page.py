from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
import time

class MainPage(BasePage):
#Логотипы и методы для редиректа
    @allure.step('Ожидание загрузки логотипа "Яндекса"')
    def waiting_for_download_logotype_Yandex(self):
        self.wait_visibility_of_element(MainPageLocators.Logotype_YANDEX)

    @allure.step('Ожидание загрузки логотипа "Самокат"')
    def waiting_for_download_logotype_Scooter(self):
        self.wait_visibility_of_element(MainPageLocators.Logotype_SCOOTER)

    @allure.step('Клик по части логотипа "Яндекс"')
    def click_on_logotype_Yandex(self):
        self.click_on_element(MainPageLocators.Logotype_YANDEX)

    @allure.step('Клик по части логотипа "Самокат"')
    def click_on_logotype_scooter(self):
        self.click_on_element(MainPageLocators.Logotype_SCOOTER)

    @allure.step('Ожидание загрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.MAIN_HEADER)

    @allure.step('Проверка отображения заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.MAIN_HEADER)

    @allure.step('Получение URL после пройденного сценария')
    def get_URL(self):
        time.sleep(3)
        return self.driver.current_url

    @allure.step('Проверка совпадения URL с указанным после редиректа по логотипу')
    def check_current_url(self, expected_url):
        current_url = self.get_URL()
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

#методы для тестов "Вопросы о важном"
    @allure.step('Проскроллить до блока "Вопросы о важном"')
    def scrolling_to_FAQ_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_section)

    @allure.step('Ожидание загрузки номера вопроса в "Вопросы о важнoм"')
    def wait_visibility_question_of_FAQ_section(self, data):
        self.wait_visibility_of_element(MainPageLocators.FAQ_QUESTIONS[data])

    @allure.step('Клик на номер вопроса в "Вопросы о важнoм"')
    def click_on_question_in_FAQ_section(self, data):
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS[data])

    @allure.step('Ожидание загрузки нужного номера ответа в "Вопросы о важнoм"')
    def wait_visibility_answer_of_FAQ_section(self, data):
        self.wait_visibility_of_element(MainPageLocators.FAQ_ANSWERS[data])

    @allure.step('Отображение текста нужного номера ответа в "Вопросы о важнoм"')
    def get_display_text_from_answer_of_FAQ_section(self, data):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWERS[data])