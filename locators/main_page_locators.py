from selenium.webdriver.common.by import By
class MainPageLocators:
    URL_app = 'https://qa-scooter.praktikum-services.ru/' #URL веб-приложения
    FAQ_section = By.XPATH, '//div[contains(@class, "Home_FAQ")]'     # Вопросы о важном
    FAQ_QUESTIONS = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }
    FAQ_ANSWERS = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }
    Logotype_SCOOTER = By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]'     # Логотип Самокат
    Logotype_YANDEX = By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]'     # Логотип Яндекс

    # Кнопки на главной странице
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
    ORDER_BUTTON_IN_HEADER = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    # Заголовок на главной странице
    MAIN_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header")]')
