# Arrays in Python: Buy and Sell Stock
# When to buy, when to sell?
#     0    5    0    20   0    10   30   0    25   20
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time complexity : O(n^2)
# Space complexity: constant


def buy_and_sell_once(A):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


print(buy_and_sell_once(A))

# Time complexity : O(n)
# Space complexity: constant


def buy_and_sell_once_2(A):
    max_profit = 0
    min_price = A[0]
    for price in A:
        min_price = min(price, min_price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit


print(buy_and_sell_once_2(A))
