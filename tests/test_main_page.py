import allure
from endpoints import Url
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from conftest import *


@allure.story('Тестирование базовой функциональности')
class TestMainFunctionality:
    @allure.title('Проверка перехода в "Констуктор"')
    def test_constructor_opening(self, driver):
        page = MainPage(driver)
        page.open_browser(Url.ORDER_LIST_PAGE)
        page.click_constructor_button()
        assert (page.get_url() == Url.BASE_PAGE and
                page.get_login_button_text() == 'Войти в аккаунт')

    @allure.title('Проверка перехода на страницу "Лента Заказов"')
    def test_order_list_opening(self, driver):
        page = MainPage(driver)
        page.open_browser(Url.BASE_PAGE)
        page.click_order_list_button()
        assert (page.get_url() == Url.ORDER_LIST_PAGE and
                page.get_order_list_text() == 'Лента заказов')

    @allure.title('Проверка всплывающего окна с инфо об ингридиенте')
    def test_ingredient_popup(self, driver):
        page = MainPage(driver)
        page.open_browser(Url.BASE_PAGE)
        page.click_ingredient_button()
        assert page.get_ingredients_details_text() == 'Детали ингредиента'

    @allure.title('Проверка возможности закрытия всплывающего окна с инфо об ингридиенте')
    def test_ingredient_popup_closing(self, driver):
        page = MainPage(driver)
        page.open_browser(Url.BASE_PAGE)
        page.click_ingredient_button()
        page.click_close_popup_button()
        page.wait_for_order_details_disappear()
        assert page.check_ingredients_details_shown() == False

    @allure.title('Проверка счетчика ингридиентов')
    def test_ingredient_counter(self, driver):
        page = MainPage(driver)
        page.open_browser(Url.BASE_PAGE)
        page.add_ingredient_to_constructor()
        assert page.get_ingredient_counter_text() == '2'

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_successful_order(self, driver, user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_browser(Url.LOGIN_PAGE)
        profile_page.login(user)
        main_page.wait_url_change(Url.BASE_PAGE)
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.find_order_number()
        assert main_page.get_order_text() == 'идентификатор заказа'
