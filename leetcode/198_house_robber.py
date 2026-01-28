class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            # 1. 현재 집을 털고 2칸 전으로 이동: nums[i] + dfs(i-2)
            # 2. 현재 집을 안 털고 1칸 전으로 이동: dfs(i-1)
            res = max(dfs(i - 1), nums[i] + dfs(i - 2))
            
            memo[i] = res
            return res

        return dfs(len(nums) - 1)