# Author: Jibran Gill
# Class ItemToPurchase
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    # Function to print the item cost based on item quantity
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    # Function to print the item description
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    # I wrote this str function to print the list items for debugging issues in the remove function 
    # it's not used otherwise
    def __str__(self):
        return (f"Item Name: {self.item_name}, "
                f"Description: {self.item_description}, "
                f"Price: ${self.item_price}, "
                f"Quantity: {self.item_quantity}")

# Class ShoppingCart
# from item_to_purchase import ItemToPurchase

class ShoppingCart:

    # Initializer Function, as required by the assignment
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Function to add the item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Function to remove the item in the cart
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print(f'{item_name} found and removed successfully\n')
                break
        if not found:
            print(f'{item_name} not found in cart. Nothing removed\n.')

    # Function to modify the item in the cart
    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                found = True
                print(f'{item_to_modify.item_name} modified successfully\n')
                break
        if not found:
            print("Item not found in cart. Nothing modified\n")

    # Function to get the number of items in the cart
    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity
    
    # Function to calculate the total cost of the cart
    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost
    
    # Function to print the total cart items as required by the assignment
    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY\n")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Function to print the item descriptions
    # Item description is referencing the class item_to_purchase
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")   
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY\n")
        else:
            for item in self.cart_items:
                item.print_item_description()

# Main section of the program
from datetime import datetime
import sys

# Function to print the menu and request user input
def print_menu(cart):
    while True:
        print("----------------------------------------------------")
        print("|            MENU                                   |")
        print("----------------------------------------------------")
        print("| a - Add item to cart                              |")
        print("| r - Remove item from cart                         |")
        print("| c - Change Item (Description, Price or Quanity)   |")
        print("| i - Output items' descriptions                    |")
        print("| o - Output shopping cart                          |")
        print("| q - Quit                                          |")
        print("----------------------------------------------------")
        choice = input("Choose an option: ")
        # Branching for handling the user input. Also checking the ValueError
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            while True:
                try:
                    item_price = float(input("Enter the item price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")
            while True:
                try:
                    item_quantity = int(input("Enter the item quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            new_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(new_item)
        elif choice == 'r':
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name: ")
            # Check if item exists before asking for other inputs
            item_exists = any(item.item_name == item_name for item in cart.cart_items)
            if not item_exists:
                print(f"Item '{item_name}' not found in cart. Nothing modified.")
                continue
            else:
                print("Item found in cart.")
            item_description = input("Enter the new description (or 'none' to leave unchanged): ")
            while True:
                try:
                    item_price = float(input("Enter the new price (or 0 to leave unchanged): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")
            while True:
                try:
                    item_quantity = int(input("Enter the new quantity (or 0 to leave unchanged): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            modified_item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.modify_item(modified_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            sys.exit("\nExiting the program. Good Bye!\n")
        else:
            print("Invalid option. Please try again.")

# Function to get the date and verify the integrity
# Checking for invalid format or wrong spellings
# Checking if date entered is a future date
def get_valid_date():
    while True:
        date_str = input("Enter today's date, Format (January 1, 2020): ")
        try:
            valid_date = datetime.strptime(date_str, "%B %d, %Y")
            if valid_date > datetime.now():
                print("Date entered is in the future. Please enter today's date or a past date.")
            else:
                return date_str
        except ValueError:
            print("Invalid date format. Make sure the date is in 'Month Day, Year' format and the month is spelled correctly. Please try again.")

# Main function
def main():
    while True:
        customer_name = input("Enter customer's name or 'q' to quit: ")
        if customer_name.lower() == 'q':
            break
        current_date = get_valid_date()
        shopping_cart = ShoppingCart(customer_name, current_date)
        print(f"\nCustomer name: {shopping_cart.customer_name}")
        print(f"Today's date: {shopping_cart.current_date}")
        print_menu(shopping_cart)
    print("\nExiting the program. Good Bye!\n") 

if __name__ == "__main__":
    main()