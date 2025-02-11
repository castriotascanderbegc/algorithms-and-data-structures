"""
    Given n items, each with a category and a price, 
    the challenge is to figure out the sales sequence that results in the highest total profit. 
    
    The profit for selling an item is calculated as the product of its price and the count of distinct categories 
    sold before that item, including its own category.

    Example:
    
    Number of Items (n): 4
    Categories (category): [3, 1, 2, 3]
    Prices (price): [2, 1, 4, 4]
    
    One possible optimal order for selling these items is:

    Sell the 2nd item (category[2] = 1, price[2] = 1):
    Profit = 1 * 1 = 1
    (Only 1 unique category has been sold.)

    Sell the 1st item (category[1] = 3, price[1] = 2):
    Profit = 2 * 2 = 4
    (Now, 2 unique categories have been sold.)

    Sell the 3rd item (category[3] = 2, price[3] = 4):
    Profit = 4 * 3 = 12
    (Three unique categories have been sold.)

    Sell the 4th item (category[4] = 3, price[4] = 4):
    Profit = 4 * 3 = 12
    (The number of unique categories remains 3.)

    Total Profit = 1 + 4 + 12 + 12 = 29

"""

from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], categories: List[int]) -> int:
        # check if prices or categories is empty
        if not prices or not categories:
            return 0
        
        # first store prices and categories in a list (of tuples)
        items = list(zip(prices, categories))

        # sort the items in ascending order of their price, min to max
        items = sorted(items, key=lambda x: -x[0])

        # define a set to keep track of each unique cateogry sold
        unique_categories = set()

        # initialize maximum profit to be returned
        max_profit = 0

        for price, category in items:
            # add the current category to the set of unique categories
            unique_categories.add(category)

            # calculate the current profit for selling the current item
            profit = price * len(unique_categories)

            # update the maximum profit
            max_profit += profit
        
        return max_profit
