from collections import defaultdict

def solve(s):
    hash_dict = defaultdict(int)

    for i in range(len(s)):
        hash_dict[s[i]] += 1
        

    return