# if < condition > :
#   < do something >
# elif < condition > :
#   < do something >
# else :
#   < do something >
# where < condition > is boolean expression that results in True or False

# user_age = int(input('What is your age? '))
#if user_age = 30: # error : SYNTAX ERROR : will not run : expression cannot be assignment target
#  print('You are 30 years old')
#elif:
#  print('You are not 30 years old')
  
''' 
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
    print('You will be contacted if you are selected for the trial')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
'''
''' 
# True is a boolean constant in Python , like 1 , 2 , 3 , 4 etc. or a b c d etc.
if True:
 print('This will always run')
elif False:
    print('This will never run')
else:
     print("This will never run either")

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
