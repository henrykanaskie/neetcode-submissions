class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            if digits[-1 - i] + carry > 9:
                digits[-1 - i] = 0
                carry = 1
            else:
                digits[-1-i] = digits[-1 - i] + carry
                carry = 0
                return digits
                
        return [1] + digits
        
        