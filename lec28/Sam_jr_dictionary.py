# -*- coding: utf-8 -*-

order = []
seen = []


def graphMaker(words):
    for i, w in enumerate(words):
        if i == 0:
            continue
        w1, w2 = list(words[i-1]), list(w)
        length = min(len(w1), len(w2))
        w1_, w2_ = w1[:length], w2[:length]
        for c1, c2 in zip(w1_, w2_):
            if c1 != c2:
                a = ord(c2) - 97
                b = ord(c1) - 97
                alphabet[a][b] = 1
                


def dfs(here):
    seen[here] = 1
    for there, seen_there in enumerate(seen):
        if alphabet[here][there] and not seen_there:
            dfs(there)
    order.append(here)


def topoSort():
    global seen, order
    seen = [0 for _ in range(26)]
    order = []

    for i, v in enumerate(seen):
        if not v:
            dfs(i)

    reversed(order)

    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            if alphabet[order[i]][order[j]]:
                return []

    return order


if __name__ == '__main__':
    idx2char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    c = int(input())
    case = []
    for _ in range(c):
        n = int(input())
        words = [input() for _ in range(n)]

        alphabet = [[0 for _ in range(26)] for _ in range(26)]

        graphMaker(words)
        result = topoSort()

        if result:
            print("".join(map(lambda x: idx2char[x], result)))
        else:
            print("INVALID HYPOTHESIS")