import heapq
from collections import Counter

class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        # 가능한 경우의 수가 아님 -- set을 통해서 했을 경우
        unique_s = list(set(list(s)))
        heap = []

        for i in unique_s:
            heapq.heappush(heap, ord(i))

        answer = ''
        for _ in range(len(unique_s)):
            answer += chr(heapq.heappop(heap))

        return answer

    def removeDuplicateLetters2(self, s: str) -> str:

        s_set = sorted(set(s))  # set --> team sort
        for c in s_set:
            suffix = s[s.index(c):]  # slice after c

            if set(s) == set(suffix):
                # if euqal --> possible.
                return c + self.removeDuplicateLetters2(suffix.replace(c, ''))

        return ''

    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []

        for c in s:
            counter[c] -= 1

            if c in stack:
                continue

            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(c)

        return ''.join(stack)