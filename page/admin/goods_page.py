"""
商品管理页面
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_page import BasePageAdmin


class GoodsPage(BasePageAdmin):
    def __init__(self):
        super().__init__()
        self.__loc_iframe = (By.ID, "workspace")

        self.__loc_add_goods_btn = (By.XPATH, "//*[text()='添加商品']")

        # 商品名称
        self.__loc_goods_name = (By.NAME, "goods_name")

        # 商品分类
        self.__loc_goods_category_1 = (By.ID, "cat_id")
        self.__loc_goods_category_2 = (By.ID, "cat_id_2")
        self.__loc_goods_category_3 = (By.ID, "cat_id_3")

        # 本店售价
        self.__loc_goods_price = (By.NAME, "shop_price")

        # 市场价
        self.__loc_market_price = (By.NAME, "market_price")
        # 是否包邮
        self.__loc_is_free_shipping = (By.ID, "is_free_shipping_label_{}")
        # 提交

        self.__loc_submit_btn = (By.XPATH, "//*[text()='确认提交']")

    def goods_add(self, goods_name, goods_price, goods_market_price, goods_category_1, goods_category_2,
                  goods_category_3, is_free_shipping):
        """
        添加商品
        :param goods_name: 商品名称
        :param goods_price: 本店售价
        :param goods_market_price: 市场价
        :param goods_category_1: 商品分类第一级
        :param goods_category_2: 商品分类第二级
        :param goods_category_3: 商品分类第三级
        :param is_free_shipping: 是否包邮
        """

        # 切换到指定的iframe
        self.base_switch_to_frame(self.__loc_iframe)

        # 点击添加商品按钮
        self.base_click(self.__loc_add_goods_btn)

        # 输入商品名称
        self.base_input(self.__loc_goods_name, goods_name)

        # 选择商品的第一级分类
        Select(self.base_find_element(self.__loc_goods_category_1)).select_by_value(goods_category_1)

        # 选择商品的第二级分类
        Select(self.base_find_element(self.__loc_goods_category_2)).select_by_value(goods_category_2)

        # 选择商品的第三级分类
        Select(self.base_find_element(self.__loc_goods_category_3)).select_by_value(goods_category_3)

        # 输入商品价格
        self.base_input(self.__loc_goods_price, goods_price)

        # 输入市场价格
        self.base_input(self.__loc_market_price, goods_market_price)

        # 根据是否包邮设置相应的值
        shipping_value = 1 if is_free_shipping else 0

        # 点击包邮选项
        self.base_click((self.__loc_is_free_shipping[0], self.__loc_is_free_shipping[1].format(shipping_value)))

        # 提交商品信息
        self.base_click(self.__loc_submit_btn)
