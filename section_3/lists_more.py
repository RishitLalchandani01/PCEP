def list_append():
  book_ratings = [7, 9, 5, 6, 8]
  book_ratings.append(4)
  # note append is a method (it belongs to the list, they are invoked with a dot / period (.) after data) 
  # method is a special type of function
  print(book_ratings)
  # if you try to call append(4) without the dot wihtout list name, it will throw a NameError

def list_insert():
  book_ratings = [7, 9, 5, 6, 8]
  book_ratings.insert(1, 10) # insert AT index 1
  print(book_ratings) # [7, 10, 9, 5, 6, 8]
  book_ratings.insert(-1, 11) # insert AFTER index -1
  print(book_ratings) # [7, 10, 9, 5, 6, 11, 8]

def list_iterate():
  # FIRST WAY TO ITERATE
  top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
  for city in top_cities:
      print('Current city:', city)
  # SECOND WAY TO ITERATE
  top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
  for city_index in range(len(top_cities)):
    print(city_index)  
    print('Current index:', city_index, '| Current city:', top_cities[city_index], )

def lists_vs_dict():
  grocery_list = ['apple','bread','cinnamon','donuts']
  print(grocery_list[2]) # index based access, index starts with 0 
  grocery_list = {'apple':'bread','cinnamon':'donuts'}
  print(grocery_list['cinnamon']) # key based access
  # https://www.youtube.com/watch?v=YhDI2btcWeU
  # range returns a series of value
  # that is then stored in x one by one
  for x in range(5): # 0,1,2,3,4
    print(x)

def list_sum():
  spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
  sum = 0.0
  for y in range(5):
   sum = sum + spendings[y]

#sort is used to put in alphabetical order if string and increasing order if int, if it is a collection of strings with numbers in it then it also puts that increasing order as shown in 50-52
#to reverse it simply say .sort(reverse=True) set it equal to false to undo
#sort is a method
def sort_backward():
  random_numbers = [2, 5, 0, -3, 4]
  random_numbers.sort(reverse=True)
  print(random_numbers)
  random_numbers.sort(reverse=False)
  print(random_numbers)

def list_sort():
  random_numbers = ["1", "2", "-1", "-3", "4"]
  random_numbers.sort()
  print(random_numbers)

#since sort is a method it sorts the original list and changes it
#while sorted is a function it returns a new list, but keeps the original list the same

def list_sort2():
  random_numbers = ["1", "2", "-1", "-3", "4"]
  print(sorted(random_numbers))



#2 ways used to swap
#way 1
def swap_with_third_variable():
   first = input('Enter first number: ')
   second = input('Enter second number: ')
   print('Before swapping:', first, second)
   temporary = first
   first = second
   second = temporary
   print('After swapping:', first, second)
#way 2
def swap_with_tuples():
  top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
  top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
  '''here it is set to tuple''' 
  print(top_cities)
  
#lists_vs_dict()
#list_insert()

#in can be used outside for loop as show below
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
#can also do it other way around with help of not
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')



name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)


list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
#both would print the same thing while for strings it would print the original and new

#because the name of the list is the name of the memory location of the list and not the list itsel, called references as they reference the memory location
#here the name of the list is assinged the same memory location as the other list, so when the list is changed the other list is also changed
