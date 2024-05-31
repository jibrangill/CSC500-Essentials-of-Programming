#A program that calculates the total amount of a meal purchased at a restaurant.
#The program asks the user to enter the charge for the food and then calculate 
#the amounts with an 18 percent tip and 7 percent sales tax
#Displays each of these amounts and the total price.

#Author: Jibran Gill

#To practice the python classes I will create a class meal price 
# I am trying to use lists to perform calculation on multiple food items charges

class MealPriceCalculator:
    #initializing the data attributes
    def __init__(self, food_charge):
        self.food_charge =  food_charge
        self.tip_amount = 0.18
        self.sales_tax = 0.07
    
    #function to sum the list
    def sumFoodCharges(self):
        summation_list = sum(self.food_charge)
        return summation_list
    
    #Function for Tip calculation
    def tipCalculator(self):
        total_charge = self.sumFoodCharges()
        return self.tip_amount * total_charge
    
    #Function for sales tax calculation
    def salesTax_Calculator(self):
        total_tax = self.sumFoodCharges()
        return self.sales_tax * total_tax
    
    #function for total bill calaulation
    def totalBill(self):
        tip = self.tipCalculator()
        tax = self.salesTax_Calculator()
        total_charge = self.sumFoodCharges()
        grand_total = total_charge + tip + tax
        return grand_total
    
    #Printing the reciept
    def printReciept(self):
        tip = self.tipCalculator()
        tax = self.salesTax_Calculator()
        total = self.totalBill()
        print("\n----RECIEPT----")
        for i, charge in enumerate (self.food_charge):
            print(f"Meal {i + 1} Food Charge: {charge:.2f}$", end=' ')
            print()
        print('Sales Tax 7%: {:.2f}'.format(tax),end='$')
        print()
        print('Tip Amount 18%: {:.2f}'.format(tip),end='$')
        print()
        print('Total Bill: {:.2f}'.format(total),end='$')

def main():
    total_meals = int(input('Enter your total meals:'))
    food_charges = []
    for x in range(total_meals):
        user_food_charge = float(input(f'Enter your food charge for meal {x+1}:'))
        food_charges.append(user_food_charge)
    user_bill = MealPriceCalculator(food_charges)
    user_bill.printReciept()

if __name__ == '__main__':
    main()