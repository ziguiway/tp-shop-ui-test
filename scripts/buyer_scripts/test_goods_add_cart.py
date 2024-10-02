from selenium.webdriver.common.by import By

import utils
from config import BASE_URL, BASE_PATH
from page.buyer.goods_details_page import GoodsDetailsPage
from page.buyer.goods_list_page import GoodsListPage
from page.buyer.home_page import HomePage
from page.buyer.login_page import LoginPage


class TestGoodsAddCart:
    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.goods_details_page = GoodsDetailsPage()
        cls.goods_list_page = GoodsListPage()
        cls.driver = utils.DriverUtils.get_driver("buyer")
        cls.driver.get(BASE_URL)

    @classmethod
    def teardown_class(cls):
        utils.DriverUtils.quit_driver("buyer")

    def test_add_cart(self):
        self.home_page.goto_login_page()
        self.login_page.buyer_login("15716216311", "123456", "8888")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/a[2]").click()
        self.home_page.goods_search("iphone")
        self.goods_list_page.goto_goods_detail_page()
        self.goods_details_page.add_to_cart()
        try:
            assert utils.is_el_exist_by_text("buyer", "添加成功") is True
            text = utils.get_el_text("buyer", '//*[@id="addCartBox"]/div[1]//span')
            assert text in '添加成功'
        except AssertionError as e:
            utils.DriverUtils.get_driver("buyer").save_screenshot(
                BASE_PATH + f"/screenshots/buyer/test_add_cart_{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            raise e