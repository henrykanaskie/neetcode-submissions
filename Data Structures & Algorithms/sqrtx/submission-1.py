class Solution:
    def mySqrt(self, x: int) -> int:
        alpha = .1
        if x == 0 or x == 1:
            return x
        xn = guess = x/2.0
        dif = float("inf")
        while abs(dif) > alpha:
            guess = .5*(xn + (x/xn))
            dif = xn - guess
            xn = guess
        
        return math.trunc(guess)
            