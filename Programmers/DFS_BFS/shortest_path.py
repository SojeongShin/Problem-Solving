from collections import deque
def solution(maps):

    n = len(maps)    # 세로 row
    m = len(maps[0]) # 가로 col

    if n == 1 and m == 1:
        return 1

    q = deque([(0, 0, 1)])
    maps[0][0] = 0

    while q:
        r, c, cnt = q.popleft()
        if r == n - 1 and c == m - 1:
            return cnt

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] = 0
                q.append((nr, nc, cnt + 1))

    return -1
