# there are two ways to raise exception by ourselves, in PCEP you only need to know the first one "AssertionError"

 # Assertions are certain assumptions that we make in our code, and if they are wrong, we want to raise an error
# https://www.geeksforgeeks.org/python/python-assertion-error/ 
def calculate_inverse(number):
  assert (number != 0), 'Got 0 as number!'
  return 1/number

print(calculate_inverse(5)) # ok  
print ("\nnext\n")
calculate_inverse(0) # will raise AssertionError
