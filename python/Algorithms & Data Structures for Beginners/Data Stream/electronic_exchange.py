"""
    Q: Electronic Exchange
    You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and 
    its traded volume of stocks. Eg: {name: vodafone, volume: 20}. 
    
    What data structure will you maintain if:
        You have to tell top k products traded by volume at end of day.
        You have to tell top k products traded by volume throughout the day.
"""

from heapq import heappush, heappop, heapify, nlargest
from collections import defaultdict
from typing import List, Tuple

class ElectronicExchange:
    def __init__(self, k: int):
        self.k = k
        self.product_volume_map = defaultdict(int)      # to store cumulative trading volumes for each product
        self.top_k_heap = []                            # to store top K products based on their traded volume


    def update(self, product: str, volume: int):
        # update the cumulative trading volume for the product
        self.product_volume_map[product] += volume

        # update the top K heap for dynamic maintenance
        for i, (vol, prod) in enumerate(self.top_k_heap):
            if prod == product:
                # remove the product from the heap
                self.top_k_heap.pop(i)
                # heapify the heap again after removal
                heapify(self.top_k_heap)
                break
        
        # add the product to the heap if its volume qualifies for the top K
        heappush(self.top_k_heap, (self.product_volume_map[product], product))

        # ensure the heap size does not exceed K
        if len(self.top_k_heap) > self.k:
            heappop(self.top_k_heap)

    def topK(self) -> List[Tuple[int, str]]:
        """
        Top K Products Traded by Volume Throughout the Day

        Key Characteristics:
            Query for top K products can be made at any time during the day
            Needs to efficiently handle updates and frequent queries
        
        Optimal Data Structure:
            a hashmap (dictionary) to store cumulative trading volumes, combined with a balanced binary heap (min-heap) 
            to maintain the top K products dynamically.
        
        Design:
            1. Use a dict to store cumulative trading volumes for each product
                Key: Product name
                Value: Cumulative Trading volume
            2. Maintain a min-heap of size K to store the top K products based on their traded volume.
                Each element of the min-heap is a tuple of product name and its traded volume.
                The heap is maintained such that the product with the least traded volume is at the root.
            3. On each update
                Check if the product is already in the dictionary
                    If yes, remove it and reintroduce it with the updated volume
                    If no, add it to the heap if its volume qualifies for the top K (remove the smallest element if the heap size exceeds k).
            4. To retrieve the top K products, simply return the elements of the heaps sorted. 
        
        Time Complexity:
            Update: O(log k) per tick (heap insertion/deletion)
            Top K query: O(k * log k) if sorting is required, O(k) oterhwise

        """

        # Return the top k elements (sorted in descending order)
        return sorted(self.top_k_heap, key=lambda x: -x[0])

    def topK_EOD(self) -> List[Tuple[int, str]]:
        """
        Top K Products Traded by Volume at End of Day

        Key Characteristics:
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

        # Use nlargest for final end-of-day query
        return nlargest(self.k, self.product_volume_map.items(), key=lambda x: x[1])


if __name__ == "__main__":
    exchange = ElectronicExchange(3)

    # Incoming ticks
    ticks = [
        ("vodafone", 20), ("vodafone", 30), ("ibm", 50),
        ("google", 40), ("ibm", 20), ("apple", 70),
        ("apple", 30), ("google", 50)
    ]

    for product, volume in ticks:
        exchange.update(product, volume)

    print("Top K throughout the day:", exchange.topK())
    print("Top K at the end of the day:", exchange.topK_EOD())
