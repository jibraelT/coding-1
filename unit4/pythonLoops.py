# create a function that will determine what year a college student
# is in based on the number of years they've been to school

# function definition
def titleBySchoolYear(year):
    if year == 1:
        print('Im a freshmen')
    elif year == 2:
         print(" Im a sophmore")
    elif year == 3:
         print(" Im a junior")
    elif year == 4:
          print(" Im a senior")
    elif year == 5 or year == 6:
         print("your in grade school attaining your masters degree ")
    elif year == 7 or year == 8:
         print(" your in grade school attaining your doctorate")

titleBySchoolYear(7)

# list are a datatype for collecting and grouping together
#other places of data

#create list using the square brackets


groceryList= ['greens','paper towels','water']
tiktok =['username','dateOfBirth',50,20]

educationStatus =['freshmen','sophmore','junior','senior']
print(educationStatus[2])