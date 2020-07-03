import sys


def pack(W, i):

    if i == n:
        return 0
    if cache[W][i] != 0:
        return cache[W][i]
    ret = pack(W, i + 1)
    if W >= volume_list[i]:
        ret = max(ret, pack(W - volume_list[i], i + 1) + need_list[i])

    return ret


def reconstruct(W, i):

    if i == n:
        return
    if pack(W, i) == pack(W, i + 1):
        reconstruct(W, i + 1)
    else:
        picked_items.append(item_list[i])
        reconstruct(W - volume_list[i], i + 1)


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':

    C = int(input_())
    for _ in range(C):

        N, W = map(int, input_().split())
        cache = [[0]*(N + 1)]*(W + 1)
        item_list, volume_list, need_list = [0]*N, [0]*N, [0]*N
        for n in range(N):

            item, volume, need = input_().split()
            item_list[n] = item
            volume_list[n] = int(volume)
            need_list[n] = int(need)

        maxNeed = pack(W, 0)
        picked_items = []
        reconstruct(W, 0)
        print(maxNeed, len(picked_items))
        for item in picked_items:
            print(item)
