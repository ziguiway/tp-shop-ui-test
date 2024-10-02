from selenium.webdriver.common.by import By

from base.base_page import BasePageBuyer


class LoginPage(BasePageBuyer):

    def __init__(self):
        super().__init__()
        self.__loc_username = (By.NAME, 'username')
        self.__loc_password = (By.NAME, 'password')
        self.__loc_verify_code = (By.NAME, 'verify_code')
        self.__loc_login_btn = (By.NAME, 'sbtbutton')

    def buyer_login(self, username, password, verify_code):
        self.base_input(self.__loc_username, username)
        self.base_input(self.__loc_password, password)
        self.base_input(self.__loc_verify_code, verify_code)
        self.base_click(self.__loc_login_btn)
