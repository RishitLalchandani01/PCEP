def slicing_creates_new_list():
    list_original = [1, 2, 3]
    list_new = list_original[:]
    list_original[0] = -5
    print('Original:', list_original, '\nNew:', list_new)
    #this would now print different lists as the original list was copied to the new list as when slicing is used, a new list is created

def appending_to_lists():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    print(numbers)

def appending_to_lists_2():
    # List Comprehension, same thing as above
    # how does this work? https://www.youtube.com/watch?v=AhSvKGTh28Q&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=22
    numbers = [i for i in range(1, 101)]
    print(numbers)

def appending_to_lists_3():
    numbers = [i for i in range(1, 101) if i % 3 != 0]
    print(numbers)
    
def list_of_lists_1():
    cells = [['A1', 'A2'], ['B1', 'B2', 'B3']] #if you did len of this, it would be 2
    #print(cells[0]) #accessing the first sub-list
    #print(cells[0][0]) #accessing the first element of the first sub-list
    # if you use [x][y] you are accessing the xth sub-list and the yth element of that sub-list 
    # but [x] only gives you the xth sub-list
    # x starts with 0, y starts with 0
    print(cells[-1]) #['B1', 'B2', 'B3']
    print(cells[-1][-1]) #B3

def traversing_lists_1():
    cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
    for x in cells:
        print('Element:', x)


def traversing_lists_2():
    cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
    for x in cells:
        for y in x:
            print('Element:', y)

def traversing_lists_3():
    table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
    for row in table:
        for cell in row:
            print('Element:', cell)

def traversing_lists_4():
    table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
    for row in table:
        for cell in row:
            print(cell, '', end='') # same line
            #print()

def traversing_lists_4_1():
    table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
    for row in table:
        for cell in row:
            print(cell, '', end='') 
        print() # diff line

def traversing_lists_5():
    # i is inner loop, j is outer loop
    table = [[i for i in range(1, 6)] for j in range(4)]
    print(table)

def list_add_string():
    list_us = ['New York City', 'Chicago']
    list_uk = ['London', 'Bristol']
    list_all = list_us + list_uk
    print(list_all)

def list_add_ints():
    list_us = [1,2,3]
    list_uk = [4,5,6]
    list_all = list_us + list_uk
    print(list_all)
    
def list_multiply_ints():
    list_us = [1, 0]
    list_us = list_us * 3
    print(list_us)

def list_multiply_str():
    list_us = ["one", "two"]
    list_us = list_us * 2 # only works with ints
    print(list_us)
# NOTE you can create 3 or 4 dimensional lists

list_add_ints()
#appending_to_lists_3()
#list_of_lists_1()
