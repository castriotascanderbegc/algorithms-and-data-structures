"""
    Q: 
        You have a stream of Stock ticker and volumen coming in from a data stream.
        You need to design a function which returns the K most voluminous stocks, i.e. K largest stocks

    Ex: 
        Input Stream:
        MSFT|400 IBM|1000 AAPL|500 AAPL|600 NFLX|1000 AMZN|700 GOGL|300


        Result:
        If there are two stock tickers with similar volume, you can return any of them in any order.


        Return K = 4
        AAPL|1100 NFLX|1000 IBM|1000 AMZN|700
        OR
        AAPL|1100 IBM|1000 NFLX|1000 AMZN|700


        You can return it as a list of tuple:
        [(APPL, 1100), (IBM,1000).... ]
        AAPL, IBM
"""
from collections import defaultdict     # a defaultdict allows to initialize a dictionary with a default value
from sortedcontainers import SortedDict # a SortedDict allows to maintain the keys in ascending order within the dictionary

class StockTicker:
    def __init__(self):
        # for each ticker we will store the volume
        self.stockmap = defaultdict(int)

        # for each volume we will have a list of tickers. Therefore, tickers with the same volume will be contained in a list
        self.sortedStockMap = SortedDict()
    
    # Time Complexity: T(n) = O(m * log q) where m is the number of stocks in the given stream and q is the number of unique volumes
    def insert(self, stream: str):
        # convert the incoming stream to a list
        stream_list = stream.split(" ")
        # iterate over each stock and volume, this takes O(m) where m is the number of stocks in the given stream
        for stream in stream_list:
            # retrieve the ticker and volume
            ticker, volume = stream.split("|")
            # convert the volume to int
            volume = int(volume)
            # if the ticker is already in the stockmap, update the volume
            if ticker in self.stockmap:
                # get the previous volume
                previous_volume = self.stockmap[ticker]

                # remove the previous volume from the sortedStockMap
                self.sortedStockMap[-previous_volume].remove(ticker)

                # calculate the new volume
                new_volume = previous_volume + volume
                # update the stockmap
                self.stockmap[ticker] = new_volume

                # add the new volume to the sortedStockMap, this takes O(log(n)) for checking and inserting into the SortedDict
                if -new_volume in self.sortedStockMap:
                    self.sortedStockMap[-new_volume].append(ticker)
                else:
                    self.sortedStockMap[-new_volume] = [ticker]
            else:
                self.stockmap[ticker] = volume
                if -volume in self.sortedStockMap:
                    self.sortedStockMap[-volume].append(ticker)
                else:
                    self.sortedStockMap[-volume] = [ticker]
    
    # Time Complexity: T(n) = O(k)
    # Overall this method takes O(k) time complexity as it stops when the result list is equal to k
    def getKMostVoluminousStocks(self, k: int):
        # initialize the result list
        result = []
        # iterate over the sortedStockMap, takes O(q) where q is the number of unique volumes
        for volume, tickers in self.sortedStockMap.items():
            # iterate over the tickers
            # takes O(p) where p is the number of tickers with the same volume
            for ticker in tickers:
                # append the ticker and volume to the result list
                result.append((ticker, -volume))
                # if the result list is equal to k, return the result
                if len(result) == k:
                    return result
        # return the result
        return result


# test the StockTicker class
if __name__ == "__main__":
    stock_ticker = StockTicker()
    stream = "MSFT|400 IBM|1000 AAPL|500 AAPL|600 NFLX|1000 AMZN|700 GOGL|300"
    stock_ticker.insert(stream)
    stock_ticker.insert("AAPL|600")
    stock_ticker.insert("AMZN|800")

    print(stock_ticker.getKMostVoluminousStocks(4)) # [('IBM', 1000), ('AAPL', 1100), ('NFLX', 1000), ('AMZN', 700)]




"""
SortedDict in Python, provided by the sortedcontainers library, is a dictionary-like data structure that maintains its keys in sorted order (ascending). Here's how it works:
Key Features:
    Sorted Keys:
        Unlike regular dictionaries, SortedDict keeps its keys in sorted order, allowing efficient access and operations based on key ordering.
    Efficient Operations:
        It provides efficient operations like:
            Insertion: Inserting a new key-value pair maintains the sorted order of keys.
            Lookup: Retrieving a value by key is efficient due to the sorted nature of the keys.
            Iteration: Iterating over the dictionary yields key-value pairs in sorted order.
            Slicing: You can efficiently access a range of key-value pairs based on their sorted order.
    Underlying Implementation:
        Internally, SortedDict uses a combination of a dictionary and a sorted list. The dictionary stores the key-value pairs, while the sorted list maintains the order of the keys.

Use Cases:
    Maintaining a leaderboard:
        SortedDict is ideal for maintaining a leaderboard where you need to keep track of the top scores in sorted order.
    Caching with LRU eviction:
        You can use SortedDict to implement a cache with LRU (Least Recently Used) eviction policy, where the least recently accessed items are removed when the cache is full.
    Efficient range queries:
        If you need to frequently perform range queries on a dictionary (e.g., finding all values between two keys), SortedDict can provide significant performance benefits.
"""