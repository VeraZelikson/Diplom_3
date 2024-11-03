import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть браузер')
    def open_browser(self, url):
        return self.driver.get(url)

    @allure.step('Дождаться смены url')
    def wait_url_change(self, url, time=15):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    @allure.step('Получить текущий url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверить видимость элемента')
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).text

    @allure.step('Проверить наличиеие элемента')
    def presence_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    @allure.step('Ввести данные')
    def send_data(self, locator, data, time=15):
        WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(data)

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, element, target):
        return ac(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Дождаться скрытия элемента')
    def wait_element_disappear(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator, time=15):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Скроллить до элемента и кликнуть на него')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ac(self.driver)
        actions.move_to_element(element).click().perform()