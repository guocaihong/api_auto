#coding=utf-8

import logging

logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)

# 定义屏幕控制器把日志输出屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # 输出屏幕的日志级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)  # 给输出屏幕的日志设置日志格式
logger.addHandler(ch)  # 将设定好的控制器添加到日志器中

# # 定义文件控制器把日志输出文件
# fh = logging.FileHandler("access.log")
# fh.setLevel(logging.DEBUG)  # 设置输出文件的日志级别
# formatter_fh = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter_fh)  # 给输出文件的日志设置日志格式
# logger.addHandler(fh)  # 将设定好的控制器添加到日志器中