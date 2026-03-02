from selene import browser
from config import BASE_URL


class LoginPage:
    EMAIL_INPUT = '#email'
    PASSWORD_INPUT = '#password'
    SUBMIT_BUTTON = '[type="submit"]'
    RESET_PASSWORD_LINK = '#reset-password-link'
    SIGN_UP_LINK = '#sign-up-link'
    REMEMBER_ME = '[data-checked]'
    EMAIL_ERROR = '#email-error'
    PASSWORD_ERROR = '#password-error'

    def open(self):
        browser.open_url(f'{BASE_URL}/login')
        return self

    def fill_email(self, email):
        browser.element(self.EMAIL_INPUT).type(email)
        return self

    def fill_password(self, password):
        browser.element(self.PASSWORD_INPUT).type(password)
        return self

    def submit(self):
        browser.element(self.SUBMIT_BUTTON).click()
        return self

    def login_as(self, email, password):
        self.open()
        self.fill_email(email)
        self.fill_password(password)
        self.submit()
        return self