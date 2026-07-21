class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/","*"}
        for token in tokens:
            if token in operators:
                x2 = stack.pop()
                x1 = stack.pop()
                expr = x1 + token + x2
                val = eval(expr)
                stack.append(str(int(val)))
            else:
                stack.append(token)
        
        return int(stack[0])

                