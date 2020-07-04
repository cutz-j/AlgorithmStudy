# https://leetcode.com/problems/two-sum/
# Solution
"""
Runtime Memory

132 ms	13.4 MB
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # delete over value
        x = 0
        y = 1
        last =len(nums)-1
        temp_nums = sorted(nums)
        while True:
            if temp_nums[x]+temp_nums[y] >int(target):
                x+=1
                y=x+1
            elif temp_nums[x]+temp_nums[y] == int(target):
                if temp_nums[x]==temp_nums[y]:
                    return [index for (index, number) in enumerate(nums) if number == temp_nums[x]]
                else:
                    return(nums.index(temp_nums[x]),nums.index(temp_nums[y]))
            elif y==last:
                x+=1
                y=x+1
            else:
                y+=1


# Solution
"""
Runtime Memory

68 ms	13.5 MB
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # delete over value
        x = 0
        y = 1
        last =len(nums)-1
        temp_nums = sorted(nums)
        while True:
            real_x =temp_nums[x]
            real_y =temp_nums[y]
            if real_x+real_y >int(target):
                x+=1
                y=x+1
            elif real_x+real_y == int(target):
                if real_x==real_y:
                    return [index for (index, number) in enumerate(nums) if number == real_x]
                else:
                    return(nums.index(real_x),nums.index(real_y))
            elif y==last:
                x+=1
                y=x+1
            else:
                y+=1