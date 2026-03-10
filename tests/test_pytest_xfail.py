import pytest

@pytest.mark.xfail (reason = "найден баг в приложении")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail (reason = "баг исправлен в приложении")
def test_without_bug():
    ...