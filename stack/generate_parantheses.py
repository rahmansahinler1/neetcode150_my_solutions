"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = {key:[] for key in range(n*2)}
        if stack:
            stack[0] = ['(']
        else:
            return []
        
        for i in range(1, n*2):
            prev_state = stack[i - 1]
            for value in prev_state:
                open_count = value.count('(')
                close_count = value.count(')')
                if open_count - close_count > 0:
                    stack[i].append(value + ')')
                if open_count < n:
                    stack[i].append(value + '(')
                
        return stack[list(stack)[-1]]
n = 3
n1 = 1
n2 = 0
n3 = 5

sol = Solution()

print(sol.generateParenthesis(n))
print(sol.generateParenthesis(n1))
print(sol.generateParenthesis(n2))
print(sol.generateParenthesis(n3))
