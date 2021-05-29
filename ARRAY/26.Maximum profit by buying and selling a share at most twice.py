"""
Maximum profit by buying and selling a share at most twice

In daily share trading, a buyer buys shares in the morning and sells them on the same day. 
If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Sell->buy->sell->buy). 
Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

Examples: 

Input:   price[] = {10, 22, 5, 75, 65, 80}
Output:  87
Trader earns 87 as sum of 12, 75 
Buy at 10, sell at 22, 
Buy at 5 and sell at 80

Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
Output:  100
Trader earns 100 as sum of 28 and 72
Buy at price 2, sell at 30, buy at 8 and sell at 80

Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
Output:  72
Buy at price 8 and sell at 80.

Input:   price[] = {90, 80, 70, 60, 50}
Output:  0
Not possible to earn.

"""
def max_profit_earn(price):
    
    #keep track of max number
    profit = 0

    #Initialize local minimum to 0 index
    j =  0 

    #start from second element
    for i in range(1, len(price)):
        #update local minimum if decreassing sequence is found 
        if price[i - 1] > price[i]: #price[i-1] --> 10 22 5 75 65  price[i]->22 5 75 65 80
            j = i 
        
        # (`previous <= current > next`)
        if price[i - 1] <= price[i] and (i + 1 == len(price) or price[i] > price[i + 1]):
            profit += (price[i]-price[j])
            print(f"Buy on day {j + 1} and sell on day {i + 1}")

    return profit
if  __name__ == "__main__":
    price = [10, 22, 5, 75, 65, 80]
    print(max_profit_earn(price))