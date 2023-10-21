"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []  # [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append((temp, i))
        return answer
                
temperatures = [73,74,75,71,69,72,76,73]
temperatures1 = [30,40,50,60]
temperatures2 = [30,60,90]

sol = Solution()

print(sol.dailyTemperatures(temperatures))
print(sol.dailyTemperatures(temperatures1))
print(sol.dailyTemperatures(temperatures2))
