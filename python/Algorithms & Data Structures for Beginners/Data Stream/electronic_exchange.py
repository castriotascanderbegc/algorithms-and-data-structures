"""
    Q: Electronic Exchange
    You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and 
    its traded volume of stocks. Eg: {name: vodafone, volume: 20}. 
    
    What data structure will you maintain if:
        You have to tell top k products traded by volume at end of day.
        You have to tell top k products traded by volume throughout the day.
"""

import heapq

class Exchange:
    def __init__(self):
        pass

    def topK(self, k: int):
        pass

    def topK_EOD(self, k: int):
        """
        Top K Products Traded by Volume at End of Day

        Key Characteristics
            Updates are made frequently  throughout the day
            Query of top K is only made at the end of the day
        
        An optimal data structure:
            A hashmap (dictionary) to store cumulative trading volumes, combined with a heap (priority queue)
            to fetch the top K products
        
        Desgign:
            1. Use a dict to store cumulative trading volumes for each product
                Key: Product name
                Value: Cumulative Trading volume
            2. At the end of the day, we can use a heap with nlargest method to efficiently retrieve the
               top K products based on their traded volume.
        
        Time Complexity:
            Update (during the day): with a dictionary it takes O(1) on average per tick
            Top K query (end of the day): with a heap it takes O(n · log k) where n is the number of products, and k those to be fetched
        """
        return heapq.nlargest(k, self.stockmap.items(), key=lambda x: x[1])