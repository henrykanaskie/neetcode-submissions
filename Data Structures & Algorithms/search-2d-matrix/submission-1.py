class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bottom, top = 0, len(matrix) -1

        while bottom <= top:
            mid = bottom + (top-bottom) // 2
            if target < matrix[mid][0]:
                top = mid - 1
            elif target > matrix[mid][-1]:
                bottom = mid + 1
            else:
                
                break

      
        

        l, r = 0, len(matrix[mid]) - 1

        while l <= r:
            m = l + (r-l)//2
            if target < matrix[mid][m]:
                r = m -1
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                return True
        
        return False
