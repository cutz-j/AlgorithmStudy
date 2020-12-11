cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2),]

def dp(cargo, capacity):
    cache = {}
    for i in range(len(cargo)+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                if cache.get(i, []):
                    cache[i].append(0)
                else:
                    cache[i] = [0]
            elif cargo[i-1][1] <= j:
                cache[i].append(max(cargo[i-1][0] + cache[i-1][j-cargo[i-1][1]], cache[i-1][j]))
            else:
                cache[i].append(cache[i-1][j])

    return cache[i][j]

print(dp(cargo, 15))