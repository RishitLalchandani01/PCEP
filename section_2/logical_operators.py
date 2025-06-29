def logical_operator_expirement_1():
  if 2 == 2:
    print('true')
  # true
  if 1 == 2:
    print('true')
  # nothing
  if 2 == 2.0:
    print('true')
  # true, because python automatically converts 2 to 2.0 making 2.0==2.0

def logical_operator_expirement_2():
  password = input('Do you know the secret pasword? ')
  if password == 'secret':
      print('correct')
  else:
      print('in correct password')

# call the function you want
logical_operator_expirement_2()
