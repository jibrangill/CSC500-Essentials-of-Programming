#Author: Jibran Gill
#Class Shopping _Cart
from item_to_purchase import ItemToPurchase

class ShoppingCart:

    #Initializer Function, as required bt the assignment
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #function to add the item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    #Funtion to remove the item in the cart
    def remove_item(self, item_name):
        #print("Current items in the cart before removal:")
        #for item in self.cart_items:
        #    print(item)
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print(f'{item_name} Found and Removed successfully')
                break
        if not found:
            #print("Current items in the cart :")
            #for item in self.cart_items:
            #   print(item)
            print(f'{item_name} not found in cart. Nothing removed.')

        #print("Current items in the cart after removal attempt:")
        #for item in self.cart_items:
        #    print(item) 

    #Funtion to modify the item in the cart
    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name != item_to_modify.item_name:
                print("Item not found in cart. Nothing modified.")
                break

            else:
                for item in self.cart_items:
                    if item.item_name == item_to_modify.item_name:
                        if item_to_modify.item_description != "none":
                            item.item_description = item_to_modify.item_description
                        if item_to_modify.item_price != 0:
                            item.item_price = item_to_modify.item_price
                        if item_to_modify.item_quantity != 0:
                            item.item_quantity = item_to_modify.item_quantity

    #Funtion to get the number of items in the cart
    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity
    
    #Funtion to calculate the total cost of the cart
    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost
    
    #function to print the total cart items as required by the assignment
    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    #Function to print the item desctiptions
    #Item desctption is referencing the class item_to_purcase
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")   
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_description()