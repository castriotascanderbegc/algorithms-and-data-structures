"""
    Design an Elevator System

    Functional Requirements:
        Request Handling: The elevator can handle requests from both inside and outside. This applies to both the Passenger elevator and the Service elevator.

        Directional Prioritization: Once the elevator starts moving in one direction (either up or down), it will finish processing all requests in that direction before starting on requests in the opposite direction. The service elevator runs on a first come first serve basis.

        Intermediate Stops: While processing requests in one direction, the elevator can stop at intermediate floors to pick up or drop off passengers if there are pending requests.

        State Management: The elevator maintains a state (IDLE, GOING_UP, GOING_DOWN) that determines its current activity and direction.

        Idle State: If there are no pending requests, the elevator remains in an idle state.

    Non-Functional Requirements:
        Safety:

        The elevator does not change its upward or downward direction suddenly, ensuring it doesn't endanger passengers due to abrupt motion.

        Efficiency: Directional prioritization ensures that the elevator does not waste energy by frequently changing directions. It moves in one continuous direction as much as possible.

        Scalability: The system is designed in a way that it could potentially handle multiple elevators (though this would need additional coordination logic).

        Usability: Clear logs and print statements give the user (or maintenance personnel) a clear idea of the elevator's activities.

        Reliability: The elevator aims to process every request in the queue, assisting all passengers to reach their desired destinations.

        Responsive: The elevator responds to requests in a timely manner, based on its prioritization algorithm. The passenger elevator prioritizes the direction and the service elevator prioritizes requests on a first come first serve basis.

        Simulated Delays: The system simulates real-world delays like the time taken to travel between floors and the time doors remain open for passengers to embark/disembark.

"""

from collections import deque
import heapq
import time
from enum import Enum

