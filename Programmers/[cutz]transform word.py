from collections import defaultdict
import sys

answer = sys.maxsize


def dfs(b, n, target, adj, visited):
    global answer
    if b == target:
        if n < answer:
            answer = n
        return n

    visited[b] = True

    for a in adj[b]:
        if not visited[a]:
            dfs(a, n + 1, target, adj, visited)

    return n


def solution(begin: str, target: str, words: list):
    # begin : word
    # target : word
    # words 단어로 변환
    # 1번에 1개의 알파벳 변환
    global answer

    # build graph
    if target not in words:
        return 0

    adj = defaultdict(list)
    for word in words:
        for w in words:
            if word == w:
                continue
            diff = 0
            for i in range(len(word)):
                if word[i] != w[i]:
                    diff += 1
            if diff == 1:
                adj[word].append(w)

    # find minimum path
    # possible initial choice
    init = []
    for w in words:
        diff = 0
        for i in range(len(begin)):
            if begin[i] != w[i]:
                diff += 1
        if diff == 1:
            init.append(w)

    for i in init:
        visited = defaultdict(lambda: False)
        dfs(i, 1, target, adj, visited)

    if answer == sys.maxsize:
        answer = 0
    return answer