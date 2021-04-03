n, B = list(map(int, input().strip().split()))
T = 0

# your code here
x = 0
x = int(x)
notfound = -1 
for i in range(1,n+1):
  if i%2 == 1:
    p = 3**i + 1 
  else:
    p = 2**i + 1
  
  x += p**(n-i)
 
for T in range(1,10000):
  if x * T > B: 
    print(T)
    break
  else:
    T += 1 

if T not in range(1,10000):
  print(notfound)

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
#print(T)