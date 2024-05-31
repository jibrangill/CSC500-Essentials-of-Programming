#A program that calculates the total amount of a meal purchased at a restaurant.
#The program asks the user to enter the charge for the food and then calculate 
#the amounts with an 18 percent tip and 7 percent sales tax
#Displays each of these amounts and the total price.

#Author: Jibran Gill

#To practice the python classes I will create a class meal price calculator

class MealPriceCalculator:
    #initializing the data attributes
    def __init__(self, food_charge):
        self.food_charge =  food_charge
        self.tip_amount = 0.18
        self.sales_tax = 0.07
    
    #Function for Tip calculation
    def tipCalculator(self):
        self.tip_amount_total = self.food_charge * self.tip_amount
        return self.tip_amount_total
    
    #Function for sales tax calculation
    def salesTax_Calculator(self):
        self.sales_tax_total = self.food_charge * self.sales_tax
        return self.sales_tax_total
    
    #function for total bill calaulation
    def totalBill(self):
        tip = self.tipCalculator()
        tax = self.salesTax_Calculator()
        total = self.food_charge + tip + tax
        return total
    
    #Printing the reciept
    def printReciept(self):
        tip = self.tipCalculator()
        tax = self.salesTax_Calculator()
        total = self.totalBill()
        print("\n----RECIEPT----")
        print('Food Charge: {:.2f}'.format(self.food_charge),end='$')
        print()
        print('Sales Tax 7%: {:.2f}'.format(tax),end='$')
        print()
        print('Tip Amount 18%: {:.2f}'.format(tip),end='$')
        print()
        print('Total Bill: {:.2f}'.format(total),end='$')

def main():
    user_food_charge = float(input('Enter your food charge:'))
    user_bill = MealPriceCalculator(user_food_charge)
    user_bill.printReciept()

if __name__ == '__main__':
    main()