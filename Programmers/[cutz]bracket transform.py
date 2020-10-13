opening = ['(']
closing = [')']


def search(string):
    # basis
    if not string:
        return ""

    stack, save = [], []
    right = True
    opening_num, closing_num = 0, 0
    # search string
    for idx, char in enumerate(string):
        # opening
        if char == '(':
            stack.append(char)
            save.append(char)
            opening_num += 1
        # closing
        else:
            # (가 나오지 않았는데 )이 나왔을 때
            if not stack:
                right = False
            # ( )의 순서가 아닐 때
            else:
                if opening.index(stack[-1]) != closing.index(char):
                    right = False
                # pop stack
                stack.pop()

            save.append(char)
            closing_num += 1

        # balanced
        if opening_num == closing_num:
            # balanced and right
            if right:
                # recursive
                answer = ''.join(save) + search(string[idx + 1:])
                return answer

            # balanced and not right
            else:
                v = search(string[idx + 1:])
                # print(v)
                u = ''.join(save)[1:-1]
                ans = '('
                ans += v + ')'
                for u_char in u:
                    if u_char == '(':
                        ans += ')'
                    else:
                        ans += '('
                return ans


def solution(p):
    answer = ''
    answer = search(p)

    return answer