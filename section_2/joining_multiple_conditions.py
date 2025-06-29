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
