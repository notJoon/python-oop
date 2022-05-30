""" Proxy
## Intent
    Provide a substitute(surrogate) or placeholder for another object.
    A proxy controls access to the original object, allowing you to perform
    something either before or after the request gets through to the original object.

## Analogy
    - A credit card is a proxy for a bank account, which is a proxy for a bundle of cash.

## Structure 
    - Service Interface
        declares the interface of the service. the proxy must follow this interface to be able to disguise itself
        as a service object.
    - Service
        provides some useful business logic. class 
    - Proxy
        proxy class has a reference field that points to a service object.
        usually, manage the full lifecycle of their service objects.
    - Client

## Pros and Cons 
    - Pros
        1. can control the service object without clients knowing about it.
        2. manage the lifecycle of the service object when clients don't care about it 
        3. works even if the service object isn't ready or is not available.
        4. Open/Closed Principle
    - Cons 
        1. more complicated
        2. the response from the service might get delayed 

"""
from abc import ABC, abstractmethod

class Subject(ABC):
    """ 
    declares common operations for both RealSubject and the proxy.
    be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass 

class RealSubject(Subject):
    """ 
    contains some business logic. usually RealSubjects are capable of doing some useful work
    which may also be very slow or sensitive.
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """ The proxy has an interface identical to the RealSubject. """
    def __init__(self, real: RealSubject) -> None:
        self._real = real
    
    def request(self) -> None:
        if self.check_access():
            self._real.request()
            self.log_access()
    
    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True 
    
    def log_access(self) -> None:
        print("Proxy: logging the time of request.", end="")

def client(sub: Subject) -> None:
    sub.request()

if __name__ == '__main__':
    print("Client: Executing the client code with a real subject:")
    real_sub = RealSubject()
    client(real_sub)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_sub)
    client(proxy)