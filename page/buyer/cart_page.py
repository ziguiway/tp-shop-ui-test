from selenium.webdriver.common.by import By

from base.base_page import BasePageBuyer


class CartPage(BasePageBuyer):

    def __init__(self):
        super(CartPage, self).__init__()
        self.loc_paytotal_btn = (By.ID, "paytotal")

    def paytotal(self):
        self.base_click(self.loc_paytotal_btn)
