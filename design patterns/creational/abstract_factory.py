## Abstract Factory 
from abc import ABC, abstractmethod




class AbstractProductA(ABC):
    """ Each distinct product of a product family should have a base interface. """

    @abstractmethod
    def function_a(self) -> str:
        pass 

""" Concrete products are created by corresponding concrete factories """

class ConcreteProductA1(AbstractProductA):
    def function_a(self) -> str:
        return "The result of the product A1"

class ConcreteProductA2(AbstractProductA):
    def function_a(self) -> str:
        return "The result of the product A2"


class AbstractProductB(ABC):

    @abstractmethod
    def function_b(self) -> None:
        pass 

    @abstractmethod
    def another_function_b(self, collaborator: AbstractProductA) -> None:
        pass 

class ConcreteProductB1(AbstractProductB):
    def function_b(self) -> str:
        return "The result of the product B1."
    
    def another_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.function_a()
        return f"The result of the B1 collaborating with the ({result})"

class ConcreteProductB2(AbstractProductB):
    def function_b(self) -> str:
        return "The result of the product B2."
    
    def another_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.function_a()
        return f"The result of the B2 collaborating with the ({result})"




class AbstractFactory(ABC):
    """
    Abstract factory interface declares a set of methods that returns different abstract products. 
    which called family and are related by a high-level theme or concept.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass 
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass 

class ConcreteFactory1(AbstractFactory):
    """ 
    Concrete Factory produce a family of products that belongs to single variant.
    guarantees that resulting products are compatible.

    while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    """ Each concrete factory has a corresponding product variant. """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()



def client_code(factory: AbstractFactory) -> None:
    """ 
    The client code works with factories and products only throught abstract types.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.function_b()}")
    print(f"{product_b.another_function_b(product_a)}", end="")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing same client code with the second factory type:")
    client_code(ConcreteFactory2())