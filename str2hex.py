#!/usr/bin/env python
# The original: https://github.com/vinxue/Toolkit/blob/master/Python/HashBin/StrToHex.py

import sys
import struct

def str_to_hex():
    if len(sys.argv) != 3:
       print ('Usage: %s [input file] [out file]' % (sys.argv[0]))
       return

    try:
        input_file = open(sys.argv[1], 'r', encoding='utf8')
    except IOError:
        print('Open file failed.\n')
        return

    out_file = open(sys.argv[2], 'wb')

    line = input_file.readline()

    while line:
        if line[0] != '0':
            line = input_file.readline()
            continue

        line = line.strip()
        line = line.replace("- ", "")
        line = line.replace("-", " ")
        # print(line)

        if line[8] == ':':
            start_offset = 9
        elif line[9] == ':':
            start_offset = 10

        for index in range(0, 48, 3):
            if line[start_offset + index:start_offset + index + 2] == '  ':
                break

            hexbyte = struct.pack('B', int(line[start_offset + index + 1:start_offset + index + 3], 16))
            out_file.write(hexbyte)

        line = input_file.readline()

    input_file.close()
    out_file.close()
    print ('Convert string to hex file successfully.\n')

if __name__ == "__main__":
    str_to_hex()
