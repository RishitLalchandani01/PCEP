# generators are functions that return a sequence of values ... they generate values one by one and only when needed
# generator is an object that can be iterated over
# whenever you use yield instead of return. The function will return a generator object, which can be iterated over to produce the values one by one.

def simple_generator_function():
  yield 1
  yield 2
  yield None
  yield 4
  yield 5

#IMP: return ends the function while, yield just pauses it

generator_obj=simple_generator_function()
print(next(generator_obj)) #1
print(next(generator_obj)) #2
#print(next(generator_obj)) #None
#print(next(generator_obj)) #4
#print(next(generator_obj)) #5
# print(next(generator_obj)) # error : StopIteration , no 6th element to return

# in layman terms ... Generator puts things in a pipe / queue and next pulls them out one by one as needed 
# if you put 5 things in generator you can pull them out max 5 times
print("Next example\n")
# you can also use for loop to iterate over generator
x=True
for x in simple_generator_function():
  print(x)
