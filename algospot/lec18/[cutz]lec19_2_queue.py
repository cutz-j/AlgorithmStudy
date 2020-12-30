import math

def signal_generator(n_length):
    a = [1983]
    signal = list()

    for index in range(n_length):
        a.append( (a[index] * 214013 + 2531011) % 2**32 )
        signal.append( int(a[index] % 10000 + 1) )
        #print signal[index]

    return signal


a = [1983]

signal = []

for i in range(10):
    a.append((a[i] * 214013+2531011) % 2**32)
    signal.append(int(a[i]%10000 + 1))