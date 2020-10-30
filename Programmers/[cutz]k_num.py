def solution(array: list, commands: list) -> list:
    answer = []
    for i,j,k in commands:
        print(i,j,k, array)
        answer.append(sorted(array[i-1:j])[k-1])
    return answer