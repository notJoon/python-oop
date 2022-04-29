"""Compose (structure) 

Compose object into tree structures to represent part-whole hierarchies. 

[Structure]
    1. Component 
        describes operations that are common to both simple and complex elements of the tree
    2. Leaf 
        basic element of a tree
        doesn't have sub-elements
        doing most real work 
    3. Client 
        works with all elements throught the component interface 
    4. Container (composite)
        have sub-elements

"""

from abc import ABC, abstractmethod
from typing import List 

class Component(ABC):
    """ 
    base component class declares common operations 
    for both simple and complex objects of a composition 
    """

    @property 
    def parent(self) -> Component:
        return self._parent
    
    @parent.setter
    def parent(self, parent: Component):
        # setting and accessing a parent of the component in a tree structure 
        self._parent = parent 

    ## declare child-management operations. 
    ## don't need to expose any concrete classes to the client node 
    def add(self, component: Component) -> None:
        pass 

    def remove(self, component: Component) -> None:
        pass 

    def is_composite(self) -> bool:
        return False 

    @abstractmethod
    def operation(self) -> str:
        # base component may implement some default behavior or leave it concrete classes
        pass 

class Leaf(Component):
    """ 
    - Leaf class represents the end objects of a composition
    - can't have any children 
    - usually do real work 
    """
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    """ 
    represents the complex components that may have children.
    usually delegate the actual work to their children and then sum-up the result.
    """
    def __init__(self) -> None:
        self._children: List[Component] = []

        """
        Composite object can add or remove other components 
        """

        def add(self, component: Component) -> None:
            self._children.append(component)
        
        def remove(self, component: Component) -> None:
            self._children.remove(component)
            component.parent = None 

        def is_composite(self) -> bool:
            return True 
        
        def operation(self) -> str:
            ## executes its primary logic in a particular way 
            results = []
            for child in self._children:
                results.append(child.operation())
            return f"Branch({'+'.join(results)})"

def client_code(component: Component) -> None:
    """ Client code works with all of the components vi the base interface """
    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: got a simple components")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)