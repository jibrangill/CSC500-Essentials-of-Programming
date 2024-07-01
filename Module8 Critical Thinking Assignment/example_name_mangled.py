# Author: Jibran Gill
# Class ItemToPurchase
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0.0):
        self.__item_name = name
        self.__item_description = description
        self.__item_price = price
        self.__item_quantity = quantity
        
        # Print the attributes and methods of the instance
        print(dir(self))

    # Function to print the item cost based on item quantity
    def print_item_cost(self):
        total_cost = self.__item_price * self.__item_quantity
        print(f"{self.__item_name} {self.__item_quantity} @ ${self.__item_price:.2f} = ${total_cost:.2f}")

    # Function to print the item description
    def print_item_description(self):
        print(f"{self.__item_name}: {self.__item_description}")

    # Getter methods for private attributes
    def get_item_name(self):
        return self.__item_name

    def get_item_description(self):
        return self.__item_description

    def get_item_price(self):
        return self.__item_price

    def get_item_quantity(self):
        return self.__item_quantity

    # Setter methods for private attributes
    def set_item_name(self, name):
        self.__item_name = name

    def set_item_description(self, description):
        self.__item_description = description

    def set_item_price(self, price):
        self.__item_price = price

    def set_item_quantity(self, quantity):
        self.__item_quantity = quantity

    # I wrote this str function to print the list items for debugging issues in the remove function 
    # it's not used otherwise
    def __str__(self):
        return (f"Item Name: {self.__item_name}, "
                f"Description: {self.__item_description}, "
                f"Price: ${self.__item_price}, "
                f"Quantity: {self.__item_quantity}")

# Example usage
item = ItemToPurchase("Apple", "Fresh Red Apple", 0.5, 10)
item.print_item_cost()
item.print_item_description()
print(item)
