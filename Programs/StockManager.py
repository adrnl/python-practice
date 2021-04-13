# Best Time to Buy and Sell Stock with Transaction Fee:
# (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day,
# and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions
# as you like, but you need to pay the transaction fee for each transaction.
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).
#
# Constraints:
#
# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104

buy if day 0 < day 1
sell if day 1 > day 2

def maxProfit(prices: List[int], fee: int) -> int:
    length = len(prices)
    profit = 0
    if length < 2 or fee < 0:
        return profit

    min = prices[0]
    for i in range(1, length):
        if prices[i] < min:
            min = prices[i]

        elif prices[i] > min + fee:
            profit += prices[i] - fee - min
            min = prices[i] - fee


prices = [1,3,2,8,4,9]
fee = 2
answer = 8

if maxProfit(prices, fee) != output:
    print("fail")
else:
    print("pass")

prices = [1,3,7,5,10,3]
fee = 3
answer = 6

if maxProfit(prices, fee) != output:
    print("fail")
else:
    print("pass")


# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# Example 2:
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6