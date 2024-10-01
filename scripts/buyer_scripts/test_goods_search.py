import logging

from selenium.common import TimeoutException

import utils
from config import BASE_URL
from page.buyer.home_page import HomePage
from page.buyer.login_page import LoginPage


class TestGoodsSearch(object):
    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.driver = utils.DriverUtils.get_driver("buyer")
        try:
            # 设置加载超时为 5 秒
            cls.driver.set_page_load_timeout(5)
            # 尝试打开网页
            cls.driver.get(BASE_URL)  # 替换为你要打开的网页

        except TimeoutException:
            logging.warning("网页加载超时，停止加载。")
            cls.driver.execute_script("window.stop();")  # 停止加载

    @classmethod
    def teardown_class(cls):
        utils.DriverUtils.quit_driver("buyer")

    def test_goods_search(self):
        self.home_page.goto_login_page()
        self.login_page.buyer_login("15716216311", "123456", "8888")
        self.driver.back()
        self.home_page.goods_search("小米")
