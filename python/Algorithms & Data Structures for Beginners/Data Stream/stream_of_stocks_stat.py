"""
    Q: Stock Stat from Stock Data Stream

    Process a stream of stock information which allow querying of the stock stat information.
    Input: <Stock Symbol, Timestamp, Stock Price>
    Output: For a given Stock Symbol
    <Stock Symbol, Current Stock Price, 52-Week High, 52-Week-Low>


    Note: You can assume the timestamp in the Epoch Millisecond format if you wish.


    Example:
    Input Stream:
    ABC, 17-July-2019 10:15:12, 12.87
    XYZ, 17-July-2019 10:16:12, 22.87
    XYZ, 18-July-2019 10:17:12, 25.87
    ABC, 18-July-2019 10:18:12, 11.87
    PQR, 18-July-2019 10:19:12, 50.87


    Query:
    ABC: ABC, 11.87, 12.87, 11.87
    XYZ; XYZ, 25.87, 25.87, 22.87
    PQY: PQR, 50.87, 50.87, 50.87
"""

from datetime import datetime, timedelta
from collections import defaultdict, deque
class StockStats:
    """
    Approach:
        To avoid recalculating the max and min every time (this can be costly if we have a large number of prices that fall witihn a 52-week period),
        we can use additional data structures:
    
        Maintaining a Sliding Window with Two Deques. 
            We can use two deques:
                - Max deque: Stores potential max values in descending order
                - Min deque: Stores potential min values in ascending order
            
            As new entries are added:
                Remove elements from the front of the deque that are outside the 52-week period.
                Maintain the order by removing values from the back that are no longer candidates for max/min.
            
            This way, we can update max and min in O(1) amortized time complexity.
    """
    def __init__(self):
        """ Initialize the Stock Stat object """
        # use a dictionary to store stock data
        self.stocks = {}
        # keep track of a 52-week period
        self.one_year = timedelta(weeks=52)

    # Time Complexity: T(n) = O(1) amortized
    def process_stock(self, stock_symbol: str, timestamp: str, stock_price: float) -> None:
        """ Updates the stock's current price and adjusts the 52-week high and low. """
        
        timestamp_dt = datetime.strptime(timestamp, "%d-%B-%Y %H:%M:%S")

        if stock_symbol not in self.stocks:
            self.stocks[stock_symbol] = {
                "prices": deque(), # to store (timestamp, price) pairs
                "max_deque": deque(), # to store max prices
                "min_deque": deque() # to store min prices
            }
        
        stock_data = self.stocks[stock_symbol]
        prices = stock_data["prices"]
        max_deque = stock_data["max_deque"]
        min_deque = stock_data["min_deque"]

        # Add the new price to the prices deque
        prices.append((timestamp_dt, stock_price))

        # Maitain the max deque
        while max_deque and max_deque[-1][1] <= stock_price:
            max_deque.pop()
        max_deque.append((timestamp_dt, stock_price))

        # Maintain the min deque
        while min_deque and min_deque[-1][1] >= stock_price:
            min_deque.pop()
        min_deque.append((timestamp_dt, stock_price))
    
        # Remove the prices that are outside the 52-week period
        while prices and prices[0][0] < timestamp_dt - self.one_year:
            old_timestamp, old_price = prices.popleft()
            if max_deque and max_deque[0][0] == old_timestamp:
                max_deque.popleft()
            if min_deque and min_deque[0][0] == old_timestamp:
                min_deque.popleft()
    
    # Time Complexity: T(n) = O(1)
    def query_stock(self, stock_symbol: str) -> str:
        """ Returns the stock stat for the given stock symbol """
        if stock_symbol not in self.stocks:
            return f"{stock_symbol}: No data available"
        
        stock_data = self.stocks[stock_symbol]
        current_price = stock_data["prices"][-1][1]
        max_price = stock_data["max_deque"][0][1]
        min_price = stock_data["min_deque"][0][1]

        return f"{stock_symbol}, {current_price}, {max_price}, {min_price}"


"""
    Time Complexity Analysis:
        - process_stock method - O(1) amortized
            a. Adding a new price to the prices deque: O(1)
            b. Maintaining the max deque: O(1) amortized
                Here, we remove elements from the back of the deque while they are smaller than or equal than 
                the current price. In the worst case, all elements in the deque might be removed. However, each price is added and removed at most once from the deque. 
            c. Maintaining the min deque: O(1) amortized
                Similarly, we remove elements from the back of the deque while they are greater than or equal to the new price
                Since each price is added and removed at most once from the deque, the time complexity is O(1) amortized.
            
            d. Removing the prices that are outside the 52-week period: O(1) amortized
                We remove entries from the fron of th prices, max_deque, and min_deque if they are outside the 52-week period.
                Each entry is added and removed at most once from the deque, so the time complexity is O(1) amortized.
        
        The amortized complexity of maintaining the deques ensures that each price is added and removed exactly once across all updates.
        Therefore, if there are n updates, the time complexity is O(n).
        
        - query_stock method - O(1)
            The query_stock method returns the stock stat for the given stock symbol in O(1) time complexity.
        
        Querying is O(1) per call, so m queries will have a total complexity of O(m).
                
""" 


if __name__ == "__main__":
    # Example usage
    stock_stats = StockStats()

    # Processing the input stream
    stock_stats.process_stock("ABC", "17-July-2019 10:15:12", 12.87)
    stock_stats.process_stock("XYZ", "17-July-2019 10:16:12", 22.87)
    stock_stats.process_stock("XYZ", "18-July-2019 10:17:12", 25.87)
    stock_stats.process_stock("ABC", "18-July-2019 10:18:12", 11.87)
    stock_stats.process_stock("PQR", "18-July-2019 10:19:12", 50.87)

    # Querying stocks
    print(stock_stats.query_stock("ABC"))  # Output: ABC, 11.87, 12.87, 11.87
    print(stock_stats.query_stock("XYZ"))  # Output: XYZ, 25.87, 25.87, 22.87
    print(stock_stats.query_stock("PQR"))  # Output: PQR, 50.87, 50.87, 50.87
    print(stock_stats.query_stock("LMN"))  # Output: LMN: No data available