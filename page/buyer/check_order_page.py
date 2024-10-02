from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_page import BasePageBuyer


class CheckOrderPage(BasePageBuyer):
    def __init__(self):
        super().__init__()
        self.__loc_remarks = (By.CLASS_NAME, 'user_note_txt fl')
        self.__loc_invoice = (By.XPATH, '//*[@id="changeinfo"]/a')
        self.__loc_type_invoice_btn = (By.ID, 'type_invoice')
        self.__loc_submit_invoice_btn = (By.ID, 'type_invoice')
        self.__loc_submit_order_btn = (By.ID, 'submit_order')
        self.__loc_consignee = (By.XPATH, '//*[@id="address_form"]/div[2]/div/div[2]/div[1]/div/input')
        self.__loc_phone = (By.XPATH, '//*[@id="address_form"]/div[2]/div/div[2]/div[2]/div/input')
        # 地址分类
        self.__loc_address_province = (By.ID, 'province')
        self.__loc_address_city = (By.ID, 'city')
        self.__loc_address_district = (By.ID, 'district')
        self.__loc_address_street = (By.ID, 'twon')

        self.__loc_detail_address = (By.XPATH, "//*[@id='address_form']/div[2]/div/div[2]/div[4]/div/input")
        self.__loc_address_submit = (By.ID, "address_submit")

    def add_shipping_address(self, consignee, phone, province, city, district, street, detail_address):
        self.base_input(self.__loc_consignee, consignee)
        self.base_input(self.__loc_phone, phone)
        Select(self.base_find_element(self.__loc_address_province)).select_by_visible_text(province)
        Select(self.base_find_element(self.__loc_address_city)).select_by_visible_text(city)
        Select(self.base_find_element(self.__loc_address_district)).select_by_visible_text(district)
        Select(self.base_find_element(self.__loc_address_street)).select_by_visible_text(street)
        self.base_input(self.__loc_detail_address, detail_address)
        self.base_click(self.__loc_address_submit)

    def input_remarks(self, remarks):
        self.base_input(self.__loc_remarks, remarks)

    # def change_invoice_btn(self):
    #     self.base_click(self.loc_invoice)
    #
    # def type_invoice_btn(self):
    #     self.base_click(self.loc_type_invoice_btn)
    #
    # def submit_invoice(self):
    #     self.base_click(self.loc_submit_invoice_btn)

    def set_invoice(self):
        self.base_click(self.__loc_invoice)
        self.base_click(self.__loc_type_invoice_btn)
        self.base_click(self.__loc_submit_invoice_btn)

    def submit_order(self):
        self.base_click(self.__loc_submit_order_btn)
