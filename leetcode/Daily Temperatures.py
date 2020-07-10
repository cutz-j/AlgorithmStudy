# https://leetcode.com/problems/daily-temperatures/
# Solution
"""
Runtime Memory

processing
"""
class Solution:
    def dailyTemperatures(self, T):
        temp_set = sorted(list(set(T)))
        temp_map=[[0]*len(temp_set)]*len(T)
        for column,element in enumerate(T):
            for index,elem in enumerate(temp_set):
                if element<elem:
                    temp_map[column]= [0]*index+ [1]*(len(temp_map)-index)
                    break
        answer =[]
        print(temp_map)
        for index,element in enumerate(T[:len(T)-2]):
            for inner_index,elem in enumerate(T[index+1::len(T)-2]):
                if elem ==1:
                    answer.append(inner_index+1)
                    break
                elif inner_index == len(T[index+1:])-1:
                    answer.append(0)
        return answer
   

class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
