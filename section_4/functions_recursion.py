'''
def SayHiInfinite(i):
  print("hi ",i)
  i+=1
  SayHiInfinite(i)

j=0
SayHiInfinite(j)
''' 

#recursion is a function calling it self

def SayHi10Times(i):
  SayHi10Times(i)
  if i<10:
    print("hi ",i)
    i+=1
  else :
    print("done")
    return

SayHi10Times(0)
print("end of program")
