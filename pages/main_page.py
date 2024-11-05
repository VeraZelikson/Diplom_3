import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.orders_queue_locators import OrderListLocators


class MainPage(BasePage):
    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Клик по ингридиенту')
    def click_ingredient_button(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверить наличие элемента')
    def check_ingredients_details_shown(self):
        return self.presence_element(MainPageLocators.INGREDIENT_DETAILS_TEXT).is_displayed()

    @allure.step('Дождаться исчезновения деталей заказа')
    def wait_for_order_details_disappear(self):
        self.wait_element_disappear(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Клик по кнопке закрытия')
    def click_close_popup_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Добавить ингридиент в констуктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.find_element(MainPageLocators.INGREDIENT),
                           self.find_element(MainPageLocators.BURGER_CONSTRUCTOR))

    @allure.step('Найти нормер заказа во всплывающем окне')
    def find_order_number(self):
        self.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Клик по кнопке "Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить текст окна ингридиентов')
    def get_ingredients_details_text(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Получить текст счетчика ингридиентов')
    def get_ingredient_counter_text(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Получить текст кнопки логин')
    def get_login_button_text(self):
        return self.get_element_text(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Получить текст листа заказов')
    def get_order_list_text(self):
        return self.get_element_text(OrderListLocators.ORDER_LIST_TEXT)

    @allure.step('Получить текст заказа')
    def get_order_text(self):
        return self.get_element_text(MainPageLocators.ORDER_TEXT)