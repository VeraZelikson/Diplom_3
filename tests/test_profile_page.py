import allure
from endpoints import Url
from pages.profile_page import ProfilePage
from conftest import driver, user


@allure.story('Тестирование личного кабинета')
class TestProfilePage:
    @allure.title('Проверка перехода в "Личный кабинет"')
    def test_profile_page_opening(self, driver):
        page = ProfilePage(driver)
        page.open_browser(Url.BASE_PAGE)
        page.click_account_button()
        page.wait_url_change(Url.LOGIN_PAGE)
        assert (page.get_url() == Url.LOGIN_PAGE and
                page.get_password_recovery_button_text() == 'Восстановить пароль')

    @allure.title('Проверка раздела "История заказов" в личном кабинете')
    def test_order_history_opening(self, driver, user):
        page = ProfilePage(driver)
        page.open_browser(Url.LOGIN_PAGE)
        page.login(user)
        page.wait_url_change(Url.BASE_PAGE)
        page.click_account_button()
        page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        page.click_order_history_button()
        assert page.get_url() == Url.ORDER_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, user):
        page = ProfilePage(driver)
        page.open_browser(Url.LOGIN_PAGE)
        page.login(user)
        page.wait_url_change(Url.BASE_PAGE)
        page.click_account_button()
        page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        page.click_logout_button()
        assert (page.get_login_button_text() == 'Войти'
                and page.get_url() == Url.LOGIN_PAGE)
