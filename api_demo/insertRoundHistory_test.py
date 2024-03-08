# encoding=utf-8

import requests, pytest
import time, random
import allure
from log.log_setting import logger

from config.host_config import java_host


@allure.story('插入轮次历史数据')
@pytest.mark.test
def test_insert_success():
    url = f'{java_host}/roundHistory/insertRoundHistory'
    param = {
        'monsterId': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        'kugouId': 1512159918
    }
    logger.info("请求URL："+url)
    logger.info("请求参数："+str(param))
    res = requests.get(url, param)
    logger.info("响应："+res.text)
    assert res.status_code == 200
