class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            ab = (a >> i) & 1
            bb = (b >> i) & 1
            curb = ab ^ bb ^ carry
            carry = (ab + bb + carry) >= 2
            if curb:
                res |= (1 << i)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res