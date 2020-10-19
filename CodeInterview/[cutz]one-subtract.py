from collections import defaultdict

def solve(word_list: list) -> bool:
    hash_dict = defaultdict(int)
    A, B = word_list[0] , word_list[1]
    for char in A:
        hash_dict[char] += 1
    one_switch = False
    for char in B:
        if hash_dict[char]:
            hash_dict[char] -= 1

        else:
            if one_switch:
                return False
            one_switch = True
    return True


print(solve(['pale', 'ple']))
print(solve(['pales', 'pale']))
print(solve(['pale', 'bale']))
print(solve(['pale', 'bake']))