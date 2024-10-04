import logging
import time

import pyautogui
import pyperclip
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import utils
from common.driver_type import DriverType
from config import LODE_PAGE_MAX_TIME


class BasePage:
    def __init__(self, driver_type):
        self.driver = utils.DriverUtils.get_driver(driver_type)

    def base_find_element(self, loc):
        logging.debug(f"正在查找元素:{loc}")
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        logging.debug(f"正在点击元素:{loc}")

        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        logging.debug(f"正在输入元素:{loc}, value:{value}")
        self.base_find_element(loc).send_keys(value)

    def base_get_attribute(self, loc, attribute_name):
        logging.debug(f"正在获取元素:{loc}, attribute_name:{attribute_name}")
        return self.base_find_element(loc).get_attribute(attribute_name)

    def base_save_screenshot(self, path):
        logging.debug(f"正在保存截图:{path}")
        self.driver.get_screenshot_as_file(path)

    def base_switch_to_frame(self, frame):
        logging.debug(f"正在切换到frame:{frame}")
        self.driver.switch_to.frame(self.base_find_element(frame))

    def base_switch_to_default_frame(self):
        logging.debug(f"正在切换到默认frame")
        self.driver.switch_to.default_content()

    def base_upload_file(self, loc, file_path):
        """
        使用 PyAutoGUI 实现文件上传。

        :param loc: 上传按钮的定位方式（如: (By.ID, 'upload-button')）
        :param file_path: 要上传的文件的完整路径
        """
        driver = self.driver
        # 等待上传按钮可见
        upload_button = WebDriverWait(driver, 10, 1).until(
            EC.element_to_be_clickable(loc)
        )

        # 创建 ActionChains 实例
        actions = ActionChains(driver)

        # 将鼠标移动到上传按钮上并点击
        actions.move_to_element(upload_button).click().perform()

        # 等待文件选择对话框弹出
        time.sleep(1)

        # 复制文件路径到剪贴板
        pyperclip.copy(file_path)
        # 粘贴文件路径
        pyautogui.hotkey('ctrl', 'v')  # 使用 Ctrl + V 粘贴
        pyautogui.press('enter')  # 确认选择
        # 等待文件上传
        # WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Upload complete')]"))  # 替换为实际完成提示
        # )
        # 等待上传完成
        time.sleep(5)

    def base_to_page_with_timeout(self, loc, url=None, timeout=LODE_PAGE_MAX_TIME):
        self.driver.set_page_load_timeout(timeout)
        try:
            if url is not None:
                self.driver.get(url)
            else:
                self.base_click(loc)
        except TimeoutException:
            logging.warning("网页加载超时，停止加载。")
            self.driver.execute_script("window.stop();")
            # print(f"页面 '{url}' 加载超时，停止加载。")
        finally:
            self.driver.set_page_load_timeout(LODE_PAGE_MAX_TIME)


class BasePageBuyer(BasePage):
    def __init__(self):
        super().__init__(DriverType.BUYER)


class BasePageAdmin(BasePage):
    def __init__(self):
        super().__init__(DriverType.ADMIN)


class BasePageApp(BasePage):
    def __init__(self):
        super().__init__(DriverType.APP)  # 这里可以根据需要调整角色
