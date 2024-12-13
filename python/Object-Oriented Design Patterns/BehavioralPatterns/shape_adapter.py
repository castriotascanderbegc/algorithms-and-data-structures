""" 
    Design Pattern: The Adapter Pattern

    Below shows an example of the usage of the Adapter Pattern


    Implement the Adapter design pattern.
        The Adapter is a structural design pattern that allows incompatible interfaces to work together. It wraps an existing class with a new interface so that it becomes compatible with the client's interface.
        You are given completed SquareHole, Square and Circle classes. A Square fits into a SquareHole if the Square's side length is less than or equal to the SquareHole's length. A Circle has a radius and a Circle fits into a SquareHole if the Circle's diameter is less than or equal to the SquareHole's length.
        Complete the implementation of the CircleToSquareAdapter class such that it adapts a Circle to a Square.
"""
class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
      # Write your code here
      self.diameter = 2 * circle.getRadius()
    
    def getSideLength(self) -> float:
      # Write your code here
      return self.diameter
    

