from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if n == 1:
            return 1

        q = deque([(0, 0, 1)])

        while q:
            b, r, cnt = q.popleft()
            if b == n - 1 and r == n - 1:
                return cnt
            
            # 8 directions
            for db, dr in [(1,1), (0,1), (1,0), (-1,-1), (-1,0), (0,-1), (-1,1), (1, -1)]:
                nb, nr = b + db, r + dr

                if 0 <= nb < n and 0 <= nr < n and grid[nb][nr] == 0:
                    grid[nb][nr] = 1
                    q.append((nb, nr, cnt+1))
        return -1