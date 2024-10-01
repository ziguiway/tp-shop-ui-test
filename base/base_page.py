import logging

from selenium.webdriver.support.ui import WebDriverWait

import utils


class BasePage:
    def __init__(self, driver_type):
        self.driver = utils.DriverUtils.get_driver(driver_type)

    def base_find_element(self, loc):
        logging.info(f"正在查找元素:{loc}")
        return WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        logging.info(f"正在点击元素:{loc}")
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        logging.info(f"正在输入元素:{loc}, value:{value}")
        self.base_find_element(loc).send_keys(value)

    def base_get_attribute(self, loc, attribute_name):
        logging.info(f"正在获取元素:{loc}, attribute_name:{attribute_name}")
        return self.base_find_element(loc).get_attribute(attribute_name)

    def base_save_screenshot(self, path):
        logging.info(f"正在保存截图:{path}")
        self.driver.get_screenshot_as_file(path)

    def base_switch_to_frame(self, frame):
        logging.info(f"正在切换到frame:{frame}")
        self.driver.switch_to.frame(frame)

    def base_switch_to_default_frame(self):
        logging.info(f"正在切换到默认frame")
        self.driver.switch_to.default_content()


class BasePageBuyer(BasePage):
    def __init__(self):
        super().__init__("buyer")


class BasePageAdmin(BasePage):
    def __init__(self):
        super().__init__("admin")


class BasePageApp(BasePage):
    def __init__(self):
        super().__init__("app")  # 这里可以根据需要调整角色
