from collections import defaultdict

def solution(phone_book: list) -> bool:
    answer = True
    hash_dict = defaultdict(int)
    for num in phone_book:
        hash_dict[num] += 1

    for num in phone_book:
        tmp = ''
        hash_dict[num] -= 1
        for n in num:
            tmp += n
            if hash_dict.get(tmp, 0):
                return False
        hash_dict[num] += 1
    return answer