from unittest.mock import Mock

import pytest

from lib_github import avatar


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/133528508?v=4'
    resp_mock.json.return_value = {
        "login": "sergiojr-dev", "id": 133528508,
        "avatar_url": url,
    }
    get_mock = mocker.patch('lib_github.avatar.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = avatar.avatar('sergio0006')
    assert avatar_url == url




