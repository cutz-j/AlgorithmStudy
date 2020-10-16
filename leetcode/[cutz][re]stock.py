import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_profit = sys.maxsize

        for p in prices:
            min_profit = min(min_profit, p)
            ans = max(ans, p - min_profit)

        return ans
