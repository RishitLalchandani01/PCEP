### SCOPE NAME #### 
# scope = the lines in code where variable can properly be recogized and used
def show_truth():
  global mysterious_var # >>NOTE<<
  mysterious_var = 'New Surprise!'
  print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth() # if function ends all the variables in it are destroyed ... unless global
print(mysterious_var)

### SCOPE NAME #### 
# scope = the lines in code where variable can properly be recogized and used

def show_truth():
  global mysterious_var # >>NOTE<<
  mysterious_var = 'New Surprise!'
  print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth() # if function ends all the variables in it are destroyed ... unless global
print(mysterious_var)
