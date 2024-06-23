#Author: Jibran Gill
#Class ItemToPurchase
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0.0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    #Funtion to print the item cost based on item quantity
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    #Function to print the item desription
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    #I wrote this str function to print the list items for debugging issues in the remove function 
    # its not used otherwise
    def __str__(self):
        return (f"Item Name: {self.item_name}, "
                f"Description: {self.item_description}, "
                f"Price: ${self.item_price}, "
                f"Quantity: {self.item_quantity}")