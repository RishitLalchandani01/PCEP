# you cannot put 2 values in a variable , they get overridden  
number = 2
number = 3
print(number)
# python offers container types to hold multiple values ... or collections

# Ideally All lists elements should be of same type
grocery_list = ['apple','bread','cinnamon','donuts']


# lists are ordered set of elements .... each element has an index
print(grocery_list[0]) # note :- starts with 0
print(grocery_list[1]) # 
#print(grocery_list[4]) # IndexError: list index out of range
print(grocery_list[-1]) # works, prints donuts from end
print(grocery_list[-2]) 
#print(grocery_list[-5]) # IndexError: list index out of range
print("\n####### #######\n")
# in below first element is element to include , second is element to exclude 
print(grocery_list[0:2]) # NOTE :- Slicing : 0:2 is 0,1 prints two elements ['apple', 'bread'] not three
print(grocery_list[1:2]) # NOTE :- only one element ['bread'] is printed
print(grocery_list[1:1]) # NOTE :- prints empty list [] 
print(grocery_list[-1:-2]) 
print(grocery_list[1:]) # print all elements from 1 to end 
print(grocery_list[:3]) # print all elements from start to 2 (3 excluded)
print(grocery_list[10:15]) # print empty list [] 
# SLICING gives you a new list
x=1
print(grocery_list[x]) # can use variables to print a particular element
############
y = 1
y = [2,3,4]
print(y) # will give the list 

#for(x=0;x<4;x=x+1):
#  print(grocery_list[x])

# working with multiple variables is not easy
city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'

# can combine them into a list
print("\n####### #######\n")
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
top_cities_2 = [city_1,city_2,city_3,city_4,city_5]
print(top_cities_2)
print("\n####### #######\n")

# lists can be empty 
empty_list = []
print("Here is empty list [",empty_list,"]")


boolean_list = [True,False,True,False]
print(boolean_list)
# technically nothing is stopping them to be of different types 
################  DELETE FROM A LIST  #################
## note del is not a function call , it is a instruction as no argument is passed  

top_cities = ['New York City', 'Los Angeles','Delhi' 'Chicago', 'Houston', 'Phoenix']
del top_cities[2] # what happened to the deleted space ? all values after 2 are shifted to left
print(top_cities)

top_cities = ['New York City', 'Los Angeles','Delhi' 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:] 
print(top_cities)
# ['New York City', 'Los Angeles', 'Singapore']

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
print(top_cities)
#[]

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities # deletes the list itself
print(top_cities)
# NameError: name 'top_cities' is not defined
