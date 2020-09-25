class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        cnt = 0
        sub = {}
        answer = ''
        for char in s:
            if char not in sub:
                sub[char] = cnt
                cnt += 1
            else:
                i = sub[char]
                if len(sub) > best:
                    best = len(sub)

                new_sub, cnt = {}, 0
                for idx in range(i + 1, len(sub)):
                    new_sub[list(sub)[idx]] = cnt
                    cnt += 1
                new_sub[char] = cnt
                cnt += 1
                sub = new_sub
        if sub:
            if len(sub) > best:
                best = len(sub)
        return best