def positiveNegative(numbers):
 if numbers > -2:
  print('if number is less than 0 it is a negative')
  
 elif numbers == 0:
   print('this is 0 ')
 
 elif numbers < 1:
         print('if number is greater than 0 it is a positive ')
 

positiveNegative(-2)
positiveNegative(0)
positiveNegative(1)



def shoppingDiscount(membership,itemName,itemPrice):
 if membership == 'superShoper': 
    discountAmount = itemPrice =0.1
    finalAmount = itemPrice -discountAmount
  