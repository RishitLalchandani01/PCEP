def concept_1():
  d1 = {"sandy":35, "surname":"Kate"}
  d2 = {"surname":"Kate", "sandy":35}
  print(d1 == d2)

concept_1()

def concept_1_explaination():
  # The dictionary does not have a fixed order. 
  # Although, the order varies but the key-value pairs are the same so they are the same.
  d1 = {"sandy":35, "surname":"Kate"}
  d2 = {"surname":"Kate", "sandy":35}
  print(id(d1)) # prints memory location
  print(id(d2)) # prints SAME memory location
  print(d1 == d2)
