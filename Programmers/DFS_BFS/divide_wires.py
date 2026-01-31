def solution(n, wires):
    answer = n

    adj = [[] for _ in range(n+1)]
    for a, b in wires:
        adj[a].append(b)
        adj[b].append(a)

    def dfs(curr, prev):
        nonlocal answer
        count = 1
        for neighbor in adj[curr]:
            if neighbor != prev:
                subtree_size = dfs(neighbor, curr)
                diff = abs(subtree_size - (n - subtree_size))
                answer = min(answer, diff)

                count += subtree_size
        return count

    dfs(1, -1)


    return answer
