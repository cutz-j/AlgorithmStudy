import sys

def getEulerCircuit(here, circuit):
    for there in range(len(adj[here])):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            adj[there][here] -= 1
            getEulerCircuit(there, circuit)
    circuit.append(here)


rl = input
# rl = lambda: sys.stdin.readline()

N = int(rl())
adj = []
for _ in range(N):
    adj.append(list(map(int, rl().split())))
    
circuit = []
getEulerCircuit(1, circuit)