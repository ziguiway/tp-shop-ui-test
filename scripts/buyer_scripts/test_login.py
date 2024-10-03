import pytest

import utils
from common.driver_type import DriverType
from config import BASE_PATH, BASE_URL
from page.buyer.home_page import HomePage
from page.buyer.login_page import LoginPage


@pytest.mark.run(order=102)
class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage()
        cls.home_page = HomePage()
        cls.driver = utils.DriverUtils.get_driver(DriverType.BUYER)
        # try:
        #     # 设置加载超时为 5 秒
        #     cls.driver.set_page_load_timeout(5)
        #     # 尝试打开网页
        #     cls.driver.get(BASE_URL)  # 替换为你要打开的网页
        # except TimeoutException:
        #     logging.warning("网页加载超时，停止加载。")
        #     cls.driver.execute_script("window.stop();")  # 停止加载
        utils.load_page_with_timeout(DriverType.BUYER, url=BASE_URL, timeout=5)

    @classmethod
    def teardown_class(cls):
        utils.DriverUtils.quit_driver(DriverType.BUYER)

    @pytest.mark.parametrize("username, password", [("15716216311", "123456")])
    def test_login(self, username, password):
        self.home_page.goto_login_page()
        self.login_page.buyer_login(username, password)
        try:
            assert utils.is_el_exist_by_text(DriverType.BUYER, "安全退出") is True
        except AssertionError as e:
            utils.DriverUtils.get_driver(DriverType.BUYER).save_screenshot(
                BASE_PATH + f"/screenshots/buyer/test_login{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            raise e
