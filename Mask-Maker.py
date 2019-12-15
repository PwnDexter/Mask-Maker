#!/usr/bin/env python

def genMiddle(length):
        mask = "?1"
        for i in range (1,length):
            mask = mask + "?1"
        return mask

customCharset = "?l?u,"

for i in range (1,17):
    fullMask = customCharset + "?d?d" + genMiddle(i) + "?d?d"
    print (fullMask)
