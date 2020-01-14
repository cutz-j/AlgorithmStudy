# -*- coding: utf-8 -*-

import sys
#For testing

def solve(n, k):

    num = 1983
    num_sum = 0


    sig_list = [0] * 0x400
    #signal = signal_generator()
    bp = 0
    tp = 0
    count = 0
    gen_count = 0
    pop_limit = 1024

    while gen_count < n:
        s = sig_list[tp]-sig_list[bp]
        #print("i=%d, s=%d" % (genCount,s))
        if s<k:
            #print("+")
            #sig_list.append(signal.next())
            gen_count += 1
            tp += 1
            tp &= 0x3FF

            num_sum += num % 10000 + 1
            num = (num*214013 + 2531011) & 0xFFFFFFFF

            sig_list[tp] = num_sum


        elif s>k:
            #print("-")
            #list.pop(0)
            bp+=1
            bp &= 0x3FF
            """
            if bp > pop_limit :
            sig_list = sig_list[pop_limit:]
                bp -= pop_limit
                tp -= pop_limit
            """
        else:
            #print("=")
            count += 1
            #sig_list.append(signal.next())
            gen_count += 1
            tp += 1
            tp &= 0x3FF
            num_sum += num % 10000 + 1
            num = (num*214013 + 2531011) & 0xFFFFFFFF

            sig_list[tp] = num_sum
    print count

if __name__ == "__main__":
    rl = lambda: sys.stdin.readline()
    for _ in xrange(int(rl())):
        input = rl().split()
        solve(int(input[1]), int(input[0]))

