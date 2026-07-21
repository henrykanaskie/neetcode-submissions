class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def happy(n):
            value = 0
            str_int = str(n)
            for dig in str_int:
                value += int(dig) ** 2
            
            
            if value == 1:
                return True
            if value in seen:
                return False
            seen.add(value)
            return happy(value)
        
        return happy(n)