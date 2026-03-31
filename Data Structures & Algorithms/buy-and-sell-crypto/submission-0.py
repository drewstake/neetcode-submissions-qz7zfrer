class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        buy = 0 # index

        for i, price in enumerate(prices):
            high = max(high, price - prices[buy])
            if price < prices[buy]:
                buy = i
        
        return high
