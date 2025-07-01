# break, breaks the loop and goes to the next vlaue outside it
#continue is used to exit current iteration (including if but for break u can't) and not whole loop

'''while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
Enter your name or EXIT to close the program: Adam
Hello Adam
Enter your name or EXIT to close the program: Kate
Hello Kate
Enter your name or EXIT to close the program: EXIT
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
1
2
3
4
6
7
8
9
11
12
13
14
16
17
18
19'''

def break_loop():
  print("Starting outer for loop...")
  for i in range(3):  # Outer for loop iterates 3 times (i = 0, 1, 2)
      print(f"\nOuter loop iteration: i = {i}")
      j = 0
      while j < 5:  # Inner while loop
          print(f"  Inner loop iteration: j = {j}")
          if j == 2:
              print("  Breaking inner while loop!")
              break  # This only breaks the while loop
          j += 1
      print(f"Outer loop continues after inner loop (i = {i})")
  print("\nFor loop finished.")

break_loop()

#pass is used to just make an empty loop/OR CONDITIONAL as a loop with nothing in it gives error like so:
for i in range(2): #error

for i in range(2):
    pass # no error

for i in range(2):
  print("k")
  pass # no error , do nothing prints k twice

# remember loops can also have else statements simmilar to if's but key diff. in if statements the its either the if or else that runs in this type of else for loops it always runs while the main one may or may not run
i = 6
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)

#if i val is 5 or greater then else runs
#ONLY IF BREAK IS INSIDE MAIN BODY OF FOR OR WHILE THEN ELSE IS SKIPPED

while True:
  print ("hi")
  while True:
    print ("bye")
    break # only breaks out of the inner most loop
# in simple terms break exits loop
# break statement doesn't delete inner while loop js immediately stops it
