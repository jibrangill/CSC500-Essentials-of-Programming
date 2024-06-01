#Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm 
#Your program should output what the time will be on a 24-hour clock when the alarm goes off
#Author Jibran Gill

#I want to practice the python classes so will create a class
class alarmCalculator:

    #initializer function
    def __init__(self,user_current_time,alarm_wait):
        self.time_entered_by_user = user_current_time
        self.hours_to_wait = alarm_wait

    #function to calculate the when the alarm goes off. Additional calculation to check # of days after which alarm will sound has been included as well.
    def alarm_time_calculator(self):
        current_time = self.time_entered_by_user
        alarm_wait = self.hours_to_wait 
        new_time = (current_time + alarm_wait) % 24
        ## While we are diplaying the time to make it more intutive I want to add the days elpased 
        days_passed = (current_time + alarm_wait) // 24
        return new_time, days_passed
    
    #funtion to output the time on a 24-hour clock
    def timePrinter(self):
        user_time_new, days_passed = self.alarm_time_calculator()
        user_time_new_formated = "{:02d}:00 hrs".format(user_time_new)
        if days_passed == 0:
            print('Alarm will go off at',user_time_new_formated,'today')
        else:
            print('Alarm will go off at',user_time_new_formated,'after',days_passed,'day(s)')

def main():
    current_time = int(input('Enter the current time in 24hrs format (0 - 23):'))
    alarm_wait_hrs = int(input('Enter number of hours to wait for alarm:'))
    alarm_time_calculated = alarmCalculator(current_time,alarm_wait_hrs)
    alarm_time_calculated.timePrinter()
    print(vars(alarm_time_calculated))

if __name__ == '__main__':
    main()
        
    
