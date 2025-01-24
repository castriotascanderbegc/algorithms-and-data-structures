"""
    Q: Stock Price Fluctuation
    You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the
    stock at that timestamp.

    Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be
    incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

    Design an algorithm that:
        Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
        Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp
        recorded.
        Finds the maximum price the stock has been based on the current records.
        Finds the minimum price the stock has been based on the current records.
    
    Implement the StockPrice class:
        StockPrice() Initializes the object with no price records.
        void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
        int current() Returns the latest price of the stock.
        int maximum() Returns the maximum price of the stock.
        int minimum() Returns the minimum price of the stock.
"""

from collections import defaultdict
from sortedcontainers import SortedList

class StockPrice:
    """
        Using a SortedList, we can benefit from addition/deletion in O(log n) time
    """
    def __init__(self):
        # we use a Hash Table to keep track of (timestamp, price) pairs
        self.stock_records = defaultdict(int)
        # we use a SortedList to efficiently retrieve max and min
        self.sorted_list = SortedList()
        # keep track of the latest timestmap to efficiently retrieve current price
        self.last = 0

    # Time Complexity: T(n) = O(log n) both deletion/addition from a SortedList takes O(log n)
    def update(self, timestamp: int, price: int) -> None:
        """ Updates the price of the stock at the given timestamp. """
        # first check if given timestamp is already present in our map
        if timestamp in self.stock_records:
            # if so, remove old price from the SortedList
            self.sorted_list.remove(self.stock_records[timestamp])
        
        # insert given price in the map
        self.stock_records[timestamp] = price
        # add new price to the SortedList
        self.sorted_list.add(price)

        # update last timestamp
        self.last = max(self.last, timestamp)
    
    # Time Complexity: T(n) = O(1)
    def current(self) -> int:
        """ Returns the latest price of the stock. """
        return self.stock_records[self.last]

    # Time Complexity: T(n) = O(1)
    def maximum(self) -> int:
        """ Returns the maximum price of the stock. """
        return self.sorted_list[-1]

    # Time Complexity: T(n) = O(1)
    def minimum(self) -> int:
        """ Returns the minimum price of the stock. """ 
        return self.sorted_list[0]

if __name__ == "__main__":
    # Your StockPrice object will be instantiated and called as such:
    obj = StockPrice()
    obj.update(4,5)
    param_2 = obj.current()
    param_3 = obj.maximum()
    param_4 = obj.minimum()