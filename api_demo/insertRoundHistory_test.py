import requests, pytest
import time, random
from log.log_setting import logger

from config.host_config import java_host


@pytest.mark.test
def test_insert_success():
    url = f'{java_host}/roundHistory/insertRoundHistory'
    param = {
        'monsterId': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        'kugouId': 1512159918
    }
    logger.info(url)
    res = requests.get(url, param)
    logger.info(res.text)
    assert res.status_code == 200
