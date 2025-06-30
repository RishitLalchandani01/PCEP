# Point 1
# A tuple in Python is an ordered collection of items, similar to a list, but with a key distinction: immutability. 
# This means that once a tuple is created, its elements cannot be changed i.e. (i) append, or (ii) del.
# IMP: list mutable while tuple immutable


# point 2
# they are created with ( )
def tuples_1():
  empty_tuple = () 
  one_element_tuple_a = (1,) # NOTE : if tuple has 1 element , is needed 
  one_element_tuple_b = 1, # NOTE () is optional but , is not ONLY for first value as if not put it might confuse for integer
  three_el_tuple = 1, 2, 3 # Notices how now , is necessary (also when it is printed it is with ()) also wether if you put , or not at the end sme result # (1, 2, 3)
  print(three_el_tuple)

def tuples_2():
  user_data = ('John', 'American', 1964)
  #user_data = ('John', 'American', 1980)
  user_data = ('Katya', 'Russian', 1980) #only way to change a tuple without adding or removing a value is by reassigning 
  #user_data.append('teacher') #AttributeError: 'tuple' object has no attribute 'append'
  print(user_data)



# indexing and slicing is possible with tuples but indexing cannot be used to change values
def tuples_indexing_slicing():
  user_data = ('John', 'American', 1964)
  print(user_data[0])
  #Output: John
  print(user_data[0:2])
  #user_data[0] = 'Mark' # TypeError: 'tuple' object does not support item assignment

#Strings are immutable, as you can access specific characters but cannot change them.
#indexing and slicing is possible with strings but indexing cannot be used to change values, simmilar to tuples (same errror)
def strings_indexing_slicing():
  x="hi person"
  print(x[0])
  print(x[0:5])

# len() always retusrns a int.
def print_tuple_len():
  user_data = ('John', 'American', 1964) #3
  print(len(user_data))
  user_data = ('John', 'American', 1964,"qwer") #4
  print(len(user_data))

def check_if_in_tuple():
  user_data = ('John', 'American', 1964, 2.12, True)
  if True in user_data:
      print('This person comes from the US!')
  elif 2.12 in user_data:
    print('This person comes from the US!')
#notice how only first statement is printed and not both as both are true but the first one is true so it stops there
    
check_if_in_tuple()

def tuple_iteration():
  user_data = ('John', 'American', 1964)
  for element in user_data:
      print(element)
  #John
  #American
  #1964
#tuples can have different data types like list, dict, str, int, float, etc.                              


  
def tuple():
  user_data = ('John', 'American', 1964) + ('teacher', 'male') #behind the scenes it creates a new tuple as adding to a tuple is not possible
  print(user_data)
  #('John', 'American', 1964, 'teacher', 'male')
  numbers = (0, 1) * 10
  print(numbers)
  #(0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
  #another example of string showing the similarity between tuples and strings
  x="a"*10
  print(x)
  #aaaaaaaaaa

x=1,
print(x)
#prints (1,) as it is a single value meaning the , shows in any other case it would not.

def list_x_tuple():
  city_1 = ('London', 'UK', 8.98)
  city_2 = ('Canberra', 'Australia', 0.4)
  city_3 = ('Algiers', 'Algeria', 3.9)
  capitals_1 = [city_1, city_2, city_3]
  for capital in capitals_1:
      #print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
       print('Name:', capital[0])

def list_inside_list():
  city_1 = ['London', 'UK', 8.98]
  city_2 = ['Canberra', 'Australia', 0.4]
  city_3 = ['Algiers', 'Algeria', 3.9)
  capitals_1 = [city_1, city_2, city_3]
  for capital in capitals_1:
      #print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])
       print('Name:', capital[0])
    
# if list (muttable data) in tuple then you can still change the list by append or del
def tuple_x_list():
  user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
  user_data[3].append(79.6)
  print(user_data)
  user_data = ('John', 'American', 1964, "hello")
  #user_data[3].append(" world") # AttributeError: 'str' object has no attribute 'append'
  #user_data[3] += "world" # TypeError: 'tuple' object does not support item assignment
  print(user_data)

tuple_x_list()
  
