"""
    Q: Design an Ordered Stream
    There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is
    a string. No two pairs have the same id.

    Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each
    insertion. The concatenation of all the chunks should result in a list of the sorted values.

    Implement the OrderedStream class:

    OrderedStream(int n) Constructs the stream to take n values.
    String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk
    of currently inserted values that appear next in the order.
"""

from typing import List
from sortedcontainers import SortedList
class OrderedStream:
    def __init__(self, n: int):
        # populate a dict with keys ranging from 1 to n
        self.pairs = {i: None for i in range(1, n + 1)}
        # keep track of next id to be outputted
        self.next = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        # initialize output list
        res = []
        # add idKey,value pair in our dictionary
        self.pairs[idKey] = value
        # keep incrementing next id until we have have a value to be outputted
        while self.next in self.pairs and self.pairs[self.next]:
            # include value to be outputted
            res.append(self.pairs[self.next])
            # increment next id
            self.next += 1
        return res