class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(count1, count2):
            if count1 == count2 == n:
                res.append("".join(stack))
            if count1 < n:
                stack.append("(")
                backtrack(count1 + 1, count2)
                stack.pop()
            if count2 < count1:
                stack.append(")")
                backtrack(count1, count2 + 1)
                stack.pop()
            
        backtrack(0,0)
        return res
            
