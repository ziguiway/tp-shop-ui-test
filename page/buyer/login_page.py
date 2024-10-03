import logging

from selenium.webdriver.common.by import By

import utils
from base.base_page import BasePageBuyer
from common.driver_type import DriverType
from tools.captcha_solver import CaptchaSolver


class LoginPage(BasePageBuyer):

    def __init__(self):
        super().__init__()
        self.__loc_username = (By.NAME, 'username')
        self.__loc_password = (By.NAME, 'password')
        self.__loc_verify_code = (By.NAME, 'verify_code')
        self.__loc_login_btn = (By.NAME, 'sbtbutton')
        self.__loc_entering = (By.XPATH, "//*[@id=\"layui-layer5\"]/div[3]/a")

    def buyer_login(self, username, password, verify_code=None):

        while True:
            # 如果没有提供验证码，则获取并解决验证码
            if verify_code is None:
                img_url = (utils.DriverUtils.get_driver(DriverType.BUYER)
                           .find_element(By.XPATH, "//*[@id='verify_code_img']")
                           .get_attribute("src"))
                logging.info("获取验证码图片: %s", img_url)
                verify_code = CaptchaSolver.solve_captcha_from_url(img_url)
                logging.info("解决验证码: %s", verify_code)

            # 输入用户名、密码和验证码
            logging.info("输入用户名和密码")
            self.base_input(self.__loc_username, username)
            self.base_input(self.__loc_password, password)
            self.base_input(self.__loc_verify_code, verify_code)

            # 点击登录按钮
            logging.info("点击登录按钮")
            self.base_click(self.__loc_login_btn)

            # 检查是否登录成功
            if not utils.is_el_exist_by_text(DriverType.BUYER, "验证码错误", 1):
                logging.info("登录成功")
                break  # 登录成功，退出循环

            # 登录失败，重置验证码并继续尝试
            logging.warning("登录失败，验证码错误")
            verify_code = None
            self.base_click(self.__loc_entering)  # 可能需要点击某个元素来重试
