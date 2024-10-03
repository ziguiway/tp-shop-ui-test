import pytest

from common.driver_type import DriverType
from utils import DriverUtils


@pytest.mark.run(order=104)
class TestEnd:
    def test_end(self):
        DriverUtils.change_buyer_key(True)
        DriverUtils.quit_driver(DriverType.BUYER)
