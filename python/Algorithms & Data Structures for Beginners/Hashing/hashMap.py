# We will store a list of Pairs in our array, for which we declare a class.
class Pair:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class HashTable:
    """
        Implementation of a HashMap
        Search, Insert, Delete operations run in O(1) time

        Collision: Open Addressing technique
    """
    # We initialize a size, capacity and the map itself in our constructor. 
    # size refers to the size of the hash map 
    # capacity refers to size of the array under the hood.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity

    """
        To add to the map, we first compute the hash of the key and find the position. Once this is calculated, there are three scenarios.
            The index is occupied
            The index is occupied with the same key
            The index is vacant
    """
    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value) # type: ignore
                self.size += 1

                if self.size >= self.capacity // 2:
                    self.resize()
                return 
            
            elif self.map[index].key == key: # type: ignore
                self.map[index].value = value # type: ignore
                return

            index +=1
            index = index % self.capacity

    # To retrieve the value, we first need to retrieve the position and check if the value exists in that position. 
    # If it does, we can return that value. Otherwise, we can perform open addressing and look for it in the next available index.
    def get(self, key: int) -> int:
        index = self._hash(key)
        while self.map[index] != None:
            if self.map[index].key == key: # type: ignore
                return self.map[index].value # type: ignore
            index += 1
            index = index % self.capacity
        return -1

    # To remove, we find the index, remove the key, and set the index to null.
    def remove(self, key: int) -> bool:

        if self.get(key) == -1:
            return False

        index = self._hash(key)
        while True:

            if self.map[index].key == key: # type: ignore
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may 
                # stop searching early when it reaches this hole.

                self.map[index] = None
                self.size -= 1

                return True

            index += 1
            index = index % self.capacity

    # Get the actual size of the HashMap
    def getSize(self) -> int:
        return self.size

    # Get the size of the underlying array
    def getCapacity(self) -> int:
        return self.capacity
        
    # When we perform re-hashing/re-sizing, we double the capacity,
    # copy our previous map's values into our new map and set the size to be zero.
    def resize(self) -> None:
        self.capacity *= 2

        newMap = [None] * self.capacity

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.value)
    
    # The hash function below finds the position of the key in the array by mod with the capacity of the array    
    def _hash(self, key) -> int:
        #index = key + ord(str(key))
        return key % self.capacity


