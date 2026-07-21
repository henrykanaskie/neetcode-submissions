class Solution:
    def myPow(self, x: float, n: int) -> float:
        def help(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = help(x * x, abs(n)//2)
            if n % 2:
                res = res * x
            return res

        res = help(x, abs(n))
        if n >= 0:
            return res
        else:
            return 1/res

            

