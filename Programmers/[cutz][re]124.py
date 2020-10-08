def solution(n):
    answer = ''
    numbers = ['4', '1', '2']
    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
        print(answer, n)

    return answer