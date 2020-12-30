import sys

rl = input

S = rl()

s_list = S.split('-')

[print(a[0], end='') for a in s_list]