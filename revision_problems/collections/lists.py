def using_is():
  l1=['a','b','c']
  # if you append l1.append('d') then it is obvious that l1 is not l2
  l2=['a','b','c']
  l3=l2
  print(l1 is l2)
  print(l1 is l3)
  print(l3 is l2)

  print(l1==l2)
  print(l1==l3)
  print(l3==l2)

def slicing():
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  # Slice with a step of 2
  sliced_list = my_list[::2]  # [1, 3, 5, 7, 9]
  # Reverse the list using a step of -1
  reversed_list = my_list[::-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  # Slice from index 1 to 7 with a step of 3
  specific_slice = my_list[1:8:3]  # [2, 5, 8]

def pop_vs_remove():
  mylist = ["a", "b", "c"]
  mylist.remove("c")  # removes the first element that has value "c"
  mylist.pop(1)  # removes element 1 from the list (remember indexing starts at zero)
  # in pop index is optional
