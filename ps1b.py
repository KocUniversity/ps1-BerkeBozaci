n, B = list(map(int, input().strip().split()))
T = 0

# your code here
x = 0 
low = 0 
high = 10000
avr = (high + low)/2

for i in range(1,n+1):
  if i%2 == 1:
    p = 3**i + 1 
  else:
    p = 2**i + 1

  x += p**(n-i)

for T in range(1,10000):
  while x * T > B:
    if T > avr:
      low = avr 

    elif T < avr:
      high = avr 

    else:
      print(T)
      break 
    
    avr = (high + low)/2

T = -1
print(T)   



# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
#print(T)