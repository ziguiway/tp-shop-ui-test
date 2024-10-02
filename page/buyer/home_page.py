'''
前台主页
'''
from selenium.webdriver.common.by import By

from base.base_page import BasePageBuyer


class HomePage(BasePageBuyer):

    def __init__(self):
        super().__init__()
        self.__loc_login_btn = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/a[1]")
        self.__loc_search_input = (By.ID, "q")
        self.__loc_search_btn = (By.CLASS_NAME, "ecsc-search-button")

    def goto_login_page(self):
        self.base_click(self.__loc_login_btn)

    def goods_search(self, goods_name):
        self.base_input(self.__loc_search_input, goods_name)
        self.base_click(self.__loc_search_btn)
