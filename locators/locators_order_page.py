from selenium.webdriver.common.by import By


class LocatorsOrder:
    name = (By.XPATH, '//input[@placeholder="* Имя"]')
    surname = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    metro_choose = (By.XPATH, '//li[@class="select-search__row"]')
    telephone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//button[text()="Далее"]')


    #Про аренду
    where_bring_scooter = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    calendar = (By. XPATH, '//div[@aria-label="Choose четверг, 26-е июня 2025 г."]')
    rental_period = (By.XPATH, '//div[text()="* Срок аренды"]')
    day_rental_period = (By.XPATH, './/div[@class="Dropdown-menu"]/div[text()="сутки"]')
    checkbox_black = (By.XPATH, '//input[@class="Checkbox_Input__14A2w"]')
    comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    button_order_order = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g")/button[text()= "Заказать"]')

    #модальное окно
    button_yes = (By.XPATH, '//button[text()= "Да"]')


