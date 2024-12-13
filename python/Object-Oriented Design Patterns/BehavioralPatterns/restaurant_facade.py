"""
    Design Pattern: Facade Pattern

    Below shows an example of the usage of the Facade Pattern

    Implement the Facade design pattern.

        The Facade is a structural design pattern that provides a simplified interface to a complex system of classes, library, or framework. It wraps the complexities of the system and provides a simple interface to clients.

        You are given several classes that represent different parts of a restaurant's operation: Order, Cashier, Food, Chef, PackagedFood, KitchenStaff, and DriveThruFacade.

            The Cashier takes the customer's Order.
            The Chef prepares the Food as per the Order.
            The KitchenStaff packages the Food if it's a takeout order.
            The DriveThruFacade acts as the interface between the customer and these internal components of the restaurant.
        
        Your task is to implement the DriveThruFacade class to coordinate these components. The facade should handle taking orders from customers and returning either Food or PackagedFood, depending on whether the order is for takeout.



"""

class Order:
    def __init__(self, contents: str, takeOut: bool):
        self.contents = contents
        self.takeOut = takeOut

    def getOrder(self) -> str:
        return self.contents

    def isTakeOut(self) -> bool:
        return self.takeOut

class Cashier:
    def takeOrder(self, contents: str, takeOut: bool) -> Order:
        return Order(contents, takeOut)

class Food:
    def __init__(self, order: str):
        self.contents = order

    def getFood(self) -> str:
        return self.contents

class Chef:
    def prepareFood(self, order: Order) -> Food:
        return Food(order.getOrder())

class PackagedFood(Food):
    def __init__(self, food: Food):
        super().__init__(food.getFood() + " in a bag")

class KitchenStaff:
    def packageOrder(self, food: Food) -> PackagedFood:
        return PackagedFood(food)

class DriveThruFacade:
    def __init__(self):
        self.cashier = Cashier()
        self.chef = Chef()
        self.kitchenStaff = KitchenStaff()

    def takeOrder(self, orderContents: str, takeOut: bool) -> Food:
        # Implement method here
        order = self.cashier.takeOrder(orderContents, takeOut)
        food = self.chef.prepareFood(order)
        if order.isTakeOut():
            return self.kitchenStaff.packageOrder(food)
        return food



