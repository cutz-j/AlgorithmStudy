# -*- coding: utf-8 -*-
import sys

def floyd():
    for k in range(V):
        for a in range(V):
            for b in range(V):
                if adj[a][b] > adj[a][k] + adj[k][b]:
                    adj[a][b] = adj[a][k] + adj[k][b]

def update(n1,n2,w):
    adj[n1][n2] = min(adj[n1][n2], w) 
    adj[n2][n1] = min(adj[n2][n1], w) 
    useless = True
    for a in range(V):
        for b in range(V):
            k = n1
            if adj[a][b] > adj[a][k] + adj[k][b]:
                adj[a][b] = adj[a][k] + adj[k][b]
                useless = False
            k = n2
            if adj[a][b] > adj[a][k] + adj[k][b]:
                adj[a][b] = adj[a][k] + adj[k][b]
                useless = False
    return useless
    
if __name__ == '__main__':
    test_case2 = lambda : sys.stdin.readline()
    for _ in range(int(test_case2())):
        V, E, N = map(int, test_case2().split())
        adj = [[float('inf') for _ in range(V)] for _ in range(V)]
        for _ in range(E):
            a,b,w = map(int, test_case2().split()) 
            adj[a-1][b-1] = w 
            adj[b-1][a-1] = w
    
        floyd()
    
        ans = 0
        for _ in range(N):
            a,b,w = map(int, test_case2().split())
            a, b = a - 1, b - 1
            useless = update(a,b,w)        
            if useless:
                ans += 1
    
        print(ans)