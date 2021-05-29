"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
def buy_and_sell_stocks(prices):
    min_price = float("inf")
    max_price = 0
    for price in prices:
        min_price = min(min_price,price) 
        max_price = max(max_price, price - min_price)
        # min -->∞ 7 1 1 1 1 1
        # max -->0 0 0 4 2 5 3 --> max  is 5
                
    return max_price

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(buy_and_sell_stocks(prices))