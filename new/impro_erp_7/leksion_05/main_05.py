"""U3"""
"""
Build a function that takes the prices of
products in a store as a list parameter
and returns the product with the highest price.
"""


def max_price(prices: list):
    max = prices[0]
    for price in prices:
        if price > max:
            max = price
    return max


lst = [10, 7, 14, 6]
print(max_price(lst))
