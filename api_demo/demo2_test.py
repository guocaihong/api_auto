# encoding=utf-8

import requests, pytest
from log.log_setting import logger


class Test_Demo2:
    ## class级
    def setup_class(self):
        logger.info('setup class级')

    def teardown_class(self):
        logger.info('teardown class级')

    ## 方法级
    def setup(self):
        logger.info('setup 方法级')

    def teardown(self):
        logger.info('teardown 方法级')

    @pytest.mark.test
    def test_1(self):
        print('demo2.test_1')
        logger.info("这里是log打印")
        assert 1
    @pytest.mark.test
    def test_2(self):
        print('demo2.test_2')
        assert 1 <= 2


if __name__ == 'main':
    pytest.main('-s demo2_test.py')
