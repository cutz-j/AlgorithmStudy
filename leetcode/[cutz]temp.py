class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                # stack condition: next element is warmmer
                top = stack.pop()
                answer[top] = i - top
            stack.append(i)

        # while stack:
        #     top = stack.pop()
        #     answer[top] = len(T) - 1 - top

        return answer
