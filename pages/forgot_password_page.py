import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль')
    def click_password_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.click_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Ввести данные в поле "Email"')
    def enter_email(self, data):
        self.send_data(PasswordRecoveryPageLocators.EMAIL_INPUT, data)

    @allure.step('Получить текст заголовка "Востановление Пароля"')
    def get_password_recovery_title_text(self):
        return self.get_element_text(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_TITLE_TEXT)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Проверить активность поля "Пароль"')
    def check_password_field_active(self):
        return self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Получить текст кнопки "Восстановить"')
    def get_recovery_button_text(self):
        return self.get_element_text(PasswordRecoveryPageLocators.RECOVERY_BUTTON)