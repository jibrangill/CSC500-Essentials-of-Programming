#Author: Jibran Gill
#Main section of the proram

from shopping_cart import ShoppingCart
from item_to_purchase import ItemToPurchase
from datetime import datetime
import sys

def print_menu(cart):
    while True:
        print("------------------------------------")
        print("|            MENU                  |")
        print("------------------------------------")
        print("| a - Add item to cart             |")
        print("| r - Remove item from cart        |")
        print("| c - Change item quantity         |")
        print("| i - Output items' descriptions   |")
        print("| o - Output shopping cart         |")
        print("| q - Quit                         |")
        print("------------------------------------")
        choice = input("Choose an option: ")

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
            sys.exit("\nExiting the program. Good Bye!\n") #I used sys.exit() to exit instead of returning the control to main to avoid being prompted for customer name in main(). 
        else:
            print("Invalid option. Please try again.")

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