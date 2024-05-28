# Author: Jibran Gill
# Practicing with arrays
#Senario-1: Using a 1D array to store the result of Module Discussions for the CSC-500 Course
#importing the array module
from array import *

def main():
    #creating an array for storing the module discussion scores for CSC500-1
    num_of_discussions_modules = 8
    discussion_scores_array = array('f', [0.0] * num_of_discussions_modules)

    #Prompt the user to eneter the score for each module
    for x in range(num_of_discussions_modules):
        score = float(input(f'Enter the score for module {x+1}:\n'))
        discussion_scores_array[x] = score

    #Printing the Result for each module disccussion
    count = 1
    print('Discussion Assignment Results:')
    for x in range(num_of_discussions_modules):
        percentage_per_module = (discussion_scores_array[x]/ 30) * 100
        print('Score for Module -',count,'disccussion is',discussion_scores_array[x],'i.e. {:.2f}'.format(percentage_per_module),'%')
        count +=1
    
    #calaulating average of scores for all modules
    total_score = sum(discussion_scores_array )
    average_score = total_score/num_of_discussions_modules
    print('Total score of all module discussions: ',total_score)
    print ('Average Score of all module discussions: {:.2f}'.format(average_score))
if __name__ == "__main__":
    main()