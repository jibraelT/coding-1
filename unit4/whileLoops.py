# Loops - is a construct that repeats a set of
# instructions under specific conditions.


# while - so long as a condition is true
# keep repeating the rules
x = 2
y = 'ian'

# while x == 2:
# while y == 'ian'
while 10 < 1:  
   
          
  def tripSavings():
    accountBalance = 0 
    tripgoal= 8000    
    while accountBalance < tripgoal:
         depositAmount = int(input('how much do you want to deposit'))
         accountBalance += depositAmount 
    print( ' Your new account balance is '+ str (accountBalance))

    tripSavings() 