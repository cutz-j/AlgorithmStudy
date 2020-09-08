
def nonDivisibleSubset(k, s):
    # Write your code here
    remainder = {}
    result1, result2 = 0, 0
    for i in range(len(s)):
        rem = s[i]%k
        if remainder.get(rem, -1) != -1:
            remainder[rem] += 1
        else:
            remainder[rem] = 1
        

    for i in range(1, k//2+1):
        if i != k-1:
            # i를 나머지로 갖는 수와 k-1를 나머지로 갖는 수는 그 중 max
            result1 += max(remainder.get(i, 0), remainder.get(k-1, 0))
            result2 += max(S_remainder.count(i), S_remainder.count(k-i))
            print(k-1,  S_remainder.count(k-i), S_remainder)
        else:
            # 아닐 경우, 1개로 압축
            result1 += int(bool(remainder.get(i, 0)))
            result2 += int(bool(S_remainder.count(i)))
    
    # 나머지가 0인 경우 1개로 압축
    value = remainder.get(0, -1)
    result += 1 if value != -1 else 0
    
    return result


for i in range(1, k // 2 + 1):  # (1, k-1), (2, k-2), ... 순회
    if i != k-i:
        # i를 나머지로 갖는 정수들과 k-i를 나머지로 갖는 정수들 중 더 많은 쪽을 포함시킴.
        
    else:
        # k로 나눈 나머지가 k//2인 정수가 있는지 확인하여 하나만 포함시킴.
        result += int(bool(S_remainder.count(i)))