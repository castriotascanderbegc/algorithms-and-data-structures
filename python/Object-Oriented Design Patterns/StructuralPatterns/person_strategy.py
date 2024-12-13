"""
    Design Pattern: Strategy Pattern

    Below shows an example of the usage of the Strategy Pattern 


    Implement the Strategy design pattern.

        The Strategy is a behavioral design pattern that enables selecting an algorithm's runtime behavior. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.

        You are given a Person class with attributes for last name, age, and marital status. Complete the implementation of the following filtering strategies (PersonFilters) to filter Person objects based on different criteria.

            AdultFilter: Filters people who are 18 years or older.
            SeniorFilter: Filters people who are 65 years or older.
            MarriedFilter: Filters people who are married.
        
        Additionally, complete the implementation of the PeopleCounter class, which uses these strategies to count Person objects based on the specified filter.
"""


from typing import List, Protocol


class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def apply(self, person:Person) -> bool:
        return person.getAge() >= 18

class SeniorFilter(PersonFilter):
    # Implement Senior filter
    def apply(self, person:Person) -> bool:
        return person.getAge() >= 65


class MarriedFilter(PersonFilter):
    # Implement Married filter
    def apply(self, person:Person) -> bool:
        return person.isMarried()

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        # Implement method here
        count = 0
        for p in people:
            if self.filter.apply(p):
                count += 1
        return count
    
