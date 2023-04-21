
#! /usr/bin/python3

import sys
import os

os.symlink(sys.argv[1], sys.argv[2])
