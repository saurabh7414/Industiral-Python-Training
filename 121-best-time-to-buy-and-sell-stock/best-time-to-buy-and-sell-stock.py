class Solution(object):
    def maxProfit(self, prices):
        buyingprice=prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sellingprice = prices[i]
            if sellingprice > buyingprice:
                profit = max(profit, (sellingprice - buyingprice))
            if buyingprice > sellingprice:
                buyingprice = prices[i]
        return profit        