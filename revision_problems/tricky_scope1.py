my_list = ['aaa', 'bbb', 'ccc']

def do(my_list):
  # passing a reference of my list not a copy of it 
   del my_list[1]
   my_list[1] = 'aaa'
   print(my_list) 

do(my_list)
print("outside")
print(my_list) 
