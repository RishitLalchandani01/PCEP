# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
# Exceptions always stop program execution


# there are many types of exceptions
# 1: Syntax Error : example IndentationError

'''
if True:
print('hooray!')
  File "xxxx.py", line 2
    print('hooray!')
    ^
IndentationError: expected an indented block
'''


# 2 : (Runtime Error) : Value Error : Error when code is syntactically correct but some runtime values result in error 
''' 
value = int(input('Enter an integer: '))
print('The inverse of', value, 'is', 1/value)
Enter an integer: a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~ xxx.py in <module>
----> 1 value = int(input('Enter an integer: '))
      2 print('The inverse of', value, 'is', 1/value)

ValueError: invalid literal for int() with base 10: 'a'
'''

#try except block
# try : try to run this code
# except : if there is an error, run this code
#always do indentation in try except blocks

try:
  value = int(input('Enter an integer: '))
  print('The inverse of', value, 'is', 1/value) # if errorr this wont be executed
  print('if no error, this will be executed')
except ValueError:
  print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
  print('You provided 0 and division by 0 is not possible, sorry')
except:
  print('Something strange happened here, sorry')

#value = int(input('Enter an integer: '))
#print('The inverse of', value, 'is', 1/value)
''' 
try:
  5:4 # this line generates a SyntaxError
except SyntaxError:
  print('Got it!') # SyntaxError is NOT caught here
'''
# this is because in the example above, the user is the one who is providing the code/entering a value while in the above case, the code is already written in the program and the user is doing nothing wrong
