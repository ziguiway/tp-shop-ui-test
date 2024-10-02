import logging

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

import utils
from config import BASE_URL, BASE_PATH
from page.buyer.home_page import HomePage
from page.buyer.login_page import LoginPage
from tools.captcha_solver import CaptchaSolver


class TestLogin:
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

    @pytest.mark.parametrize("username, password", [("15716216311", "123456")])
    def test_login(self, username, password):
        self.home_page.goto_login_page()
        img_url = (utils.DriverUtils.get_driver("buyer").
                   find_element(By.XPATH, "//*[@id='verify_code_img']").get_attribute("src"))
        # print(img_url)
        verify_code = CaptchaSolver.solve_captcha_from_url(img_url)
        self.login_page.buyer_login(username, password, verify_code)

        try:
            assert utils.is_el_exist_by_text("buyer", "安全退出") is True
        except AssertionError as e:
            utils.DriverUtils.get_driver("buyer").save_screenshot(
                BASE_PATH + f"/screenshots/buyer/test_login{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            raise e
