from selenium.webdriver.common.by import By


class LocatorsMain:
    important_questions = {
        1: (By.XPATH, '//div[@id="accordion__heading-0"]'),
        2: (By.XPATH, '//div[@id="accordion__heading-1"]'),
        3: (By.XPATH, '//div[@id="accordion__heading-2"]'),
        4: (By.XPATH, '//div[@id="accordion__heading-3"]'),
        5: (By.XPATH, '//div[@id="accordion__heading-4"]'),
        6: (By.XPATH, '//div[@id="accordion__heading-5"]'),
        7: (By.XPATH, '//div[@id="accordion__heading-6"]'),
        8: (By.XPATH, '//div[@id="accordion__heading-7"]')
    }

    important_answers = {
        1: (By.XPATH, '//div[@id = "accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id = "accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id = "accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id = "accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id = "accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id = "accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id = "accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id = "accordion__panel-7"]')
    }

    top_button_order = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    bottom_button_order = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    scooter_logo = (By.XPATH, '//img[@src="/assets/scooter.svg"]')
    yandex_logo = (By.XPATH, '//img[@src="/assets/ya.svg"]')
    questions_text = (By.XPATH, '//div[text()= "Курьер забирает самокат"]')
    cookie_banner_close = (By.XPATH, '//button[text()= "да все привыкли"]')
