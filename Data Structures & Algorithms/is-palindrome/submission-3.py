class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s =s.lower()
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c
        while i < len(cleaned) // 2:
            if cleaned[i] != cleaned[-i - 1]:
                return False
            i += 1
        
        return True