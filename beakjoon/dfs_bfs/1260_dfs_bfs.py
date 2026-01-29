import sys
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for nxt in range(1, n + 1):
        if not visited[nxt] and graph[idx][nxt]:
            dfs(nxt)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for nxt in range(1, n + 1):
            if not visited[nxt] and graph[cur][nxt]:
                visited[nxt] = True
                q.append(nxt)



input = sys.stdin.readline
# 정점의 개수 n, 간선의 개수 m, 탐색 시작 정점 v
n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 간선 정보를 그래프로 저장
    graph[a][b] = True
    graph[b][a] = True

# DFS
dfs(v)
print()

# BFS
visited = [False] * (n + 1)
visited[v] = True
q = [v]
bfs()