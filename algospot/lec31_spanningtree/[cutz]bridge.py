import sys

def get_node_num(block, i, j, cur_list):
    global graph_num
    present = block[i][j]
    if present == 0:
        return block, cur_list
        
    block[i][j] = 0
    cur_list.append((i, j))
    
    
    for k in range(4):
        new_i, new_j = i+row_dir[k], j+col_dir[k]
        
        if (new_i >= 0 and new_i < N) and (new_j >= 0 and new_j < M):
            if block[new_i][new_j] == 1:
                get_node_num(block, new_i, new_j, cur_list)
    
    return block, cur_list

def edge_search(graph, y, x, g):
    for cur_g, coord in enumerate(graph):
        if cur_g == g:
            continue
        for cur_y, cur_x in coord:
            sub_y, sub_x = cur_y - y,  cur_x - x
            one_cnt = 0
            if sub_y == 0 and abs(sub_x) > 2:
                if sub_x < 0:
                    for j in range(cur_x+1, x):
                        if block[cur_y][j] == 1:
                            one_cnt = 1
                    if one_cnt == 0:
                        if ((abs(sub_x)-1, (g, cur_g)) not in adj) and ((abs(sub_x)-1, (cur_g, g)) not in adj):
                            adj.append((abs(sub_x)-1, (g, cur_g)))
                else:
                    for j in range(x+1, cur_x):
                        if block[cur_y][j] == 1:
                            one_cnt = 1
                    if one_cnt == 0:
                        if ((abs(sub_x)-1, (g, cur_g)) not in adj) and ((abs(sub_x)-1, (cur_g, g)) not in adj):
                            adj.append((abs(sub_x)-1, (g, cur_g)))
            
            elif sub_x == 0 and abs(sub_y) > 2:
                if sub_y < 0:
                    for i in range(cur_y+1, y):
                        if block[i][cur_x] == 1:
                            one_cnt = 1
                    if one_cnt == 0:
                        if ((abs(sub_y)-1, (g, cur_g)) not in adj) and ((abs(sub_y)-1, (cur_g, g)) not in adj): 
                            adj.append((abs(sub_y)-1, (g, cur_g)))
                else:
                    for i in range(y+1, cur_y):
                        if block[i][cur_x] == 1:
                            one_cnt = 1
                    if one_cnt == 0:
                        if ((abs(sub_y)-1, (g, cur_g)) not in adj) and ((abs(sub_y)-1, (cur_g, g)) not in adj): 
                            adj.append((abs(sub_y)-1, (g, cur_g)))
            
def find(x):
    k = []
    while parent[x] != x:
        k.append(x)
        x = parent[x]
        
    for i in k:
        parent[i] = x
    
    return x

def merge(a, b):
    parent[b] = a
    


rl = input
# rl = lambda:sys.stdin.readline()

row_dir = [-1, 0, 1, 0]
col_dir = [0, -1, 0, 1]
cur_list, graph_coord = [], []
N, M = map(int, rl().split())
block, new_block = [], []
for _ in range(N):
    tmp = list(map(int, rl().split()))
    block.append(tmp)
    new_block.append(tmp.copy())

# node
for i in range(N):
    for j in range(M):
        new_graph, cur_list = get_node_num(new_block, i, j, cur_list)
        if cur_list:
            graph_coord.append(cur_list)
            cur_list = []

# possible edge
adj = []
for g, coord in enumerate(graph_coord):
    for y, x in coord:
        edge_search(graph_coord, y, x, g)
            
# spanning tree
adj.sort()
parent = {i:i for i in range(len(graph_coord))}

ans = 0
for weight, (a, b) in adj:
    a, b = find(a), find(b)
    if a == b:
        continue
    
    ans += weight
    merge(a, b)

for i in range(len(graph_coord)):
    find(i)

impossible = False
last_p = parent[0]
for p in parent.values():
    if last_p != p:
        impossible = True
    last_p = p

if impossible:
    print(-1)
else:
    print(ans)
    
