import sys

cache = {}


# def dp(n, answer, exp, number, N):
#     print(n, answer, exp)
#     if n >= 9:
#         return n
#
#     if answer == number:
#         return n
#
#     if cache.get(tuple(exp), -1) != -1:
#         return cache[tuple(exp)]
#
#     exp_copy = [i for i in exp]
#     for i in range(5):
#         exp_copy[i] += 1
#         if i == 0:
#             cache[tuple(exp_copy)] = min(dp(n + 1, answer + N, exp_copy, number, N),
#                                          cache.get(tuple(exp_copy), sys.maxsize))
#             exp_copy[i] -= 1
#         elif i == 1:
#             cache[tuple(exp_copy)] = min(dp(n + 1, answer - N, exp_copy, number, N),
#                                          cache.get(tuple(exp_copy), sys.maxsize))
#             exp_copy[i] -= 1
#         elif i == 2:
#             cache[tuple(exp_copy)] = min(dp(n + 1, answer * N, exp_copy, number, N),
#                                          cache.get(tuple(exp_copy), sys.maxsize))
#             exp_copy[i] -= 1
#         elif i == 3:
#             cache[tuple(exp_copy)] = min(dp(n + 1, answer // N, exp_copy, number, N),
#                                          cache.get(tuple(exp_copy), sys.maxsize))
#             exp_copy[i] -= 1
#         elif i == 4:
#             ans = str(answer) + str(N)
#             cache[tuple(exp_copy)] = min(dp(n + 1, int(ans), exp_copy, number, N),
#                                          cache.get(tuple(exp_copy), sys.maxsize))
#             exp_copy[i] -= 1
#
#     return cache[tuple(exp)]

def solution(N, number):
    answer = -1
    dp = {}
    s = [set() for x in range(8)]
    for i,x  in enumerate(s, start=1):
        x.add(int(str(N)*i))

    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break


    # answer = min(cache.values())
    return answer

print(solution(4, 17))