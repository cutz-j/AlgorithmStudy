# https://leetcode.com/problems/running-sum-of-1d-array/
#solution
"""
Runtime Memory
60 ms   13.9 MB
"""
class Solution:
    def runningSum(self, nums):
        output =[]
        index =0
        for index,elem in enumerate(nums):
            if index==0:
                output.append(elem)
                index+=1
            else:
                output.append(output[-1]+elem)
                
        return output

#solution
"""
Runtime Memory
92 ms   13.8 MB
"""
class Solution:
    def runningSum(self, nums):
                
        return [sum(nums[:x+1]) for x in range(len(nums))]