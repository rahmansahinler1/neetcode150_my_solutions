"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(max_profit, profit)
                r += 1
            else:
                l = r
                r += 1                
        return max_profit
    
prices = [7,1,5,3,6,4]
prices1 = [7,6,4,3,1]

sol = Solution()

print(sol.maxProfit(prices))
print(sol.maxProfit(prices1))
