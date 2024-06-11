class Rainfall_Calculator:

    def __init__(self):
        self.num_yrs = 0
        self.num_months = 12
        self.month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
        self.monthly_rainfall = {}
    
    def calculate_rainfall(self):
        rainfall_total = sum(self.monthly_rainfall.values())
        num_months = len(self.monthly_rainfall)
        average_rainfall = rainfall_total / num_months if num_months else 0
        return rainfall_total, average_rainfall, num_months
    
    def input_userValues(self):
        self.num_yrs = int(input('Enter the number of years or -1 to quit: '))
        if self.num_yrs != -1:
            entered_months = set()
            for year in range(self.num_yrs):
                for month_number, month_name in self.month_names.items():
                    rainfall = float(input(f'Enter the rainfall for {month_name} in year {year + 1} or -1 at any time to quit: '))
                    if rainfall != -1:
                        self.monthly_rainfall[month_name] = self.monthly_rainfall.get(month_name, 0) + rainfall
                        entered_months.add(month_name)
                    else:
                        break
            self.num_months = len(entered_months)
        else:
            print()
            print('Exiting the Program. Good Bye')
            print()
            
    def print_results(self):
        if self.num_yrs != -1:
            total_rainfall, average_rainfall, num_months = self.calculate_rainfall()
            print()
            print('RESULTS:')
            print(f"Number of months: {num_months}")
            print(f"Total inches of rainfall: {total_rainfall} inches")
            print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Main program
if __name__ == "__main__":
    rainfall_calculator = Rainfall_Calculator()
    rainfall_calculator.input_userValues()
    rainfall_calculator.print_results()
