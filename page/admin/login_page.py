from selenium.webdriver.common.by import By

from base.base_page import BasePageAdmin


class LoginPage(BasePageAdmin):
    def __init__(self):
        super().__init__()
        self.__loc_username = (By.NAME, 'username')
        self.__loc_password = (By.NAME, 'password')
        self.__loc_vertify_code = (By.NAME, 'vertify')
        self.__loc_login_button = (By.NAME, 'submit')

    def admin_login(self, username, password, vertify_code):
        self.base_input(self.__loc_username, username)
        self.base_input(self.__loc_password, password)
        self.base_input(self.__loc_vertify_code, vertify_code)
        self.base_click(self.__loc_login_button)
