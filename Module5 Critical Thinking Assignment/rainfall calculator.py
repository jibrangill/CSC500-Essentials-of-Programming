#Author: Jibran Gill
#Part1 - Program to collect rainfall data and calculate the average rainfall over a period of years
import datetime;

#Class to calaulate rainfall
class Rainfall_Calculator:

    #initializer function to initialize the pclass variables
    def __init__(self):
        self.num_yrs = 0
        self.num_months = 12
        self.month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
        self.monthly_rainfall = {}
    
    #Function to calculate the total rainfall and average rainfall
    def calculate_rainfall(self):
        rainfall_total = sum(self.monthly_rainfall.values())
        num_months = len(self.monthly_rainfall)
        average_rainfall = rainfall_total / num_months if num_months else 0 #handling the div by zero case
        return rainfall_total, average_rainfall
    
    #Function to get user input for the years and monthly rainfall. 
    #sentinel has  been used as a termination condition
    def input_userValues(self):
        num_months_user = 0
        self.num_yrs = int(input('Enter the number of years or -1 to quit: '))
        if self.num_yrs != -1:
            entered_months = []
            user_interupt = False  #another sentinel to control iL
            for year in range(self.num_yrs):
                if user_interupt:
                    break
                for month_name in self.month_names.values():
                    rainfall = float(input(f'Enter the rainfall for {month_name} in year {year + 1} or -1 at any time to quit: '))
                    if rainfall != -1:
                        self.monthly_rainfall[month_name] = self.monthly_rainfall.get(month_name, 0) + rainfall
                        entered_months.append(month_name)
                        num_months_user = len(entered_months)
                    else:
                        user_interupt = True 
                        ct = datetime.datetime.now()
                        num_months_user = len(entered_months)
                        print()
                        print('==========================================================================================')
                        print(f'[{ct}][Warning] User interrupt gerenated (-1).') 
                        print(f'[{ct}][Warning] Data Entered - month count({num_months_user}) in Year Count({self.num_yrs})')
                        print('==========================================================================================')
                        print()
                        break
        else:
            ct = datetime.datetime.now()
            print()
            print('========================================================================')
            print(f'[{ct}][Warning] User Interrupt Generated (-1).') 
            print(f'[{ct}][Warning] Exiting the Program.')
            print(f'[{ct}][Warning] Good Bye.')
            print('=========================================================================')
            print()
        return num_months_user  
    
    #Funtion to print the rainfgall results
    def print_results(self,num_months_user):
        if self.num_yrs != -1:
            total_rainfall, average_rainfall = self.calculate_rainfall()
            print()
            print('===========================================================================================')
            print('PRECIPITATION-RESULTS:')
            print(f"Total Rainfall data entered by user in a span of {self.num_yrs} yr(s): {num_months_user} month(s)")
            print(f"Total inches of rainfall in {num_months_user} month(s): {total_rainfall:.2f} inches")
            print(f"Average rainfall per month: {average_rainfall:.2f} inches")
            print('============================================================================================')

# Main program
def main():
    rainfall_calculator = Rainfall_Calculator()
    num_months = rainfall_calculator.input_userValues()
    rainfall_calculator.print_results(num_months)

#calling main()
if __name__ == "__main__":
    main()