import pytest

from utils import DriverUtils


@pytest.mark.run(order=101)
class TestBegin:
    def test_begin(self):
        DriverUtils.change_buyer_key(False)
