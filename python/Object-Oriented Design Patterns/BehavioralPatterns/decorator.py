"""
    Design Pattern: Decorator Pattern

    Below shows an example of the usage of the Decorator Pattern


    Implement the Decorator design pattern.
        The Decorator is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.
        You are given a completed Coffee class, which has a method getCost() to return the cost of the coffee.
        Your task is to implement the following decorator classes that add ingredients to the coffee and increase the coffee's cost.

        MilkDecorator increases the cost by 0.5.
        SugarDecorator increases the cost by 0.2.
        CreamDecorator increases the cost by 0.7.
"""
from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self) -> float:
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self) -> float:
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    # Implement the Milk decorator
    def __init__(self, coffe):
        super().__init__(coffe)

    def getCost(self) -> float:
        return 0.5 + super().getCost()

class SugarDecorator(CoffeeDecorator):
    # Implement the Sugar decorator
    def __init__(self, coffe):
        super().__init__(coffe)

    def getCost(self) -> float:
        return 0.2 + super().getCost()

class CreamDecorator(CoffeeDecorator):
    # Implement the Cream decorator
    def __init__(self, coffe):
        super().__init__(coffe)

    def getCost(self) -> float:
        return 0.7 + super().getCost()
