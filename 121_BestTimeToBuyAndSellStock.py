
def maxProfit(prices: list[int]) -> int:

        L, R = 0, 1
        max_profit = 0

        while R < len(prices):
            profit = prices[R] - prices[L]
            if profit < 0:
                L += 1
                if L == R:
                    R += 1
            else:
                R += 1
                max_profit = max(max_profit, profit)

        return max_profit

print(maxProfit([7,1,5,3,6,4]))
# Output should be 5

print(maxProfit([7,6,4,3,1]))
# Output should be 0
