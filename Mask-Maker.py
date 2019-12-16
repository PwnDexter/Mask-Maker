#!/usr/bin/env python3
"""
usage: ./maskgen.py <charset> <length>

"""

import sys

if len(sys.argv) < 3:
    customCharset = '?l?u,'
    maxLen = 10
else:
    customCharset = str(sys.argv[1])
    maxLen = int(sys.argv[2])


def genMiddle(length):
        mask = '?1'
        for i in range(1, length):
            mask = "{}{}".format(mask, '?1')
        return mask

if  __name__ == "__main__":
    for i in range(1,maxLen):
        fullMask = "{}{}{}{}".format(customCharset, '?d?d', genMiddle(i), '?d?d')
        print(fullMask)
