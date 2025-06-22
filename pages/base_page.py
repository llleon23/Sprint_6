import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import curl


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик')
    def click_on(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст в поле')
    def send_keys_text(self, locator, texts):
        self.driver.find_element(*locator).send_keys(texts)

    @allure.step("Прогрузка элемента")
    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Получить текст")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Отображение элемента")
    def display_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Ожидание открытия Дзен")
    def wait_visibility_site_dzen(self):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(curl.dzen_site))

    @allure.step("Ожидание открытия главной страницы")
    def wait_visibility_main_page(self):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(curl.main_site))

    @allure.step("Перейти на вкладку")
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
