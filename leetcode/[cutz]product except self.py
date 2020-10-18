from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prior / posterior
        out = []
        ans = 1
        for i in range(len(nums)):
            out.append(ans)
            ans *= nums[i]

        ans = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= ans
            ans *= nums[i]

        return out


