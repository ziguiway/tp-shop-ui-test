import pytest
from selenium.webdriver.common.by import By

import utils
from config import BASE_URL, BASE_PATH
from page.buyer.home_page import HomePage
from page.buyer.login_page import LoginPage


class TestGoodsSearch(object):

    def setup_method(self):
        self.login_page = LoginPage()
        self.home_page = HomePage()
        self.driver = utils.DriverUtils.get_driver("buyer")
        # 尝试打开网页
        self.driver.get(BASE_URL)  # 替换为你要打开的网页

    def teardown_method(self):
        utils.DriverUtils.quit_driver("buyer")

    @pytest.mark.parametrize("goods_name", [("iphone",), ("小米",)])
    def test_goods_search(self, goods_name):
        self.home_page.goto_login_page()
        self.login_page.buyer_login("15716216311", "123456", "8888")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/a[2]").click()
        self.home_page.goods_search(goods_name)
        try:
            assert utils.is_el_exist_by_text("buyer", "搜索结果") is True
            assert utils.is_el_exist_by_text("buyer", *goods_name) is True
        except AssertionError as e:
            utils.DriverUtils.get_driver("buyer").save_screenshot(
                BASE_PATH + f"/screenshots/buyer/test_goods_search{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            raise e
