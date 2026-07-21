class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        t = sorted(t)
        s = sorted(s)
        return s == t