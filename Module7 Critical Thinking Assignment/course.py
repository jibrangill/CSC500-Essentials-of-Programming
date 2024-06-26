#Author: JIbran Gill
'''
Program creates three dictionaries. All the dictionaries have the course number as key. 
Values in dictionaries are room number, instructor name and the meeting time. User can retrieve this qinfomartion 
by entering the course number. The program will display the Course Number, meeting room number, name of instructor
and the meeting time
'''
def main():
    # Creating dictionaries for course information
    #Added a test course CSC104 in room_numbers. This is missing in dict instructors and meeting time
    #Program will check if the course is added in all three dictionaries. If not it will print what information of dictoinaries missing the info
    room_numbers = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411',
        'CSC104': '1254'
    }
    
    #Dictionary for couse to instructor mapping
    #test course CSC242 is added which is misisng in other two dictionaries.
    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee',
        'COM242': 'Spiderman'
    }
    
    #Dictionary for meeting times
    #test course NET120 is added here which is missing in other two dicts. Program will verify if the course is preent in all three dicts and notify user if not
    meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.',
        'NET120': '2:00 pm.'
    }

    while True:
        # Getting input from user
        course_number = input("Enter a course number (or 'q' to quit): ").strip().upper()
        
        # Check if user wants to quit
        if course_number == 'Q':
            print("Exiting program. Goodbye!")
            break
        
        # Check if the course number is valid
        missing_info = []
        
        if course_number not in room_numbers:
            missing_info.append("Room number")
        if course_number not in instructors:
            missing_info.append("Instructor")
        if course_number not in meeting_times:
            missing_info.append("Meeting time")
        
        if not missing_info:
            print()
            print(f"Course Number: {course_number}")
            print(f"Room Number: {room_numbers[course_number]}")
            print(f"Instructor: {instructors[course_number]}")
            print(f"Meeting Time: {meeting_times[course_number]}\n")
        else:
            print(f"\nInvalid or incomplete course information.\nMissing Information: {', '.join(missing_info)}.\nPlease enter a valid course number or 'q' to quit.\n")


if __name__ == "__main__":
    main()