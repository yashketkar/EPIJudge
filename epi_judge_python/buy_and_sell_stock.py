from test_framework import generic_test


# 121. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 5.6
def buy_and_sell_stock_once(prices):
    max_profit, min_price = 0, float('inf')
    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        if i>0 and prices[i]<=prices[i-1]:
            continue
        max_profit = max(prices[i] - min_price, max_profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
