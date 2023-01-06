#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Get Os Name
__author__ = 'lbbxsxlz@gmail.com'

import platform

def get_os_name():
    sys = platform.system()
    if sys == "Windows":
        print("OS is Windows!")
    elif sys == "Linux":
        print("OS is Linux!")


if __name__ == "__main__":
    get_os_name()

