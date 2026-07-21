class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b = 0, len(matrix[0]) -1, 0, len(matrix) - 1
        res = []
        i = 0
        j = 0
        els = (len(matrix) * len(matrix[0]))
        while len(res) < els:
            for j in range(l, r + 1):
                res.append(matrix[t][j])
            t += 1
            for i in range(t,b + 1):
                res.append(matrix[i][r]) 
            r -= 1
            if not (l <= r and t <= b):
                break
            for j in range(r, l - 1, -1):
                res.append(matrix[b][j])
            b -= 1
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1


        return res