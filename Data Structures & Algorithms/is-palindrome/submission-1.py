import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        stri = s.replace(" ", "")
        low = stri.lower()
        for char in low:
            if not char.isalnum():
                low = low.replace(char, '')

        rlow = low[::-1]
        print(low, rlow)
        if low == rlow:
            return True
        return False
