# you can use AND , OR , NOT in boolean expressions
def using_and_1():
  age = int(input("Enter your age: "))
  if age >= 0 and age <= 9:
      print("You are a child!")
  elif age > 9 and age <= 18:
      print("You are an adolescent!")
  elif age > 18 and age <= 65:
      print("You are an adult!")
  elif age > 65:
      print("Golden ages!")

def answer_using_or():
 ans = input('Do you...? (yes/no): ')
 # NOTE : python evaluates the expression from left to right 
 # and stops as soon as it finds a true value i.e. first true value
 if ans.lower() == 'yes' or ans.lower() == 'y':
   print(f'Positive answer: {ans}')
 elif ans.lower() == 'no' or ans.lower() == 'n':
   print(f'Negative answer: {ans}')

# not of true false
# not of false is true
def divide_using_not(a, b):
    if not b == 0:
        print("b is not 0, dividing")
        return a / b
    else:
       print("b is not 0, cannot divide")

# call 
#divide_using_not(10,5)
#divide_using_not(10,0)
#answer_using_or()
using_and_1()

# NOTE : you can use 'back' slash \ if your lines of code are too large

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if not user_country == 'Germany' and user_age < 25 or \
   user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify!')

# Operator Precendence : NOT , AND , OR
# in above line 41 , first python will evaluate NOT of country , then AND ... if it is true do not eval OR part
# https://docs.python.org/3/reference/expressions.html#operator-precedence 
# https://stackoverflow.com/questions/16679272/priority-precedence-of-the-logical-operators-order-of-operations-for-not-an 
def order_of_logical_operators():
  a = 'apple'
  b = 'banana'
  c = 'carrots'
  if c == 'carrots' and a == 'apple' or b == 'BELGIUM': # True
    print('one')
  else:
    print('not one')
  
  # Note this one, which might surprise you:
  if c == 'CANADA' and a == 'apple' or b == 'banana': #True
    print('two')
  else:
    print('not two')
  
  # ... it is the same as:
  if (c == 'CANADA' and a == 'apple') or b == 'banana': #True
    print('three')
  else:
    print('not three')
  
  if c == 'CANADA' and (a == 'apple' or b == 'banana'): #FALSE
    print('four')
  else:
    print('not four')
  
  if c == 'CANADA' and a == 'apple' or b == 'BELGIUM': #False
    print('five')
  else:
    print('not five')
    
  if c == 'CANADA' or a == 'apple' and b == 'banana': #True
    print('six')
  else:
    print('not six')
  
  if c == 'CANADA' or (a == 'apple' and b == 'banana'): #True
    print('seven')
  else:
    print('not seven')
  
  if (c == 'carrots' and a == 'apple') or b == 'BELGIUM': #True
    print('eight')
  else:
    print('not eight')
    
  if c == 'carrots' and (a == 'apple' or b == 'BELGIUM'): #True
    print('nine')
  else:
    print('not nine')
    
  if a == 'apple' and b == 'banana' or c == 'CANADA': #True
    print('ten')
  else:
    print('not ten')
    
  if (a == 'apple' and b == 'banana') or c == 'CANADA': #True
    print('eleven')
  else:
    print('not eleven')
    
  if a == 'apple' and (b == 'banana' or c == 'CANADA'): #True
    print('twelve')
  else:
    print('not twelve')
  
  if a == 'apple' and (b == 'banana' and c == 'CANADA'):# False
    print('thirteen')
  else:
    print('not thirteen')
    
  if a == 'apple' or (b == 'banana' and c == 'CANADA'): #True
    print('fourteen')
  else:
    print('not fourteen')

order_of_logical_operators()
