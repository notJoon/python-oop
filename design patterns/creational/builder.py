""" Builder (Creational Patterns) 

Seperate the construction of a complex object
same construction process can create differnet representation

Use this pattern when
    1. for creating complex object should be independent
    2. the construction process must allow differnet representations 
    for the object that's constructed.

Participants
    * Builder 
        - Specifies an abstract interface for creating parts of a Product object.
    * ConcreteBuilder:
        - constructs and assembles parts of the proiduct by implementing the Builder interface.
        - defines and keeps track of the representation it creates.
        - provides an interface for retreiving the product.
    * Director
        - constructs an object using the Builder interface
    * Product
        - prepresents the complex object under construction
        - includes classes that define the constitute parts
        - including interfaces for assembling the parts into the final result

Pros an Cons
    * Pros
        - can construct objects step-by-step, defer construction steps or run steps recursively.
        - reuse the same construction code when building various representations of products.
        - Single Responsibility Principle
    * Cons
        - complexity of the code increases
"""

from abc import abstractmethod, ABC 
from typing import Any 

class Builder(ABC):
    """ Specifies methods """

    @property 
    @abstractmethod
    def product(self) -> None:
        pass 

    @abstractmethod
    def produce_part_a(self) -> None:
        pass 

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product1():
    def __init__(self) -> None: 
        self.parts = []
    
    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Product partsL {', '.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):
    """ follows the Builder interface and provide specific implementations of building steps"""

    def __init__(self) -> None:
        """ 
        A fresh builder instance should contain a blank product object,
        which is used in further assembly.
        """
        self.reset()
    
    def reset(self) -> None:
        self._product = Product1()
    
    @property 
    def product(self) -> Product1:
        """ 
        Concrete Builders are supposed to provide their own methods for retrieving results. Because various types of builders 
        may create entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base builder interface.
        """
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        self._product.add("PartA1")
    
    def produce_part_b(self) -> None:
        self._product.add("PartB1")
    
    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Director:
    """ 
    only responsible for executing the building steps in a particular sequences.
    It is helpful when producing products according tyo a specific order or configuration.
    """

    def __init__(self) -> None:
        self._builder = None 
    
    @property 
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        """ Director works with any builder instance that the client code passes to it. """
        self._builder = builder 
    
    """ The Director can construct several product variations using the same building steps. """
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()
    
    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder 

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    ## Builder pattern can be used without a Director class 
    print("Custom product")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.produce_part_c()
    builder.product.list_parts()

"""Output
Standard basic product: 
Product partsL PartA1

Standard full featured product: 
Product partsL PartA1, PartB1, PartC1

Custom product
Product partsL PartA1, PartB1, PartC1⏎ 
"""