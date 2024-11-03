import allure
from endpoints import Url
from pages.forgot_password_page import PasswordRecoveryPage
from conftest import *


@allure.story('Тестирование восстановления пароля')
class TestsPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_password_recovery_opening(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open_browser(Url.LOGIN_PAGE)
        page.click_password_recovery_button()
        assert (page.get_url() == Url.FORGOT_PASSWORD_PAGE and
                page.get_recovery_button_text()) == 'Восстановить'

    @allure.title('Проверка восстановления пароля с существующим email')
    def test_password_recovery_with_email(self, driver, user):
        page = PasswordRecoveryPage(driver)
        page.open_browser(Url.FORGOT_PASSWORD_PAGE)
        page.enter_email(user['email'])
        page.click_recovery_button()
        page.wait_url_change(Url.RESET_PASSWORD_PAGE)
        assert (page.get_url() == Url.RESET_PASSWORD_PAGE and
                page.get_password_recovery_title_text() == 'Восстановление пароля')

    @allure.title('Проверка функции показать/скрыть пароль')
    def test_show_hide_password_button(self, driver, user):
        page = PasswordRecoveryPage(driver)
        page.open_browser(Url.FORGOT_PASSWORD_PAGE)
        page.enter_email(user['email'])
        page.click_recovery_button()
        page.click_show_hide_password_button()
        assert page.check_password_field_active()
