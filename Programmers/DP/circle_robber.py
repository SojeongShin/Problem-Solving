def solution(money):
    
    n = len(money)
    case1 = linear_robber(money[:-1])
    case2 = linear_robber(money[1:])
    
    return max(case1, case2)

def linear_robber(nums):
    n = len(nums)
    # if n == 0: return 0
    # if n == 1: return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    return dp[-1]