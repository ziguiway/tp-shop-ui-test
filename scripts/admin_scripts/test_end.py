import pytest

from utils import DriverUtils


@pytest.mark.run(order=100)
class TestEnd:
    def test_end(self):
        DriverUtils.change_admin_key(True)
        DriverUtils.quit_driver("admin")
