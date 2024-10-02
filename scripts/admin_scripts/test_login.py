import pytest

import utils
from config import *
from page.admin.login_page import LoginPage


@pytest.mark.run(order=2)
class TestLogin:

    @classmethod
    def setup_class(cls):
        driver_admin = utils.DriverUtils.get_driver("admin")
        driver_admin.get(BASE_URL + "/index.php/Admin/Admin/login")

    @classmethod
    def teardown_class(cls):
        utils.DriverUtils.quit_driver("admin")

    def test_login(self):
        LoginPage().admin_login("admin", "HM_2023_test", "8888")
        try:
            assert utils.is_el_exist_by_text("admin", "admin") is True
        except AssertionError as e:
            utils.DriverUtils.get_driver("admin").save_screenshot(
                BASE_PATH + f"/screenshots/admin/test_login{utils.TimeUtils.get_current_timestamp_int().__str__()}.png")
            raise e
