import allure
import helpers
from endpoints import Url
from conftest import user, driver
from pages.orders_queue_page import OrderList
from pages.profile_page import ProfilePage
from pages.main_page import MainPage


@allure.story('Тестирование ленты заказов')
class TestOrderList:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_order_details_popup(self, driver):
        order_page = OrderList(driver)
        order_page.open_browser(Url.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_page.click_order()
        assert order_page.get_from_consist_text() == 'Cостав'

    @allure.title('Проверка наличия созданных заказов в истории и ленте заказов')
    def test_created_orders_in_list(self, driver, user):
        order_page = OrderList(driver)
        order_page.open_browser(Url.LOGIN_PAGE)
        response = helpers.create_order(user)
        order_number = response.json()['order']['number']
        profile_page = ProfilePage(driver)
        profile_page.login(user)
        profile_page.wait_url_change(Url.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_order_list_button()
        order_page.search_element_by_order_number(order_number)
        profile_page.click_account_button()
        profile_page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        profile_page.click_order_history_button()
        assert str(order_number) in order_page.get_order_number_text()

    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_done_counter_for_today_orders(self, driver, user):
        page = OrderList(driver)
        page.open_browser(Url.ORDER_LIST_PAGE)
        old_number = page.get_today_orders_counter()
        helpers.create_order(user)
        assert int(page.get_today_orders_counter()) >= int(old_number) + 1

    @allure.title('Проверка счетчика "Выполнено за все время"')
    def test_done_counter_for_all_time_orders(self, driver, user):
        page = OrderList(driver)
        page.open_browser(Url.ORDER_LIST_PAGE)
        old_number = page.get_all_orders_counter()
        helpers.create_order(user)
        assert int(page.get_all_orders_counter()) >= int(old_number) + 1

    @allure.title('Проверка заказов "В работе"')
    def test_orders_in_work(self, driver, user):
        page = OrderList(driver)
        page.open_browser(Url.ORDER_LIST_PAGE)
        response = helpers.create_order(user)
        order_number = response.json()['order']['number']
        assert str(order_number) >= page.get_current_order_number()
