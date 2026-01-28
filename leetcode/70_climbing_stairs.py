class Solution:
    def climbStairs(self, n: int) -> int:
        # l[s] = s칸 남았을 때 경우의 수
        l = [-1] * (n + 1)

        def dfs(s: int) -> int:
            if s < 0:
                return 0
            if s == 0:
                return 1
            if l[s] != -1:
                return l[s]

            l[s] = dfs(s - 1) + dfs(s - 2)
            return l[s]

        return dfs(n)
