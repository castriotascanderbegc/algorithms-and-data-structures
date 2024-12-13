"""
    Design Pattern: Observer Pattern

    Below shows an example of the usage of the Observer Pattern

    Implement the Observer design pattern.

        The Observer is a behavioral design pattern that allows objects to be notified about changes in another object's state.

        In an e-commerce setting, customers (observers) can subscribe to notifications about product availability, and they are notified when an out-of-stock product (subject) becomes available.

        Complete the implementation of an OnlineStoreItem (the subject) and Customer (the observer). The OnlineStoreItem will notify Customer instances only when its stock changes from 0 to a positive number.

        Your class will be tested by calling countNotifications() on each Customer to ensure they received the correct number of notifications.

"""
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def updateStock(self, newStock: int) -> None:
        if self.stock == 0 and newStock > 0:
            self.sendNotifications()
        self.stock = newStock
    
    def sendNotifications(self) -> None:
        for obs in self.observers:
            obs.notify(self.itemName)
