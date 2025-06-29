#basic diff. between for and while loop is that in for loop you know end and start , in while loop continues until a given condition  is false / true

for letter in 'hello!':
    print('Current letter:', letter)

# firs time you run this value of letter is h and second time e and so on...

for counter in range(1, 11):
    print(counter)
print('Finished!')

# last val is never included
# same as while from before 

#if u say rang(11) assumes start val. is 0 and end is 11 (given) will give values from          0-10 pay atention last is never included
for counter in range(1, 11, 4):
    print(counter)
print('Finished!')
'''1
5
9
Finished!  4 is increasing interval'''

#note only int values in for loop no float
