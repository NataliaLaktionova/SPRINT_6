from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData
import allure

class OrderPage(BasePage):
    @allure.step('Заполнение формы "Для кого самокат"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.Field_Name)
        self.click_on_element(OrderPageLocators.Field_Name)
        self.send_keys_to_input(OrderPageLocators.Field_Name, test_data[0])
        self.click_on_element(OrderPageLocators.Field_Last_Name)
        self.send_keys_to_input(OrderPageLocators.Field_Last_Name, test_data[1])
        self.click_on_element(OrderPageLocators.Field_Address)
        self.send_keys_to_input(OrderPageLocators.Field_Address, test_data[2])
        self.click_on_element(OrderPageLocators.Field_Metro_station)
        self.send_keys_to_input(OrderPageLocators.Field_Metro_station, test_data[3])
        self.click_on_element(OrderPageLocators.Dropdown_list_Metro_station)
        self.click_on_element(OrderPageLocators.Field_Phone_number)
        self.send_keys_to_input(OrderPageLocators.Field_Phone_number, test_data[4])
        self.click_on_element(OrderPageLocators.Button_Next)

    @allure.step('Клик по дропдауну станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.Field_Metro_station)

    @allure.step('Ввод даты заказа в филд "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.Field_Scooter_delivery_date).send_keys(TestData.TEST_Person1[5])

    @allure.step('Клик по выбранной дате в выпадающем календаре')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.Dropdown_calendar)

    @allure.step('Проверить отображение всплывающего окна "Заказ оформлен" после оформления заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.Section_Order_placed)

    @allure.step('Заполнение формы "Про Аренду" и шаги с всплывающим окном подтверждения оформления заказа')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.Field_Scooter_delivery_date)
        self.click_on_element(OrderPageLocators.Field_Scooter_delivery_date)
        self.send_keys_to_input(OrderPageLocators.Field_Scooter_delivery_date, test_data[5])
        self.click_on_element(OrderPageLocators.Checkbox_gray)
        self.click_on_element(OrderPageLocators.Field_Rental_period)
        self.click_on_element(OrderPageLocators.Dropdown_list_rental_period)
        self.click_on_element(OrderPageLocators.Field_Comment)
        self.send_keys_to_input(OrderPageLocators.Field_Comment, test_data[6])
        self.click_on_element(OrderPageLocators.Button_Order)
        self.wait_visibility_of_element(OrderPageLocators.Button_Yes)
        self.click_on_element(OrderPageLocators.Button_Yes)