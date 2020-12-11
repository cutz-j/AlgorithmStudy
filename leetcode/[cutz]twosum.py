class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(N)
        for idx, t in enumerate(numbers):
            targ = target - t
            # O(logN)
            left, right = 0, len(numbers) - 1
            ans = []
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < targ:
                    left = mid + 1
                elif numbers[mid] > targ:
                    right = mid - 1
                else:
                    if mid != idx:
                        ans.append(idx + 1)
                        ans.append(mid + 1)
                        break
                    else:
                        left = mid + 1
            if ans:
                break
        return ans
