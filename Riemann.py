#Susan 

#1=trapezoidal 
#2=left 
#3=right 
#4=midpoint

import time

def f(x): 
  return (x**2 + 5*x + 2)
  
def riemann(lower,upper,n,type): 
  if type==1: 
    h = (upper-lower)/n
    sum= 0
    for i in range (1,n+1): 
      sum+= (f(lower+ i*h) + f(lower+ (i-1)*h))/2
    return(sum * h)
  if type==2:
    h = (upper-lower)/n
    sum= f(lower)
    for i in range (1,n):
      sum+= f(lower + i*h)
    return (sum * h)
  if type==3: 
    h = (upper-lower)/n
    sum= f(lower + h)
    for i in range (1,n): 
      sum+= f(lower + (i+1)*h)
    return(sum * h)
  if type==4:
    h = (upper-lower)/n
    sum= f(lower + h/2)
    for i in range (1,n): 
      sum+=f(lower + h/2 + i*h)
    return(sum * h)

while True:
  lower = float(input("lower?: "))
  upper = float(input("upper?: "))
  n = int(input("n?:"))
  type = float(input("type?:"))
  start = time.time()
  approx = riemann(lower,upper,n,type)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")

  
    