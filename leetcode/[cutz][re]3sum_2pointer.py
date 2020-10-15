from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()  # left, right

        for i in range(len(nums) - 2):
            # 중복값 건너띄기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격 좁히며 sum
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                # 작은 경우
                if sum_val < 0:
                    left += 1
                # 큰 경우
                elif sum_val > 0:
                    right -= 1
                else:
                    # 0
                    results.append((nums[i], nums[left], nums[right]))

                    # 중복 모두 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
