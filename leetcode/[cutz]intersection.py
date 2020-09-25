import sys

sys.setrecursionlimit(10000000)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1, len2 = len(nums1), len(nums2)
        ans = []
        if len1 >= len2:
            self.arr = sorted(nums1)
            for target in set(nums2):
                self.switch = False
                self.bsearch(0, len1 - 1, target)
                if self.switch:
                    ans.append(target)

        else:
            self.arr = sorted(nums2)
            for target in set(nums1):
                self.switch = False
                self.bsearch(0, len2 - 1, target)
                if self.switch:
                    ans.append(target)

        return set(ans)

    def bsearch(self, left, right, target):
        if left > right:
            return 0

        mid = left + (right - left) // 2
        if self.arr[mid] > target:
            self.bsearch(left, mid - 1, target)
        elif self.arr[mid] < target:
            self.bsearch(mid + 1, right, target)
        else:
            self.switch = True
            return




