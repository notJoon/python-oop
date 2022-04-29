""" Bridge (Structure pattern) 
    lets you split a large class or a set of closely related classes 
    into two separate hierarchies—abstraction and implementation—
    which can be developed independently of each other.

    - Abstraction (or interface)
        high-level control layer for some entity.
        It should delegate the work to the implementation layer
        for not to do any real work on its own.
            -> GUI

    - Implementation (or platform)
        do some works 
            -> API

    * Structures
        - Abstraction 
            provides high-level control logic.
            relies on implementation layer.
        
        - Client 
            only interested in working with the abstraction. 
            However, it’s the client’s job to link the abstraction object 
            with one of the implementation objects
        
        - Implementation 
            declares the interface that’s common for all concrete implementations.
            Abstraction layer only communicate with this layer. 

        - Concrete Implementations 
            contain platform-specific code.

        - Refined Abstractions (OPTIONAL)
            provide variants of control logic.
        
    * Applicability
        -  Use the Bridge pattern when you want to divide and organize a monolithic class 
        that has several variants of some functionality 

        - need to extend a class in several orthogonal (independent) dimensions.

        - need to be able to switch implementations at runtime.

    * Pros and Cons 
        Pros
            - can create platform-independent classes and apps
            - Open/Closed Principle.
            - Single Responsibility Principle 
            - Client code works with high-level abstractions. 
            It isn’t exposed to the platform details.
        
        Cons
            - make the code more complicated by applying the pattern 
            to a highly cohesive class.
"""
from abc import ABC, abstractmethod 

class Implementation(ABC):
    """ 
    defines the interface for all implementation classes.
    It doesn't math with Abstraction's interface
    Typically the Implementation interface provides only primitive operations.
    """

    @abstractmethod
    def operation_implementation(self) -> str: 
        pass 


class Abstraction:
    """ 
    The Abstaction defines the interface for the "control" part
    of the two class hierarchies.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    
    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """ extend Abstraction without changing the Implementation classes """
    
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ConcreteImplementaionA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementaionB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None: 
    """ The client code should only depend on the Abstraction class """
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    impl = ConcreteImplementaionA()
    abstraction = Abstraction(impl)
    client_code(abstraction)

    print("\n")

    impl = ConcreteImplementaionB()
    abstraction = Abstraction(impl)
    client_code(abstraction)