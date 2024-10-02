import allure
import pytest

import utils
from config import BASE_PATH
from page.admin.goods_page import GoodsPage
from page.admin.home_page import HomePage
from page.admin.login_page import LoginPage


@pytest.mark.run(order=3)
class TestGoods:

    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage()
        cls.goods_page = GoodsPage()
        cls.home_page = HomePage()
        # cls.driver = utils.DriverUtils.get_driver("admin")
        # cls.driver.get(BASE_URL + "/index.php/Admin/Admin/login")

    @classmethod
    def teardown_class(cls):
        utils.DriverUtils.quit_driver("admin")

    @pytest.mark.parametrize(
        "goods_name, goods_price, goods_market_price, goods_category_1, goods_category_2, goods_category_3, is_free_shipping",
        [(utils.TimeUtils.get_current_timestamp_int().__str__() + "test_goods_add", "100", "100", "12", "13", "187",
          "1")])
    def test_goods_add(self, goods_name, goods_price, goods_market_price, goods_category_1, goods_category_2,
                       goods_category_3, is_free_shipping):
        # self.login_page.admin_login("admin", "HM_2023_test", "8888")
        self.home_page.goto_goods_page()
        self.home_page.goto_goods_list_page()
        self.goods_page.goods_add(goods_name, goods_price, goods_market_price, goods_category_1, goods_category_2,
                                  goods_category_3, is_free_shipping)
        try:
            assert utils.is_el_exist_by_text("admin", "1727773109test_goods_add") is True
        except AssertionError as e:
            # utils.DriverUtils.get_driver("admin").save_screenshot(
            #     BASE_PATH + f"/screenshots/admin/test_goods_add_{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            allure.attach(
                utils.DriverUtils.get_driver("admin").get_screenshot_as_png(),
                f"{BASE_PATH}/screenshots/admin/test_goods_add.png"
                , allure.attachment_type.PNG
            )
            raise e
