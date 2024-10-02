from selenium.webdriver.common.by import By

from base.base_page import BasePageBuyer


class GoodsDetailsPage(BasePageBuyer):
    def __init__(self):
        super().__init__()
        self.loc_add_to_cart = (By.CSS_SELECTOR, "#join_cart > i")
        self.loc_frame = (By.CSS_SELECTOR, '[id*=layui-layer-iframe]')

    def add_to_cart(self):
        self.base_click(self.loc_add_to_cart)
        self.base_switch_to_frame(self.loc_frame)
