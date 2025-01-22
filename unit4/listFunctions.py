# List - a data type or collecting and organizing data
# - List can contain all data types, including other list
# - List are changable, we ca update the list
# - List can contain duplicate data.
# - we can get specific list itema based on its index position

#input is function that allows us  to enter data directly into
#our prograqm from the terminal
# data that is passed in from an input function automatically becomes
# a sting



name = input('what is your name ')
print(name)

# List functions



skii_TripItems = ['glove']
#insert() - allows us to enter a new list item
#based on an idex position
# Insert requires 2 arguments to work

skii_TripItems.insert(1,'snow boats ')
skii_TripItems.insert(2,'goggles')
print(skii_TripItems)

#append() - Allows us to eneter a new item into a list
# without having to provide and index location. append() will
# automatically put the new item at the end of the list.

skii_TripItems.append('scarf')
print(skii_TripItems)

#remove() - Allows us to remove an item from the list.
# It works by specifying what item you want to take out

skii_TripItems.remove('scarf')
print(skii_TripItems)

# pop( - Allows us remove the last item in a list )
skii_TripItems.pop()
print(skii_TripItems)

# clear/ del() - Allow us to delet/ remove all the
# list items

del skii_TripItems

skii_TripItems.clear()
print(skii_TripItems)
