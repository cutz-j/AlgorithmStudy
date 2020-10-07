import sys

def dp():
    cache[(dice[0])] = line[dice[0]]

    for i in range(1, 10):
        dice[i]




rl = lambda:sys.stdin.readline()

line = [i for i in range(2, 41, 2)]
ten = [10, 13, 16, 19, 25, 30, 35, 40]
twe = [20, 22, 24, 25, 30, 35, 40]
thr = [30, 28, 27, 26, 25, 30, 35, 40]
road = [10, 20, 30]
raod_map = [ten, twe, thr]

horse = [0, 0, 0, 0]
cache = {}

dice = list(map(int, rl().split()))