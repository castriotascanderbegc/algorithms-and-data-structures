"""
    Design Pattern: State Pattern

    Below shows an example of the usage of the State Pattern

    Implement the State design pattern.

        The State is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. This pattern is often used to encapsulate the state-related behavior within state-specific classes, avoiding large conditional statements in the object's methods.

        You are given a basic Document class, which can be in one of three states: Draft, Review, or Published. The behavior of the publish method should change based on the current state of the document.

        Your task is to implement the State design pattern by creating state classes and updating the Document class so that it changes its behavior according to its state.

        States:

            Draft: A document in this state can move to the Review state.
            Review: A document in this state can be either approved to move to the Published state or rejected to return to the Draft state, depending on the value of isApproved in the Document class.
            Published: A document in this state cannot change its state anymore.
"""

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_request(self, doc) -> None:
        pass

class Document:
    def __init__(self):
        self.state = Draft()
        self.approved = False

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State) -> None:
        self.state = state

    def publish(self) -> None:
        self.state.handle_request(self)

    def set_approval(self, approved: bool) -> None:
        self.approved = approved

    def is_approved(self) -> bool:
        return self.approved

class Draft(State):
    def handle_request(self, doc: Document) -> None:
        # set to Review state
        doc.set_state(Review())

class Review(State):
    def handle_request(self, doc: Document) -> None:
        # set to Published state if approved
        if doc.is_approved():
            doc.set_state(Published())
        else:   # set back to Draft state
            doc.set_state(Draft())

class Published(State):
    def handle_request(self, doc: Document) -> None:
        # no action needed here
        pass

