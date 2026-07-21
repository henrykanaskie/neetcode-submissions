class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp1, mp2 = [0] * 26, [0] * 26
        for c in s:
            mp1[ord(c) - ord('a')] += 1
        for c in t:
            mp2[ord(c) - ord('a')] += 1
        
        return mp1 == mp2