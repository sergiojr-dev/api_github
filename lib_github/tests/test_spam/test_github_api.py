from unittest.mock import Mock

import pytest

from lib_github import avatar


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/133528508?v=4'
    resp_mock.json.return_value = {
        "login": "sergiojr-dev", "id": 133528508,
        "avatar_url": url,
    }
    get_original = avatar.requests.get
    avatar.requests.get = Mock(return_value=resp_mock)
    yield url
    avatar.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = avatar.avatar('sergiojr-dev')
    assert avatar_url == url




