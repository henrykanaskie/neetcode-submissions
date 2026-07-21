class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        counts = {}
        countst = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for char in t:
            if char in countst:
                countst[char] += 1
            else:
                countst[char] = 1

        if counts == countst:
            return True

        return False