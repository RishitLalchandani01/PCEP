# if < boolean condition > :
#   < do something >
# elif < boolean condition > :
#   < do something >
# else :
#   < do something >


# user_age = int(input('What is your age? '))
#if user_age = 30: # error : SYNTAX ERROR : will not run : expression cannot be assignment target
#  print('You are 30 years old')
#elif:
#  print('You are not 30 years old')
  
''' 
if user_age > 30 :
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
    print('You will be contacted if you are selected for the trial')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are younger than 30 years')
    print('Congratulations, you qualify!')
'''
# you can use AND , OR , NOT in boolean expressions
age = int(input("Enter your age: "))

if age >= 0 and age <= 9:
    print("You are a child!")
elif age > 9 and age <= 18:
    print("You are an adolescent!")
elif age > 18 and age <= 65:
    print("You are an adult!")
elif age > 65:
    print("Golden ages!")

def answer():
 ans = input('Do you...? (yes/no): ')
 if ans.lower() == 'yes' or ans.lower() == 'y':
   print(f'Positive answer: {ans}')
 elif ans.lower() == 'no' or ans.lower() == 'n':
   print(f'Negative answer: {ans}')

def divide(a, b):
    if not b == 0:
        print("b is not 0, dividing")
        return a / b
    else:
       print("b is not 0, cannot divide")

divide(10,5)
divide(10,0)
''' 
# True is a boolean constant in Python , like 1 , 2 , 3 , 4 etc. or a b c d etc.
if True:
 print('This will always run')
elif False:
    print('This will never run')
else:
     print("This will never run either")
if -1:
  print("truthy")
elif 0:
  print("true")
else:
  print("falsy")
# 1 is True in Python , like True , 0 is False in Python , like False
# ACTUALLY 0 is False , non zero is True

if 1:
 print('This will always run')
elif 0:
    print('This will never run')
else:
     print("This will never run either")
'''
'''
if 21:
    print('This will never run')
else:
    print('This will always run')
''' 
if 0:
  print('xxxx')
else:
  print('yyyy')

if -1:
  print("truthy")
elif 0:
  print("true")
else:
  print("falsy")
''' 
# The Basics
is_old=False # assignment statement
is_licensed=True
if is_old: # note the : , can use 'and' 'or' etc.
  print ("old enuf to drive")
elif is_licensed: # note the :
  print ("drive safely")
# elif <more_condition>
else :
  print ("too young")
  print ("choose a good driving school")
'''
''' 
# Type Conversion for boolean  
bool_val=True
num_as_bool=5
if bool_val and num_as_bool :
  print ("number treated as true") 
else:
  print ("number NOT treated as true")
print("Truthy is="+str(bool(5))) # truthy values in pthon


# More Truthy...
password='secret'
username='myname'
if password and username:
  print("thank you for giving username and password")
else:
  print("please provide username and password")

print("end of program")
'''
