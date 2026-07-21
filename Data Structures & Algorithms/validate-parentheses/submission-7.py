class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["-"]
        for c in s:
            if c == "}":
                top = stack.pop()
                if top != "{":
                    return False
            elif c == "]":
                top = stack.pop()
                if top != "[":
                    return False
            elif c == ")":
                top = stack.pop()
                if top != "(":
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 1 else False
