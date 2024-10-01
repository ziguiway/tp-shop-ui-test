'''
后台主页
'''
from selenium.webdriver.common.by import By

from base.base_page import BasePageAdmin


class HomePage(BasePageAdmin):

    def __init__(self):
        super().__init__()
        self.loc_goods = (By.XPATH, "//div[3]/ul/li[4]")
        self.loc_goods_list = (By.XPATH, "//*[@id='admincpNavTabs_goods']/dl[1]/dd/ul/li[1]/a")


    def goto_goods_page(self):
        self.base_click(self.loc_goods)

    def goto_goods_list_page(self):
        self.base_click(self.loc_goods_list)

