import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.profile_locators import ProfilePageLocators
from locators.forgot_password_locators import PasswordRecoveryPageLocators


class ProfilePage(BasePage):
    @allure.step('Залогиниться в аккаунт')
    def login(self, data):
        self.send_data(ProfilePageLocators.EMAIL_INPUT, data['email'])
        self.send_data(ProfilePageLocators.PASSWORD_INPUT, data['password'])
        self.move_to_element_and_click(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет')
    def click_account_button(self):
        self.move_to_element_and_click(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_button(self):
        self.move_to_element_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Получить текст кнопки "Войти"')
    def get_login_button_text(self):
        return self.get_element_text(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.move_to_element_and_click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Получить текст кнопки "Востановление Пароля"')
    def get_password_recovery_button_text(self):
        return self.get_element_text(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)