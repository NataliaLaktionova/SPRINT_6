from selenium.webdriver.common.by import By
class OrderPageLocators:

#страница 'Для кого самокат?'
    Field_Name = By.XPATH, '//input[@placeholder="* Имя"]'
    Field_Last_Name = By.XPATH, '//input[@placeholder="* Фамилия"]'
    Field_Address = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    Field_Metro_station = By.XPATH, '//input[@placeholder="* Станция метро"]'
    Dropdown_list_Metro_station = By.XPATH, '//div[@class="select-search__select"]'
    Field_Phone_number = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    Button_Next = By.XPATH, '//div[contains(@class, "Order_NextButton")]/button'

#страница 'Про аренду'
    Field_Scooter_delivery_date = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    Dropdown_calendar = By.XPATH, '//div[@class="react-datepicker__month-container"]'
    Field_Rental_period = By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]'
    Dropdown_list_rental_period = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='двое суток']"
    Checkbox_black = By.XPATH, '//input[@id="black" and contains(@class, "Checkbox_Input__14A2w")]'
    Checkbox_gray = By.XPATH, '//input[@id="grey" and contains(@class, "Checkbox_Input__14A2w")]'
    Field_Comment = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    Button_Cancel = By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Назад"]'
    Button_Order = By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Заказать"]'

#всплывающее окно подтверждения закаа
    Button_Yes = By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Да"]'
    Section_Order_placed = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]'


