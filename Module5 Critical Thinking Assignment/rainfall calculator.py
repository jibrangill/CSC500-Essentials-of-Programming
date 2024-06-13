# Author: Jibran Gill
# Part1 - Program to collect rainfall data and calculate the average rainfall over a period of years
import datetime

# Class to calculate rainfall
class Rainfall_Calculator:

    # Initializer function to initialize the class variables
    def __init__(self):
        self.num_yrs = 0
        self.num_months = 12
        self.month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        self.monthly_rainfall = {}
    
    # Function to calculate the total rainfall and average rainfall
    def calculate_rainfall(self):
        rainfall_total = sum(self.monthly_rainfall.values())
        num_months = len(self.monthly_rainfall)
        average_rainfall = rainfall_total / num_months if num_months else 0 # Handling the div by zero case
        return rainfall_total, average_rainfall
    
    # Function to get user input for the years and monthly rainfall.
    # Sentinel has been used as a termination condition
    def input_user_values(self):
        total_entered_months = 0
        self.num_yrs = int(input('Enter the number of years or -1 to quit: '))
        if self.num_yrs != -1:
            user_interrupt = False  # Another sentinel to control input
            for year in range(self.num_yrs):
                if user_interrupt:
                    break
                for month_name in self.month_names.values():
                    rainfall = float(input(f'Enter the rainfall for {month_name} in year {year + 1} or -1 at any time to quit: '))
                    if rainfall != -1:
                        self.monthly_rainfall[month_name + str(year)] = rainfall
                        total_entered_months += 1
                    else:
                        user_interrupt = True
                        ct = datetime.datetime.now()
                        print()
                        print('==========================================================================================')
                        print(f'[{ct}][Warning] User interrupt generated (-1).') 
                        print(f'[{ct}][Warning] Data Entered - month count({total_entered_months}) in Year Count({self.num_yrs})')
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
        return total_entered_months  
    
    # Function to print the rainfall results
    def print_results(self, total_entered_months):
        if self.num_yrs != -1:
            total_rainfall, average_rainfall = self.calculate_rainfall()
            print()
            print('===========================================================================================')
            print('PRECIPITATION-RESULTS:')
            print(f"Total Rainfall data entered by user in a span of {self.num_yrs} yr(s): {total_entered_months} month(s)")
            print(f"Total inches of rainfall in {total_entered_months} month(s): {total_rainfall:.2f} inches")
            print(f"Average rainfall per month: {average_rainfall:.2f} inches")
            print('============================================================================================')

# Main program
def main():
    rainfall_calculator = Rainfall_Calculator()
    total_entered_months = rainfall_calculator.input_user_values()
    rainfall_calculator.print_results(total_entered_months)

# Calling main
if __name__ == "__main__":
    main()