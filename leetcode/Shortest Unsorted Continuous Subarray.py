# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Solution
"""
Runtime Memory

300 ms	15.1 MB	
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        temp_nums = sorted(nums)
        temp_output =[0 if temp_nums[index]==element else 1 for index,element in enumerate(nums)]
        if sum(temp_output)==0:
            return 0
        else:
            start=temp_output.index(1)+1
            for index, element in enumerate(reversed(temp_output)):
                if element:
                    end = len(temp_output)-index
                    break
            return end-start+1
                
# Solution
"""
Runtime Memory

304 ms	15 MB
"""        
class Solution:
    def findUnsortedSubarray(self, nums):
        temp_nums = sorted(nums)
        temp_output =[0 if temp_nums[index]==element else 1 for index,element in enumerate(nums)]
        if sum(temp_output)==0:
            return 0
        else:
            start=temp_output.index(1)+1
            end = len(temp_output)-list(reversed(temp_output)).index(1)
            return end-start+1





# Solution
"""
Runtime Memory

Should be done later
"""
class Solution:
    def sort_checker(self,arrays):
        bucket =[-1,-1]
        for index in range(len(arrays)-1):
            if arrays[index]>arrays[index+1]:
                bucket[0] = index
                break
        for index in range(len(arrays)-1,1,-1):
            if arrays[index]<arrays[index-1]:
                bucket[1] = index
                break
        return bucket
    
    def findUnsortedSubarray(self, nums):
        # initial area split
        init =sort_checker(nums)
        if sum(init)==-2:
            return 0
        else:
            #partial 
            temp = sorted(nums[init[0]:init[1]+1])
            total = nums[:init[0]]+temp+nums[init[1]+1:]
            init = sort_checker(nums)
            if sum(init)==-2:
                return =
            
            
                
            
        
            