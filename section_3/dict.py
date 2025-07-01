def dict_1():
  # dictionary is key value pair
  dict_one = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3'
  }
  dict_one = {
    1.0 : 1,
    'python' : 2.0,
    3.0 : 3
  }
  #print(dict_one[2.0]) # access any element , as long as you know the key ... you dont have to access by index
  
  
  traffic_lights = {
    'red': 'stop',
    'yellow': 'wait',
    'green': 'go'
  }
  print(traffic_lights['yellow'])

def dict_2():
  dict_implicit_conversion = {
    1.0 : 1,
    2 : 2.0,
    3.0 : 3
  }
  print(dict_one[2.0]) # access any element , as long as you know the key ... you dont have to access by index
#notice how python is able to convert 2 to 2.0 automatically

def dict_2():
  dict_implicit_conversion = {
    1.0 : 1,
    1.0 : 1,
    3.0 : 3
  }
  print(dict_implicit_conversion) # note : 2 elements only, notice no errors even thought keys are same


def dict_3():
  dict_implicit_conversion = {
    1.0 : 1,
    1.0 : 2,
    3.0 : 3
  }
  print(dict_implicit_conversion) # 2 value overrides first, also only 2 elements printed
dict_3() 
#always {} for dict. 
#can have any data type as key and value
#key:value, key2,value2, key3:value3 (like dict_one above)
#key should be unique or else it overrides the value
#can only call by key not value, one way tool

#keys can be any other immutable data type like tuple, string, number but not list
#values can be immutable or mutable data types
x=[7, 4, 7, 5]
y=[7, 6, 4, 5]
z=[6, 6, 4, 4, 5]

def city_ratings_01():
  city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
    }
  print(city_ratings)


def dict_operations():
  grades = {} #empty dict.
  grades['John'] = 'A-'  #add key-value pair
  grades['John'] = 'A'  #update key-value pair
  grades.update({'John':'A'}) # or update key-value pair
  print(grades)
  print(len(grades)) #1
  print(grades['John']) #to get value A
  del grades['John'] #to delete key-value pair
  print(grades) #empty dict.
  
  del grades
  print(grades) #UnboundLocalError: local variable 'grades' referenced before assignment because grades is deleted


def dic_iterate():
  grades = {
    'John': 'A-',
    'Jane': 'B+',
    'Jill': 'A',
    'Jack': 'A+'
  }
  # 2 ways to prit keys
  for el in grades:
    print(el)
  for el in grades.keys():
    print(el)
  
  # 2 ways to prit values
  for el in grades:
    print(grades[el])
  for el in grades.values():
    print(el)

  for person, grade in grades.items():
    print(person, 'got', grade)

dic_iterate()
