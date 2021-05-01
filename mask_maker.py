#!/usr/bin/env python3
"""
usage: ./maskgen.py <charset> <length>

"""

import sys

def genMiddle(length):
    return '?1' * length

def getCharset():
    try: customCharset
    except NameError:
        customCharset = 'yolo'
    return customCharset

def genMask(maxLen):
    masks = []
    for i in range(1,maxLen):
        masks.append("{}{}{}{}".format(getCharset(), '?d?d', genMiddle(i), '?d?d'))
    return '\n'.join(masks)

if  __name__ == "__main__":
    if len(sys.argv) < 3:
        customCharset = '?l?u,'
        maxLen = 10
    else:
        customCharset = str(sys.argv[1])
        maxLen = int(sys.argv[2])
    print(genMask(maxLen))
