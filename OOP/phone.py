from item import Item

# child class 
class Phone(Item):
    def __init__(self, name: str, price: float, 
                    quantity: int, broken_phones=0) -> None:
        ## call super() to have access to all attributes / methods
        ## avoid code duplicates 
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"broken_phones {broken_phones} is not greater than or equal to zero"

        self.broken_phones = broken_phones