# encoding=utf-8

import requests, pytest
import allure
from log.log_setting import logger

@allure.feature('class上的feature注解')
@allure.story('class上的story注解')
@allure.tag('class上的tag注解')
@allure.title('class上的title注解')
@allure.epic('class上的epic注解')
@allure.step('class上的step注解')
@allure.suite('class上的suite注解')
@allure.issue("class上的url")
@allure.id('class上的id')
@allure.label('label_type', 'labels')
@allure.description('class上的 description')
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

    @allure.feature('method 上的feature注解')
    @allure.story('method 上的story注解')
    @allure.tag('method 上的tag注解')
    @allure.title('method 上的title注解')
    @allure.epic('method 上的epic注解')
    @allure.step('method 上的step注解')
    @allure.suite('method 上的suite注解')
    @allure.issue("method 上的url")
    @allure.id('method 上的id')
    @allure.label('label_type', 'labels')
    @allure.description('method 上的 description')
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
