#Author Jibran Gill
#Module4 Critical Thinking Assignment
#Online Shopping Cart

#Step 1: ItemToPurchase class
class ItemtoPurchase:

    def __init__(self):
        self.item_name = 'name'
        self.item_price = 0.0
        self.item_quantity = 0

    def priceCalculator(self):
        self.total_price = self.item_quantity * self.item_price
        return self.total_price
    
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_price:.2f} ')
        
#Step 2 Prompting the user for two items and creating two objects of the ItemToPurchase class in main section
def main():
   
    list_of_items = []
    total_all_items = 0.0
    for i in range(2):
        item = ItemtoPurchase()
        print('Item',i+1)
        item.item_name = input('Enter the item name: ')
        item.item_price = float(input('Enter the item price: '))
        item.item_quantity =  int(input('Enter the item quantity: '))
        print()
        item_total_quantity_price = item.priceCalculator()
        total_all_items += item_total_quantity_price
        list_of_items.append(item)
            
    #Step 3: Adding the costs of the two items together and printing the total cost.
    print('TOTAL COST')
    for items in list_of_items:
        items.print_item_cost()
    print(f'Total: ${total_all_items:.2f}')   

if __name__ == "__main__":
    main()