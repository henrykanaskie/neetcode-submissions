class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        numstack = []
        operations = {"+", "-", "*", "/"}
        if tokens[0] in operations:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            
            if token not in operations:
                numstack.append(int(token))
            else:
                if token == "+":
                    print(numstack)
                    numstack[-2] = numstack[-2] + numstack[-1]
                    numstack.pop()
                elif token == "/":
                    print(numstack)
                    numstack[-2] = int(numstack[-2] / numstack[-1])
                    numstack.pop()
                elif token == "*":
                    print(numstack)
                    numstack[-2] = numstack[-2] * numstack[-1]
                    numstack.pop()
                elif token == "-":
                    print(numstack)
                    numstack[-2] = numstack[-2] - numstack[-1]
                    numstack.pop()
        return numstack[0]