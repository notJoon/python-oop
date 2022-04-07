""" Singletone (Creational Pattern)

Ensure a class has only one instance, while providing global access point to this instance 

* Implementation
    - Make the default constructor privates
    - Create a static creation that acts as a constructor. this method calls the private constructor
    to create an object and saves it in a static field.

* Pros and Cons 
    Pros:
        - class has a only a single instance
        - gain a global access point to that instance 
        - Singleton object is initialized only when it's requested for the first time
    
    Cons:
        - violate single responsibility principle 
        - can mask bad design, for instance, when the components of the program 
        know too much about each other
        - difficult to unit test 

"""
from typing import Any

class SingletonMeta(type):
    """
        In python, singleton method can be implemented in different ways. 
        i.e.) base class, decorator, metaclass 
    """

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Possible changes to the value of the `__init__` args do not affect
        the return instance
        """

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance 
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        """ 
        define some bussiness logic, which can be executed on its instance.
        """
        ... 

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("singleton failed, variables contain differnet instances.")