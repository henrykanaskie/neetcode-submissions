class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def mult(num1, num2):
            if num1 == "0" or num2 == "0":
                return 0
            product = num1 * num2
            return product

        res = 0
        for i in range(len(num1)):
            prod = 0
            for j in range(len(num2)):
                mul = mult(int(num1[-1-i]), int(num2[-1-j]))
                prod += mul * pow(10, j)
            
            res += prod * pow(10, i)

        return str(res)

             