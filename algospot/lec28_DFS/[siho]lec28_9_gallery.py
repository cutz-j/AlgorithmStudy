import sys


def adjacency(mat_, g1, g2):

    mat_[g1].append(g2)
    mat_[g2].append(g1)

    return mat_


def dfs(gallery, visited):

    visited[gallery] = True
    children = [0]*len(cases)
    installed = 0
    for adj_gallery in adj_mat[gallery]:

        if not visited[adj_gallery]:
            case, installation = dfs(adj_gallery, visited)
            children[case] += 1
            installed += installation

    if children[cases.get('unwatched')]:
        installed += 1
        return cases.get('installed'), installed
    if children[cases.get('installed')]:
        return cases.get('watched'), installed

    return cases.get('unwatched'), installed


def installCamera():

    installed = 0
    for gallery in range(g):

        if not visited[gallery]:
            case, installation = dfs(gallery, visited)
            installed += installation
            if case == cases.get('unwatched'):
                installed += 1

    return installed


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':

    C = int(input_())
    cases = {'unwatched': 0, 'watched': 1, 'installed': 2}
    for _ in range(C):

        g, h = map(int, input_().split())
        adj_mat = [[] for _ in range(g)]
        #     installed = 0
        visited = [False] * g
        for _ in range(h):
            g1, g2 = map(int, input_().split())
            adj_mat = adjacency(adj_mat, g1, g2)

        print(installCamera())
