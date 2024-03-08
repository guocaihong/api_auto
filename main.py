# encoding=utf-8

import pytest


def main():
    pytest.main(["--reruns", "1", "--reruns-delay", "2", "--alluredir", "allure-results"])


if __name__ == '__main__':
    main()
