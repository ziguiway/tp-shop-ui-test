from selenium.webdriver.common.by import By

from base.base_page import BasePageBuyer


class GoodsListPage(BasePageBuyer):
    def __init__(self):
        super().__init__()
        self.loc_goods_detail = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[1]/a")
        self.loc_cart_btn = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]")

    def join_cart(self):
        self.base_click(self.loc_cart_btn)

    def goto_goods_detail_page(self):
        self.base_click(self.loc_goods_detail)
