x=10

def fun1():
    # print(x) # Syntax error because x is not defined in the local scope
    global x
    x=20
    print(x)

print(x)
fun1()
print(x)
