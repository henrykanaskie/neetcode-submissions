class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        mins = 0
        fresh = 0
        q = deque()

        def checkfruit(r, c):
            nonlocal fresh
            if r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            fresh -= 1
            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                checkfruit(r + 1, c)
                checkfruit(r - 1, c)
                checkfruit(r, c + 1)
                checkfruit(r, c - 1)
            mins += 1
        
        return mins if fresh == 0 else -1
            
           