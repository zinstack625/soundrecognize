from numpy import fft

def detfreq(buf):
    freqtable = fft.fft(buf)
    maximum = 0
    maxindex = -1
    for i in enumerate(freqtable):
        if (abs(i[1]) > max):
            maximum = abs(i[1])
            maxindex = i[0]
    freq = freqtable[maxindex]
    return freq

def normalize(buf):
    # поиск пиков громкости
    maximum = 0
    for i in buf:
        if (abs(i) > maximum):
            maximum = abs(i)
    coeff = 32768 / max
    # нормализация
    newbuf = [ i * coeff for i in buf ]
    return newbuffer


