import json
import logging
import time
from datetime import datetime

import appium.webdriver
import selenium.webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.driver_type import DriverType
from config import BASE_PATH, LODE_PAGE_MAX_TIME


class DriverUtils:
    # 门户网站
    __buyer_driver = None
    __app_driver = None
    __admin_driver = None

    __buyer_key = True

    @classmethod
    def change_buyer_key(cls, key):
        cls.__buyer_key = key

    @classmethod
    def __get_buyer_driver(cls):
        if cls.__buyer_driver is None:
            cls.__buyer_driver = selenium.webdriver.Chrome()
            cls.__buyer_driver.maximize_window()
            cls.__buyer_driver.implicitly_wait(30)
        return cls.__buyer_driver

    @classmethod
    def __quit_buyer_driver(cls):
        if cls.__buyer_driver is not None and cls.__buyer_key:
            cls.__buyer_driver.quit()
            cls.__buyer_driver = None

    __app_key = True

    @classmethod
    def change_app_key(cls, key):
        cls.__app_key = key

    @classmethod
    def __get_APP_driver(cls):
        if cls.__app_driver is None and cls.__app_key:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '6.0.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # APP包名 com.tpshop.malls/.SPMainActivity
            desired_caps['appPackage'] = "com.tpshop.malls"
            # 启动名
            desired_caps['appActivity'] = ".SPMainActivity"
            # 设置中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    @classmethod
    def __quit_APP_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()

    __admin_key = True

    @classmethod
    def change_admin_key(cls, key):
        cls.__admin_key = key
        print(cls.__admin_key)

    @classmethod
    def __get_admin_driver(cls):
        if cls.__admin_driver is None:
            cls.__admin_driver = selenium.webdriver.Chrome()
            cls.__admin_driver.maximize_window()
            cls.__admin_driver.implicitly_wait(30)
        return cls.__admin_driver

    @classmethod
    def __quit_admin_driver(cls):
        if cls.__admin_driver is not None and cls.__admin_key:
            cls.__admin_driver.quit()
            cls.__admin_driver = None

    @classmethod
    def get_driver(cls, driver_type):
        if driver_type == DriverType.BUYER:
            return cls.__get_buyer_driver()
        elif driver_type == DriverType.APP:
            return cls.__get_APP_driver()
        elif driver_type == DriverType.ADMIN:
            return cls.__get_admin_driver()
        else:
            return None

    @classmethod
    def quit_driver(cls, driver_type):
        if driver_type == DriverType.BUYER:
            cls.__quit_buyer_driver()
        elif driver_type == DriverType.APP:
            cls.__quit_APP_driver()
        elif driver_type == DriverType.ADMIN:
            cls.__quit_admin_driver()
        else:
            logging.error(f"{driver_type} 参数错误")


def get_el_text(driver_type, xpath_str):
    try:
        msg = WebDriverWait(DriverUtils.get_driver(driver_type), 10, 0.5).until(
            lambda x: x.find_element(By.XPATH, xpath_str)).text
        logging.info(f"获取文本成功,内容:{msg}")
    except Exception as e:
        logging.error(f"获取文本失败,xpath:{xpath_str}")
        msg = None
    return msg


def is_el_exist_by_text(driver_type, key_text, timeout=10, poll_frequency=0.5):
    try:
        if driver_type == DriverType.APP:
            xpath_str = f"//*[@text='{key_text}']"
        else:
            xpath_str = f"//*[text()='{key_text}']"

        WebDriverWait(DriverUtils.get_driver(driver_type), timeout, poll_frequency=poll_frequency).until(
            EC.presence_of_element_located((By.XPATH, xpath_str))
        )
        return True  # 找到元素，返回 True
    except TimeoutException:
        logging.error(f"元素未找到，key_text: {key_text}，超时")
        return False  # 未找到元素，返回 False
    except Exception as e:
        logging.error(f"获取文本元素失败, key_text: {key_text}, 异常信息: {e}")
        return False  # 其他异常情况也返回 False


def build_data(file_name):
    case_data = []
    with open(BASE_PATH + f"/data/{file_name}.txt", 'r', encoding='utf-8') as f:
        all_data = json.load(f)
    for i in all_data.values():
        case_data.append(list(i.values()))
    return case_data


class TimeUtils:
    @staticmethod
    def get_current_timestamp():
        """获取当前时间的时间戳（浮点数）"""
        return time.time()

    @staticmethod
    def get_current_timestamp_int():
        """获取当前时间的时间戳（整数）"""
        return int(time.time())

    @staticmethod
    def format_timestamp(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
        """将时间戳格式化为指定格式的时间字符串"""
        return datetime.fromtimestamp(timestamp).strftime(format_str)

    @staticmethod
    def parse_time_string(time_str, format_str="%Y-%m-%d %H:%M:%S"):
        """将时间字符串解析为时间对象"""
        return datetime.strptime(time_str, format_str)

    @staticmethod
    def get_time_difference(start_time, end_time):
        """计算两个时间之间的差值（秒）"""
        return (end_time - start_time).total_seconds()


def load_page_with_timeout(driver_type, loc=None, url=None, timeout=LODE_PAGE_MAX_TIME):
    driver = DriverUtils.get_driver(driver_type)
    driver.set_page_load_timeout(timeout)
    try:
        if url is not None:
            driver.get(url)
        else:
            driver.find_element(*loc).click()
    except TimeoutException:
        logging.warning("网页加载超时，停止加载。")
        driver.execute_script("window.stop();")
    finally:
        driver.set_page_load_timeout(LODE_PAGE_MAX_TIME)
