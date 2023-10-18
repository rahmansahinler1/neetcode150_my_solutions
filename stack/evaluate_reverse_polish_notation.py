"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def is_integer(num_str):
            try:
                int(num_str)
                return True
            except ValueError:
                return False
            
        stack = []
        for value in tokens:
            if is_integer(value):
                stack.append(int(value))
            else:
                processed = 0
                if value == '*':
                    processed = stack[-2] * stack[-1]
                elif value == '/':
                    processed = int(stack[-2] / stack[-1])
                elif value == '+':
                    processed = stack[-2] + stack[-1]
                else:
                    processed = stack[-2] - stack[-1]
                    
                for _ in range(2):
                    stack.pop()
                stack.append(processed)
        
        return stack[0]

tokens = ["2","1","+","3","*"]
tokens1 = ["4","13","5","/","+"]
tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()

print(sol.evalRPN(tokens))
print(sol.evalRPN(tokens1))
print(sol.evalRPN(tokens2))
