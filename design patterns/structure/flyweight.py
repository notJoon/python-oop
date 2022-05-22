""" Flyweight 
## Intent
    Use sharing to support large numbers of fine-grained objects efficiently

    Let you fit more objects into the available amount of RAM 
    by sharing parts of state between multiple objects instead of 
    keeping all of the data in each object 

`intrinsic stage`
    - constant data of an object. stored in the flyweight.
    - It consist of information that's independent of the flyweight's context
    - sharable 

`extrinsic stage`
    - Depends on and varies with the flyweight's context
    - can't be shared

The Flyweight pattern: stop storing extrinsic state inside the object.
            -> should pass this state to specific methods which rely on it

Only the intrinsic state stays within the object, letting you reuse it in different contexts.

    * Extrinsic state storage
    * Immutability 
        Since the same flyweight object can be used in different contexts,
        must have to make sure that its state can't be modified. 
    * Factory
        For more convenient access to various flyweights 

## Applicability 
    - Use this when program must support a huge number of objects which barely fit into available RAM 
    - An application uses a large number of objects
    - Most object state can be made extrinsic 

## Pros & Cons 
    * Pros 
        - save lots of RAM 

    * Cons 
        - trading RAM over CPU cycle when some of the context data needs 
        to be recalculated each time.

        - much more complicated code
"""

import json 
from typing import Dict 

class Flyweight():
    """ 
    stores a common portion of the state (intrinsic state) that belongs to multiple 
    real business entities. 

    The flyweight accepts the rest of the state(extrinsic state) via its method params.
    """
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state
    
    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared `{s}` and unique `{u}` state.", end="")


class FlyweightFactory():
    """ 
    Flyweight Factory creates and manages the Flyweight objects

    It ensures that flyweights are shared correctly.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, init_flyweights: Dict) -> None:
        for state in init_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state: Dict) -> str:
        """ returns a Flyweight;s string hash for a given state """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """ Returns an existing Flyweight with a given state or creates a new one. """
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: can't find a flyweight, create new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]
    
    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights.")
        print("\n".join(map(str, self._flyweights.keys())), end="")

def add_car_to_police_db(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to DB.")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])

if __name__ == "__main__":
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_db(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_db(factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()