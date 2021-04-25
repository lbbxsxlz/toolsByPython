#!/usr/bin/python
# -*- encoding=utf8 -*-

'''
sudo python3 recvEther.py
'''

import base64
import struct
import binascii

from socket import (
    PF_PACKET,
    SOCK_RAW,
    socket,
    htons,
)

rawSocket = socket(PF_PACKET, SOCK_RAW, htons(0x1024))

pkt = rawSocket.recvfrom(1514)

ethernetHeader = pkt[0][0:14]   #提取以太网帧头
eth_hdr = struct.unpack("!6s6s2s",ethernetHeader) #6字节目的mac地址，6字节源mac地址，2字节协议类型

dstMac = binascii.hexlify(eth_hdr[0])
srcMac = binascii.hexlify(eth_hdr[1])
etherType = binascii.hexlify(eth_hdr[2])

print(dstMac.decode('utf-8'))
print(srcMac.decode('utf-8'))
print(etherType.decode('utf-8'))
print(pkt[0][14:-1].decode('utf-8'))
