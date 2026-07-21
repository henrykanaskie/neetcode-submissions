class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = []
        star_stack = []
        for i, c in enumerate(s):
            if c == '*':
                star_stack.append(i)
            elif c == '(':
                paren_stack.append(i)
            else:
                if paren_stack:
                    paren_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            
        while paren_stack:
            if star_stack:
                if star_stack[-1] > paren_stack[-1]:
                    paren_stack.pop()
                    star_stack.pop()
                else:
                    return False
            else:
                return False

        return True