import logging
import os
from logging.handlers import TimedRotatingFileHandler

from colorama import Fore, Style, init

BASE_PATH = os.path.dirname(__file__)

BASE_URL = "http://hmshop-test.itheima.net/"

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

    # 自定义日志格式器，添加颜色支持
    class ColoredFormatter(logging.Formatter):
        COLORS = {
            'DEBUG': Fore.WHITE,
            'INFO': Fore.WHITE,
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
    fm = ColoredFormatter(fmt)

    # 为两个处理器设置格式器
    ls.setFormatter(fm)
    lht.setFormatter(fm)

    # 将处理器添加到记录器
    logger.addHandler(lht)
    logger.addHandler(ls)



