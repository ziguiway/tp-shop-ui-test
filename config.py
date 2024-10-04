import os
import time

BASE_PATH = os.path.dirname(__file__)

BASE_URL = "http://hmshop-test.itheima.net/"

LODE_PAGE_MAX_TIME = 300

TIMESTAMP = int(time.time()).__str__()

GOODS_NAME = "GOODS_NAME" + TIMESTAMP


import logging
from logging.handlers import TimedRotatingFileHandler
from colorama import Fore, Style, init

# 初始化 colorama
init(autoreset=True)


def basic_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 文件处理器，用于记录日志到文件
    lht = TimedRotatingFileHandler(
        filename=f"{BASE_PATH}/log/tpshop_test.log",
        when="midnight",
        interval=1,
        encoding="utf-8",
        backupCount=2
    )

    # 控制台处理器，用于记录日志到控制台
    ls = logging.StreamHandler()

    # 自定义日志格式器，用于控制台输出
    class ColoredFormatter(logging.Formatter):
        COLORS = {
            'DEBUG': Fore.WHITE,
            'INFO': Fore.GREEN,
            'WARNING': Fore.YELLOW,
            'ERROR': Fore.RED,
            'CRITICAL': Fore.RED + Style.BRIGHT,
        }

        def format(self, record):
            color = self.COLORS.get(record.levelname, Fore.WHITE)
            message = super().format(record)
            return f"{color}{message}{Style.RESET_ALL}"

    # 日志格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

    # 控制台格式器，带颜色
    colored_formatter = ColoredFormatter(fmt)
    ls.setFormatter(colored_formatter)

    # 文件格式器，不带颜色
    file_formatter = logging.Formatter(fmt)
    lht.setFormatter(file_formatter)

    # 将处理器添加到记录器
    logger.addHandler(lht)
    logger.addHandler(ls)
