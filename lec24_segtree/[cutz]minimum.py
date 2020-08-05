import sys
sys.setrecursionlimit(999999990)

def init():
    t = 1
    while t <= N:
        # level down
        t *= 2
    
    # final leaf init
    for i in range(N):
        tree[t+i] = int_list[i]
        
    # upper node
    for i in range(t-1, 0, -1):
        # left right lower node
        # minimum tree
        tree[i] = min(tree[i*2], tree[i*2+1])
        
def init_rc(left, right, node):
    if left == right:
        tree[node] = int_list[left]
        return tree[node]
    
    mid = (left + right) // 2
    left_min = init_rc(left, mid, node*2)
    right_min = init_rc(mid+1, right, node*2+1)
    tree[node] = min(left_min, right_min)
    return tree[node]

def query(left, right, node, node_left, node_right):
    if right < node_left or left > node_right:
        return sys.maxsize
    if left <= node_left and right >= node_right:
        return tree[node]
    mid = (node_left + node_right)//2
    return min(query(left, right, node*2, node_left, mid),
               query(left, right, node*2+1, mid+1, node_right))

rl = input
# rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())

int_list = []
for _ in range(N):
    int_list.append(int(rl()))

coord = []
for _ in range(M):
    a, b = map(int, rl().split())
    coord.append((a, b))
    
tree = [sys.maxsize] * 4*N
init_rc(0, N-1, 1)
#
for l, r in coord:
    print(query(l-1, r-1, 1, 0, N-1))
