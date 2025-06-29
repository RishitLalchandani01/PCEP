while 1==2:
  print ("hello")
while False:
  print ("bye")

while True:
  print ("hi")
  break # only breaks out of the inner most loop 
  # break helps end while and for loops


while True:
  print ("hi")
  while True:
    print ("bye")
    break # only breaks out of the inner most loop


''' 
while True:
  print ("hi")
  if True:  # not a loop , it is a condition
    print ("bye")
    break # only breaks out of the inner most loop

''' 

'''   
number = 0
while number < 10:
  print (number)
  number += 2

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')

# note how it prints number from only 1-10 and DOESN'T INCLUDE 11 because it is < 11 same as <= 10
increasing by 1 speciically is callled incementation

good example: Secret  number game
'''
secret_number = 14
print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')
print ("end of program")


NOTICE HOW ''' is used to comment and duriing the print command to print multiple lines at once instead of using \n over and over again
