class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(amount):
            if amount == 0:
                return 0
            
            res = 10**9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            
            return res
        
        minCoins = dfs(amount)
        if minCoins == 10**9:
            return -1
        else:
            return minCoins