# our elevator can have three states: GOING_UP, GOING_DOWN, IDLE
class State(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3
    EMERGENCY = 4

# elevator can be of type: Passenger, Service
class ElevatorType(Enum):
    PASSENGER = 1
    SERVICE = 2

# a request can be made from: Inside, Outside
class RequestOrigin(Enum):
    INSIDE = 1
    OUTSIDE = 2

# elevator door can have two states: Open, Closed
class DoorState(Enum):
    OPEN = 1
    CLOSED = 2

# to call an elevator, users needs to push a button (either from inside or outside) that sends out a Requests
class Request:
    def __init__(self, origin, origin_floor, destination_floor=None):
        self.origin = origin
        self.origin_floor = origin_floor
        self.destination_floor = destination_floor
        self.direction = State.IDLE
        self.elevator_type = ElevatorType.PASSENGER
    
        # Determine direction if both origin_floor and destination_floor are provided
        if destination_floor is not None:
            if origin_floor > destination_floor:
                self.direction = State.DOWN
            elif origin_floor < destination_floor:
                self.direction = State.UP

    def get_origin(self):
        return self.origin
    
    def get_origin_floor(self):
        return self.origin_floor
    
    def get_destination_floor(self):
        return self.destination_floor
    
    def get_direction(self):
        return self.direction
    
    # to determine order within the loop
    # method overloading
    def __lt__(self, other):
        return self.destination_floor < other.destination_floor
        
# the service elevator has a different type of request
class ServiceRequest(Request):
    def __init__(self, origin, current_floor=None, destination_floor=None):
        if current_floor is not None and destination_floor is not None:
            super().__init__(origin, current_floor, destination_floor)
        else:
            super().__init__(origin, destination_floor)
        self.elevator_type = ElevatorType.SERVICE

# requests will be handled by the elevators, either PassengerElevator or ServiceElevator
class Elevator:
    def __init__(self, current_floor, emergency_status):
        self.current_floor = current_floor
        self.emergency_status = emergency_status
        self.state = State.IDLE
        self.door_state = DoorState.CLOSED
    
    def open_doors(self):
        self.door_state = DoorState.OPEN
        print(f"Doors are OPEN on floor {self.current_floor}")
    
    def close_doors(self):
        self.door_state = DoorState.CLOSED
        print(f"Doors are CLOSED")

    def wait_for_seconds(self, seconds):
        time.sleep(seconds)

    def operate(self):
        pass

    def process_emergency(self):
        pass

    def get_current_floor(self):
        return self.current_floor

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def set_current_floor(self, floor):
        self.current_floor = floor

    def get_door_state(self):
        return self.door_state

    def set_emergency_status(self, status):
        self.emergency_status = status

# PassengerElevator will use a maxHeap and minHeap to prioritize direction of the requests
class PassengerElevator(Elevator):
    def __init__(self, current_floor, emergency_status):
        super().__init__(current_floor, emergency_status)
        self.passenger_up_queue = []
        self.passenger_down_queue = []
    
    def operate(self):
        while self.passenger_up_queue or self.passenger_down_queue:
            self.process_requests()
        self.set_state(State.IDLE)
        print("All requests have been fulfilled, elevator is now ", self.get_state())

    def process_emergency(self):
        self.passenger_up_queue.clear()
        self.passenger_down_queue.clear()
        self.set_current_floor(1)
        self.set_state(State.IDLE)
        self.open_doors()
        self.set_emergency_status(True)
        print("Queues cleared, current floor is ", self.get_current_floor(), ". Doors are ", self.get_door_state())
    
    def add_up_request(self, request):
        if request.get_origin() == RequestOrigin.OUTSIDE:
            pick_up_request = Request(request.get_origin(), request.get_origin_floor(), request.get_origin_floor())
            heapq.heappush(self.passenger_up_queue, pick_up_request)
        heapq.heappush(self.passenger_up_queue, request)

    def add_down_request(self, request):
        if request.get_origin() == RequestOrigin.OUTSIDE:
            pick_up_request = Request(request.get_origin(), request.get_origin_floor(), request.get_origin_floor())
            heapq.heappush(self.passenger_down_queue, pick_up_request)
        heapq.heappush(self.passenger_down_queue, request)
    
    def process_up_requests(self):
        while self.passenger_up_queue:
            up_request = heapq.heappop(self.passenger_up_queue)

            if self.get_current_floor() == up_request.get_destination_floor():
                print("Currently on floor", self.get_current_floor(),
                      ". No movement as destination is the same.")
                continue
            print("The current floor is", self.get_current_floor(),
                  ". Next stop:", up_request.get_destination_floor())

            try:
                print("Moving ", end="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.5)  # Pause for half a second between dots.
                time.sleep(1)  # Assuming 1 second to move to the next floor.
                print()
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print("Error:", e)

            self.set_current_floor(up_request.get_destination_floor())
            print("Arrived at ", self.get_current_floor())

            self.open_doors()
            # Simulating 3 seconds for people to enter/exit
            self.wait_for_seconds(3)
            self.close_doors()
        
        print("Finished processing all the up requests")


    def process_down_requests(self):
        while self.passenger_down_queue:
            down_request = heapq.heappop(self.passenger_down_queue)

            if self.get_current_floor() == down_request.get_destination_floor():
                print("Currently on floor", self.get_current_floor(),
                      ". No movement as destination is the same.")
                continue

            print("The current floor is", self.get_current_floor(),
                  ". Next stop:", down_request.get_destination_floor())

            try:
                print("Moving ", end="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.5)  # Pause for half a second between dots.
                time.sleep(1)  # Assuming 1 second to move to the next floor.
                print()
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print("Error:", e)

            self.set_current_floor(down_request.get_destination_floor())
            print("Arrived at", self.get_current_floor())

            self.open_doors()
            # Simulating 3 seconds for people to enter/exit.
            self.wait_for_seconds(3)
            self.close_doors()

        print("Finished processing all the down requests.")

    
    def process_requests(self):
        if self.get_state() == State.UP or self.get_state() == State.IDLE:
            self.process_up_requests()
            if self.passenger_down_queue:
                print("Now processing down requests...")
                self.process_down_requests()
        else:
            self.process_down_requests()
            if self.passenger_up_queue:
                print("Now processing up requests...")
                self.process_up_requests()

# ServiceElevator operates on a first-come first-serve basis
class ServiceElevator(Elevator):
    def __init__(self, current_floor, emergency_status):
        super().__init__(current_floor, emergency_status)
        self.service_queue = deque()

    def operate(self):
        while self.service_queue:
            curr_request = self.service_queue.popleft()

            print() # Move to the next line after the dots
            print("Currently at ", self.get_current_floor())
            try:
                time.sleep(1)  # Assuming 1 second to move to the next floor.
                print(curr_request.get_direction(), end="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.5)  # Pause for half a second between dots.
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print("Error:", e)

            self.set_current_floor(curr_request.get_destination_floor())
            self.set_state(curr_request.get_direction())
            print("Arrived at", self.get_current_floor())

            self.open_doors()
            # Simulating 3 seconds for loading/unloading.
            self.wait_for_seconds(3)
            self.close_doors()

        self.set_state(State.IDLE)
        print("All requests have been fulfilled, elevator is now", self.get_state())
    
    def add_requests_to_queue(self, request):
        self.service_queue.append(request)

    
    def process_emergency(self):
        self.service_queue.clear()
        self.set_current_floor(1)
        self.set_state(State.IDLE)
        self.open_doors()
        self.set_emergency_status(True)
        print("Queue cleared, current floor is", self.get_current_floor(),
              ". Doors are", self.get_door_state())

# The user does not need to know all of the above logic. To abstract the instantiation, we can use the Factory pattern
class ElevatorFactory:
    @staticmethod
    def create_elevator(elevator_type: ElevatorType):
        if elevator_type == ElevatorType.PASSENGER:
            return PassengerElevator(1, False)
        elif ElevatorType.SERVICE:
            return ServiceElevator(1, False)
        else:
            return None

# The user will interact with the Controller class
class Controller:
    def __init__(self, factory):
        self.factory = factory
        self.passenger_elevator = factory.create_elevator(
            ElevatorType.PASSENGER)
        self.service_elevator = factory.create_elevator(
            ElevatorType.SERVICE)
        
    def send_passenger_up_requests(self, request):
        self.passenger_elevator.add_up_request(request)
    
    def send_passenger_down_requests(self, request):
        self.passenger_elevator.add_down_request(request)
    
    def send_service_request(self, request):
        self.service_elevator.add_request_to_queue(request)
    
    def handle_passenger_requests(self):
        self.passenger_elevator.operate()
    
    def handle_service_requests(self):
        self.service_elevator.operate()
    
    def handle_emergency(self):
        self.passenger_elevator.process_emergency()
        self.service_elevator.process_emergency()
    

# our Main class instantiates the Controller and sends the requests to the elevators

class Main:

    @staticmethod
    def main():
        factory = ElevatorFactory()
        controller = Controller(factory)

        controller.send_passenger_up_requests(
            Request(RequestOrigin.OUTSIDE, 1, 5)
        )
        controller.send_passenger_down_requests(
            Request(RequestOrigin.OUTSIDE, 4, 2)
        )
        controller.send_passenger_up_requests(
            Request(RequestOrigin.OUTSIDE, 3, 6)
        )
        controller.handle_passenger_requests()

        controller.send_passenger_up_requests(
            Request(RequestOrigin.OUTSIDE, 1, 9)
        )
        controller.send_passenger_down_requests(
            Request(RequestOrigin.INSIDE, 5))
        controller.send_passenger_up_requests(
            Request(RequestOrigin.OUTSIDE, 4, 12)
        )
        controller.send_passenger_down_requests(
            Request(RequestOrigin.OUTSIDE, 10, 2)
        )
        controller.handle_passenger_requests()

        print("Now processing service requests")

        controller.send_service_request(
            ServiceRequest(RequestOrigin.INSIDE, 13))
        controller.send_service_request(
            ServiceRequest(RequestOrigin.OUTSIDE, 13, 2)
        )
        controller.send_service_request(
            ServiceRequest(RequestOrigin.INSIDE, 13, 15)
        )

        controller.handle_service_requests()


if __name__ == "__main__":
    Main.main()


        

    


