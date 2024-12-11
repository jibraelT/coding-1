#functions are just instructions to be used on data

#Conditionals use the if/ else keyword to make decisions
#and outcomes based on data

def elevatorLogic(floor):
 #1. take in user input/ user data
 
 #2. determine which floor they want to go based on input
 if floor == 'b':
    print('you are getting to the basement.')
 elif floor == '1':
  print('you are going to the first floor')
 elif floor == '2':
  print('you are going to the second floor')
 elif floor == '3':
  print('you are going to the third floor')
 elif floor == 'r':
  print('you are going to the rooftop')
 else:
   print('floor does not exist')
 #3. print and return the correct floor based on there input
 
elevatorLogic('b')


# create a function taht will give someone a letter grader based on their 
#numerical grade score. for example, if some has a 50, your program should print
#you have an A, if the data entered is an 80
# the program should print you have a B.

def gradingSystem(letter):
 if letter == 'A':
  print('you should have a 90%')

 elif letter == 'B':
  print('you should have a 80% ')
 elif letter == 'C':
  print('you should have a 70% ')
 elif letter == 'D':
  print('you should have a 60% ')
 elif letter == 'F':
  print('you should have a 50% ')


gradingSystem('A')