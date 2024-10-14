import allure
from conftest import driver
from pages.main_page import MainPage

class Test_Logotype_Redirect:
    @allure.title('Тестирование редиректа основной страницы сервиса при клике на логотип "Самокат" в хедэре')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.waiting_for_download_logotype_Scooter()
        main_page.click_on_logotype_scooter()
        main_page.wait_visibility_of_main_header()
        main_page.check_current_url('https://qa-scooter.praktikum-services.ru/')

    @allure.title('Тестирование редиректа страницы "Яндекс Дзен" в новом окне при клике на логотип "Яндекс" в хэдере')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.waiting_for_download_logotype_Yandex()
        main_page.click_on_logotype_Yandex()
        main_page.switch_to_next_tab()
        main_page.check_current_url('https://dzen.ru/?yredirect=true')