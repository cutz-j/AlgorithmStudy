import sys

# dfs
min_val, max_val = sys.maxsize, -sys.maxsize

def dfs(i, res, add, sub, mul, div):
    global min_val, max_val
    if i == N:
        min_val = min(res, min_val)
        max_val = max(res, max_val)
        return
    if add:
        dfs(i+1, res+arr[i], add-1, sub, mul, div)
    if sub:
        dfs(i+1, res-arr[i], add, sub-1, mul, div)
    if mul:
        dfs(i+1, res*arr[i], add, sub, mul-1, div)
    if div:
        dfs(i+1, int(res/arr[i]), add, sub, mul, div-1)


rl = lambda: sys.stdin.readline()

N = int(rl())
arr = list(map(int, rl().split()))
add, sub, mul, div = map(int, rl().split())


dfs(1, arr[0], add, sub, mul, div)
print(max_val)
print(min_val)







#
# op_arr = []
# op_arr += ['+']*op_list[0]
# op_arr += ['-']*op_list[1]
# op_arr += ['*']*op_list[2]
# op_arr += ['/']*op_list[3]
# #
# op_permutation = permutations()
#
# # cache = {}
# min_res, max_res = sys.maxsize, 0
# for op_p in op_permutation:
#     value = 0
#     stack = []
#     for i in range(N-1, 0, -1):
#         stack.append(arr[i])
#         stack.append(op_p[i-1])
#     stack.append(arr[0])
#
#     res = stack.pop(-1)
#     while stack:
#         v = stack.pop(-1)
#         if v == '+':
#            res += stack.pop(-1)
#         elif v == '-':
#             res -= stack.pop(-1)
#         elif v == '*':
#             res *= stack.pop(-1)
#         elif v == '/':
#             if res < 0:
#                 res = abs(res) // stack.pop(-1)
#             else:
#                 res //= stack.pop(-1)
#
#     if res < min_res:
#         min_res = res
#     if res > max_res:
#         max_res = res
# print(max_res)
# print(min_res)



