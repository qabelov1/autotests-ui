import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regress
def test_regress_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...
@pytest.mark.regress #маркировка применяется на все ниже тесты
class TestUserAuth:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.skow
    def test_logout(self):
        ...