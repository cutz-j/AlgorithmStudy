class Solution:
    def isValid(self, s: str) -> bool:
        answer = True
        stack = []
        open_set, close_set = ['(', '{', '['], [')', '}', ']']

        for char in s:
            if char in open_set:
                stack.append(char)
            else:
                if not stack:
                    answer = False
                    break
                close_idx = close_set.index(char)
                open_idx = open_set.index(stack[-1])
                if close_idx != open_idx:
                    answer = False
                    break
                else:
                    stack.pop()

        if stack:
            answer = False
        return answer

