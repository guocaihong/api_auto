import requests, pytest
import random
from log.log_setting import logger

from config.host_config import java_host

temp = [1, 2]


@pytest.mark.online
@pytest.mark.smoke_test
def test_1():
    res = requests.get('http://www.baidu.com')
    logger.info(res)
    assert res.status_code == 200


@pytest.mark.skip
@pytest.mark.test
def test_2():
    logger.warning('test_2')
    c = random.choice(temp)
    d = random.choice(temp)
    assert c == d


@pytest.mark.test
def test_queryAll():
    url = f'{java_host}/roundHistory/queryAll'
    logger.info(url)
    res = requests.get(url)
    logger.info(res.text)
    assert res.status_code == 200


@pytest.mark.test
def test_config():
    url = f'{java_host}/config?val=haha'
    logger.info(url)
    res = requests.get(url)
    logger.info(res.text)
    assert res.status_code == 200


if __name__ == 'main':
    pytest.main('-s demo1_test.py')
