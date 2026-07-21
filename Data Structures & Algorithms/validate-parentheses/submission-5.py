class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        if len(s) % 2 != 0:
            return False
        opens = {'(', '{', '['}
        closes = {')', '}', ']'}
        if s[0] in closes:
            return False
        for char in s:
            if char in opens:
                stack.append(char)
            if char in closes:
                if stack:
                    if char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ")" and stack[-1] == "(":
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
        if len(stack) > 0:
            return False
        else:
            return True