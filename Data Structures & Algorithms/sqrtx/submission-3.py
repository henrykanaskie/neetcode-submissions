class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        alpha = .00001
        xn = x
        dif = float("inf")

        while abs(dif) > alpha:
            guess = .5*(xn + (x/xn))
            dif = xn - guess
            xn = guess
    
        return math.trunc(guess)
            