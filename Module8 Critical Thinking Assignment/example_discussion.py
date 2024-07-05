# Author: Jibran Gill
# Class ItemToPurchase
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0.0):
        self._item_name = name
        self._item_description = description
        self._item_price = price
        self._item_quantity = quantity
        
        # Print the attributes and methods of the instance
        print(dir(self))

    # Function to print the item cost based on item quantity
    def print_item_cost(self):
        total_cost = self._item_price * self._item_quantity
        print(f"{self._item_name} {self._item_quantity} @ ${self._item_price:.2f} = ${total_cost:.2f}")

    # Function to print the item description
    def print_item_description(self):
        print(f"{self._item_name}: {self._item_description}")

    # Getters and setters for private attributes
    def get_item_name(self):
        return self._item_name

    def set_item_name(self, name):
        self._item_name = name

    def get_item_description(self):
        return self._item_description

    def set_item_description(self, description):
        self._item_description = description

    def get_item_price(self):
        return self._item_price

    def set_item_price(self, price):
        self._item_price = price

    def get_item_quantity(self):
        return self._item_quantity

    def set_item_quantity(self, quantity):
        self._item_quantity = quantity

    # I wrote this str function to print the list items for debugging issues in the remove function 
    # it's not used otherwise
    def __str__(self):
        return (f"Item Name: {self._item_name}, "
                f"Description: {self._item_description}, "
                f"Price: ${self._item_price}, "
                f"Quantity: {self._item_quantity}")

# Example usage
item = ItemToPurchase("Apple", "Fresh Red Apple", 0.5, 10)
#item.print_item_cost()
#item.print_item_description()
#print(item)
print(item._item_description)
print(item._item_name)
