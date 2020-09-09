
def nonDivisibleSubset(k, s):
    # Write your code here
    remainder = {}
    result = 0
    for i in range(len(s)):
        rem = s[i]%k
        if remainder.get(rem, -1) != -1:
            remainder[rem] += 1
        else:
            remainder[rem] = 1
        
    for i in range(1, k//2+1):
        if i != k-i:
            # i를 나머지로 갖는 수와 k-1를 나머지로 갖는 수는 그 중 max
            result += max(remainder.get(i, 0), remainder.get(k-i, 0))
        else:
            # 아닐 경우, 1개로 압축
            result += int(bool(remainder.get(i, 0)))
    
    # 나머지가 0인 경우 1개로 압축
    value = remainder.get(0, -1)
    result += 1 if value != -1 else 0
    
    return result