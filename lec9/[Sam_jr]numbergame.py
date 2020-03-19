def dp(left, right):
    if not cache[left][right] is None:
        return cache[left][right]

    if left == right:
        cache[left][right] = board[left]
        return cache[left][right]
    elif (right - left) == 1:
        if board[left] > board[right]:
            diff = board[left] - board[right]
        else:
            diff = board[right] - board[left]

        cache[left][right] = diff
        return cache[left][right]
    else:
        # 4 cases
        ret = EMPTY
        # Delete left 2
        ret = max(ret, -dp(left+2, right))
        # Delete right 2
        ret = max(ret, -dp(left, right-2))
        # Gain left 1
        ret = max(ret, board[left] - dp(left+1, right))
        # Gain right 1
        ret = max(ret, board[right] - dp(left, right-1))

        cache[left][right] = ret
        return cache[left][right]
def solve():
    return dp(0, num_num-1)
    
if __name__=='__main__':
    EMPTY = -987654321
    
    test_case = int(input())
    num_list = []
    for _ in range(test_case):
        num_num = int(input())
        board = [int(x) for x in input().split()]
        cache = [[None for _ in range(num_num)] for _ in range(num_num)]   
        print(solve())