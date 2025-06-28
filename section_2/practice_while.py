while 1==2:
  print ("hello")
while False:
  print ("bye")

while True:
  print ("hi")
  break # only breaks out of the inner most loop


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
'''

print ("end of program")
