def numerical():
  for i in range(10):
    yield i%2
 
for x in numerical():
  print(x, end='-')
