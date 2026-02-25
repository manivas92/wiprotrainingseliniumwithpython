import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self,driver):


