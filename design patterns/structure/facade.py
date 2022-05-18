""" Facade 
# Intent 
    Provide a unified interface to a set of interfaces in a subsystem.
    Defines a higher-level interface that makes the subsystem easier to use.
        -> Provides a simplified interface to a lib, frameworks , or other things 

# Structure
    - Facade: provides convenient access to a particular part of the subsystem's functionality
    - Additional Facade: prevent polluting a single facade with unrelated features 
    - Complex Subsystem
    - Client

# Applicability
    - Need to have a limited but straightforward interface to a complex subsystem 
    - To structure a subsystem into layers 

# Pros and Cons 
## Pros
    - isolate the code from the complexity of a subsystem

## Cons 
    - can become a got object
"""

class Subsystem1:
    """ Accept request either from the facade or client directly """
    def operation1(self) -> str:
        return "Subsystem1 is ready"

    def operationZ(self) -> str:
        return "Subsystem1 is Activated"

class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2 is ready"

    def operationZ(self) -> str:
        return "Subsystem2 is Activated"

class Facade:
    """ Provides a simple interface to the complex logic of one or more subsystems """
    def __init__(self, sub1: Subsystem1, sub2: Subsystem2) -> None:
        self._sub1 = sub1 or Subsystem1()
        self._sub2 = sub2 or Subsystem2()
    
    def operation(self) -> str:
        result = []
        result.append("Facade init subsystems:")
        result.append(self._sub1.operation1())
        result.append(self._sub2.operation1())
        result.append("Facade orders subsystems to perform the action")
        result.append(self._sub1.operationZ())
        result.append(self._sub2.operationZ())

        return "\n".join(result)

def client(facade: Facade) -> None:
    """ 
        The Client works with complex subsystems through a simple interface
        provided by the Facade
    """        
    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client(facade)