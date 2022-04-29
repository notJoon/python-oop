""" Apdater (Structure Pattern) 

allows objects with incompatible interfaces to collaborate.
converts the interface of one object so that another object can understand it.

    * Structures:
        - Client : contains the existing business logic of the program
        - Client Interface : describes a protocol that other classes 
                must follow to be able to collaborate with the client code.
        - Service : 3rd-party or legacy. client can't use this directly
        - Adapter : class that’s able to work with both the client and the service
    
    The client code doesn’t get coupled to the concrete adapter class 
    as long as it works with the adapter via the client interface. 

    * Pros and Cons:
        Pros:
            - Single Responsibility Principle
            - Open/closed Principle 

        Cons: 
            - The overall complexity of the code increases 
"""

### via inheritance 
class Target:
    """ 
    target defines the domain-specific interface used by the client code
    """

    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    """
    The Adapter makes the the Adaptess's interface compatible
    with the Target's interfacce via multiple inheritance. 
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "\
        "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)