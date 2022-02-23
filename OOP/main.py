from item import Item
from phone import Phone 


if __name__ == '__main__':
    item1 = Phone('MyItem', 750, 6)
    item1.apply_discount()
    
    print(item1.price)

