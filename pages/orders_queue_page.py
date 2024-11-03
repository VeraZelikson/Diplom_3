import allure

from pages.base_page import BasePage
from locators.orders_queue_locators import OrderListLocators
from locators.profile_locators import ProfilePageLocators


class OrderList(BasePage):
    @allure.step('Клик по заказу в списке заказов')
    def click_order(self):
        self.click_element(OrderListLocators.ORDER)

    @allure.step('Клик по кнопке "Восстановить пароль')
    def click_password_recovery_button(self):
        self.move_to_element_and_click()

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_counter(self):
        return self.get_element_text(OrderListLocators.TODAY_ORDERS)

    @allure.step('Получитьтекст номер заказа')
    def get_order_number_text(self):
        return self.get_element_text(ProfilePageLocators.ORDER_NUMBER)

    @allure.step('Получить количество заказов за все время')
    def get_all_orders_counter(self):
        return self.get_element_text(OrderListLocators.ALL_TIME_ORDERS)

    @allure.step('Получить текст окна состава')
    def get_from_consist_text(self):
        return self.get_element_text(OrderListLocators.CONSIST_TEXT)

    @allure.step('Найти элемент по номеру заказа')
    def search_element_by_order_number(self, num_order):
        str_num_order = OrderListLocators.ORDERS_LIST
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.find_element(str_num_order)

    @allure.step('Получить номер заказа в работе')
    def get_current_order_number(self):
        return self.get_element_text(OrderListLocators.CURRENT_ORDERS)