import pytest


def main():
    pytest.main(["--reruns", "1", "--reruns-delay", "2"])


if __name__ == '__main__':
    main()
