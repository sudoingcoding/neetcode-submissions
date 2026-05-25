class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buy,sell=0,1
        n=len(prices)
        while sell < n:
            profit=prices[sell]-prices[buy]
            if profit<0:
                buy=sell
            elif profit>maxProfit:
                maxProfit=profit
            sell+=1
        return maxProfit