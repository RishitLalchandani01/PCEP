### SCOPE NAME #### 
# scope = the lines in code where variable can properly be recogized and used
def show_truth(mysterious_var):
 # mysterious_var # >>NOTE<<
  mysterious_var = 'New Surprise!'
  print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth(mysterious_var) # if function ends all the variables in it are destroyed ... unless global
print(mysterious_var)
