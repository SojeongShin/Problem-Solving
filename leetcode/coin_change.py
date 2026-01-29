class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = [False] * (amount + 1)
        q = [(amount, 0)]
        visited[amount] = True

        while q:
            curr_remain, count = q.pop(0)
            for coin in coins:
                next_remain = curr_remain - coin

                if next_remain == 0:
                    return count + 1

                if next_remain > 0 and not visited[next_remain]:
                    visited[next_remain] = True
                    q.append((next_remain, count + 1))
        return -1