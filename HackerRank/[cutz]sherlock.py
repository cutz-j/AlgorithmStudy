import sys
from collections import Counter


def is_valid(s):
    s_count = Counter(s)
    s_sorted = Counter(s_count.values()).most_common()
    same_num, same_count = s_sorted[0]
    
    if len(s_sorted) == 2:
        diff_num, count = s_sorted[1]
        if diff_num-1 == same_num and count == 1:
            return True
        elif diff_num == 1 and count == 1:
            return True
    elif len(s_sorted) == 1 and same_count == 1:
        return True
    else:
        return False
            
        



#rl = lambda:sys.stdin.readline()
rl = input

s = input().strip()
result = is_valid(s)
if result:
    print("YES")
else:
    print("NO")

