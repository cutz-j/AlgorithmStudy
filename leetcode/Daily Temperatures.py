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