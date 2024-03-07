import requests,pytest
import random,logging

temp = [1,2]
@pytest.mark.online
@pytest.mark.smoke_test
def test_1():
    res = requests.get('http://www.baidu.com')
    logging.info(res)
    assert res.status_code == 200

@pytest.mark.skip
@pytest.mark.test
def test_2():
    logging.warning('test_2')
    c = random.choice(temp)
    d = random.choice(temp)
    assert c == d

if __name__ == 'main':
    pytest.main('-s demo1_test.py')

