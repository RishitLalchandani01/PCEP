# Question 6: : What will be the output of the following code?

def func(a):
   global b
   b = a + a
   return b

b = 10
print(func(13))
print(b)

# The global keyword inside the function means that we'll be modifying the global b variable, even outside the function. That means both print invocations will return 26.

