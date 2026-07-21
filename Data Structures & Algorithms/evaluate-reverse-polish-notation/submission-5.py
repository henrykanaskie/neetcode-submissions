class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}
        for token in tokens:
            print(stack)
            if token in operators:
                int2 = stack.pop()
                int1 = stack.pop()
                if token == "+":
                    stack.append(int1 + int2)
                if token == "-":
                    stack.append(int1 - int2)
                if token == "*":
                    stack.append(int1 * int2)
                if token == "/":
                    stack.append(int(int1 / int2))
            else:
                stack.append(int(token))
        
        return stack[-1]