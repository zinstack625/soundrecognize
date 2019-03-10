# -*- coding: utf-8 -*-
from numpy import fft

def detfreq(buf):
    print(buf[0])
    #newbuf = [ int(buf[i] + buf[i+1]) for i in range(0, len(buf), 2) ]
    freqtable = fft.fft(newbuf)
    maximum = 0
    maxindex = -1
    for i in enumerate(freqtable):
        if (abs(i[1]) > max):
            maximum = abs(i[1])
            maxindex = i[0]
    freq = freqtable[maxindex]
    return freq

def normalize(buf):
    # searching for volume peaks
    maximum = 0
    for i in buf:
        if (abs(i) > maximum):
            maximum = abs(i)
    coeff = 32768 / max
    # normalizing
    newbuf = [ i * coeff for i in buf ]
    return newbuf

def normalizefreq(buf, freq):
    newbuf = [ buf[int(i * (100.0 / freq))] for i in range(0, len(buf)) ]
    for j in range(0, 3):
        for i in range(0, len(newbuf)):
            if newbuf[i] == newbuf[i-1]:
                newbuf[i] = (newbuf[i-1] + newbuf[i+1]) / 2
    return newbuf

def prepare(buf):
    newbuf = normalizefreq(buf, detfreq(buf))
    newbuf = normalize(newbuf)
    return newbuf
