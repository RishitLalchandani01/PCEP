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
