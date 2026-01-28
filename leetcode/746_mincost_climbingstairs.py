class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = len(cost)
        dp = [0] * (stairs+1)
        # dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, stairs+1):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])

        return dp[-1]
        