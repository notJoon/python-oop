import csv 

## parent class
class Item:
    all = []
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity: int) -> None:

        ## run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        ## assign to self object
        self.__name = name 
        self.__price = price 
        self.quantity = quantity

        ## actions to excute
        Item.all.append(self)

    @property 
    def price(self) -> float:
        return self.__price
    
    def apply_discount(self) -> None:
        self.__price = self.__price * Item.pay_rate

    def apply_increment(self, increments_num: int) -> float:
        self.__price = self.__price + self.__price * increments_num

    def calculate_total_price(self) -> int:
        return self.__price * self.quantity

    @property 
    ## property decorator : read-only attrribute
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            raise Exception('The name is toooo long')
        
        else:
            self.__name = value
    

    @classmethod
    def read_from_csv(cls) -> None:
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num: any) -> bool:
        if isinstance(num, float):
            return num.is_integer()
        
        elif isinstance(num, int):
            return True 
        
        else:
            return False 
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def __connect(self, smpt_server) -> None:
        pass 

    def __prepare_body(self) -> str:
        return f"""
        hello, someone
        we have {self.name} {self.quantity} times.
        """
    
    def __send(self):
        pass 

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()