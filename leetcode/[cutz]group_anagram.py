from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for s in strs:
            answer[tuple(sorted(s))].append(s)

        res = []
        for k in answer:
            res.append(answer[k])

        return res