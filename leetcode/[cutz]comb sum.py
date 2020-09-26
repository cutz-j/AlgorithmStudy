class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []

        def dfs(i, cand, ans):
            if ans == target:
                self.results.append(cand[:])
                return
            elif ans > target:
                return

            for k in range(i, len(candidates)):
                cand.append(candidates[k])
                dfs(k, cand, ans + candidates[k])
                cand.pop()

        dfs(0, [], 0)
        return self.results