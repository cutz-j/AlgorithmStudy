def solution(board: list, moves: list) -> int:
    # board: 2d array
    # moves: column
    stack = []
    answer = 0
    row = len(board)
    for m in moves:
        for i in range(row):
            if board[i][m-1]:
                if not stack:
                    stack.append(board[i][m-1])
                else:
                    if stack[-1] == board[i][m-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer