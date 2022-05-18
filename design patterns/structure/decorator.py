""" Decorator (a.k.a Wrapper)
Attatch additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing
for extending functionality. 

# Applicability
    - to add responsibilities to individual objects dynamically
    and transparently, without affecting other objects

# Structure
    - Component: declares the common interface for both wrapper and wrapped obj.
    - Concrete Component: wrapped objects. It defines basic behavior.
    - Base Decorator: class has a field for referencing a wrapped object.
    - Concrete Decorators: define extra behaviors that can be added to components dynamically.

# Pros and Cons
## Pros
    - More flexibility than static inheritance
    - Avoids feature-laden classes high up in the hierachy
    - Combine several behaviors by wrapping an object into multiple decorators

## Cons 
    - A decorator and its components aren't identical
    - Lots of little objects 
    - Hard to remove a specific wrapper from the wrappers stack 


***
    1. What classes does it consist of?
    2. What roles do these classes play?
    3. In what way the elements of the pattern are related? 
"""

class Component():
    """ 
    The base Component interface defines operations that can be altered by decorators
    """
    def operation(self) -> str:
        pass 


class ConcreteComponent(Component):
    """ Concrete components provide default implementations of the operations """
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """ define the wrapping interface for all concrete decorators """

    _component: Component = None 

    def __init__(self, component: Component) -> Component:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """ call the wrapped object and alter its result """

    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client(component: Component) -> None:
    """ 
    Works with all objects using the Component interface.
    Stay independent of the concrete classes of components it works with 
    """

    print(f"result: {component.operation()}")


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client(decorator2)