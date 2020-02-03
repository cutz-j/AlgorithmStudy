import sys


def adjacency(mat_, v1, v2, cost):

    mat_[v1-1][v2-1] = cost
    mat_[v2-1][v1-1] = cost
    return mat_


def solve():

    for k in range(V):

        w = order[k]
        for i in range(V):
            for j in range(V):

                adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][w] + adj_mat[w][j])   # i -> j vs. i -> w -> j
                W[i][j] = min(adj_mat[i][w] + delay[w] + adj_mat[w][j], W[i][j])


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':
    V, E = map(int, input_().split())
    delay = list(map(int, input_().split()))

    W = [[sys.maxsize]*V for _ in range(V)]         # sys.maxsize ~= inf.
    adj_mat = [[sys.maxsize]*V for _ in range(V)]   # sys.maxsize ~= inf.
    for _ in range(E):

        A, B, C = map(int, input_().split())

        adj_mat = adjacency(adj_mat, A, B, C)
        W = adjacency(W, A, B, C)

    for idx_diag in range(V):

        W[idx_diag][idx_diag] = 0

    order = sorted(range(V), key=lambda k: delay[k])
    solve()

    T = int(input_())
    for _ in range(T):

        s, t = map(int, input_().split())
        print(W[s-1][t-1])
