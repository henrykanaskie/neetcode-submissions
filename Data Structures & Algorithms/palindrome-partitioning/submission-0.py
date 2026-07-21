class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def backtrack(i, j):
            if j >= len(s):
                if i == j:
                    res.append(subset.copy())
                return

            if self.isPal(s[i:j+1]):
                subset.append(s[i:j+1])
                backtrack(j + 1, j + 1)
                subset.pop()
            
            backtrack(i, j + 1)
        
        backtrack(0,0)
        return res



    def isPal(self, s:str) -> bool:
        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return False
            
        return True