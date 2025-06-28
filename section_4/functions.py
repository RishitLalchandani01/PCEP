# functions
# we have seen "in built" functions like print() and len() and input()


# what are functions ?
# they are seperate units of code that perform a specific task ... they are reusable.

# greet() # NameError: name 'greet' is not defined
def greet():
    print('Hello World!')

def greet_indian():
  print('Namaste Duniya!')
  
greet()
greet_indian()

# by default all functions return None
def multiplly(variable1, variable2) :
    # here we are not using return keyword nor printing... so it returns None by default
    var3 = variable1 * variable2
print(multiplly(2,3))

##### DEFALT PARAMETERS #####
# named arguments or keyword arguments ... always at end ... always optional and have default values
print('Hello', 'How are you?', end='.', sep='-')

# can define our own functions with input parameters (with our without default values) and return values
def add(variable1, variable2):
    #print(variable1 + variable2)
    return variable1 + variable2 # return is a keyword that returns the value and ends the function
    print("this will never be printed") # un reachable code

# NOTE : keyword return does two things 1) returns the value 2) ends the function ... a function can have only one return value

result=add(1,2)
print('\n',result)

def add_with_defaults(variable1=10, variable2=20):
  #print(variable1 + variable2)
  return variable1 + variable2

result=add_with_defaults() #use defaults
print('\n',result)

result=add_with_defaults(30,40) #overrides defaults
print('\n',result)

result=add_with_defaults(40,) #can use defaults only for last parameter
print('\n',result)

#result=add_with_defaults(,40) # cannot use defaults for first Params SyntaxError: invalid syntax
#print('\n',result)

# return
def get_average(input_numbers):
  sum = 0.0
  for number in input_numbers:
      sum += number
  average = sum / len(input_numbers)
  return average

print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')

get_average([2])

# note a function can only have one return value but multiple return statements
# note a function can have MULTIPLE return statements BUT only one will be executed (condiional)
def is_first_last_equal(number_list):
  if len(number_list) == 0:
      return
  if (number_list[0] == number_list[-1]):
      return True
  else:
      return False

print(is_first_last_equal([10, 20, 30, 40, 10]))

print(is_first_last_equal([10, 20, 30, 40, 50]))

print(is_first_last_equal([]))

### SCOPE NAME #### 
# scope = the lines in code where variable can properly be recogized and used

