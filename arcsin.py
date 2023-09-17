# integration of 1 / sqrt 1 - x^2 = arcsin x
# Qing Yi

import time

def f(x): 
  return float(1) / ((1 - (x**2))**0.5)
  
def integrate(a,b): 
  n=1000000
  h = (b-a)/n
  sum= 0
  for i in range (1,n+1): 
    sum+= (f(a+ i*h) + f(a+ (i-1)*h))/2
  return sum * h

def arcsin(x):
  return integrate(0,x)

# cannot do when x = 1 because thats the upperbound for arcsin
# says it's dividing by 0 when x = 1
# we have to calculate a one sided limit when x = 1 or close to 1
# unaccurate when x = 0.99999999999...
# otherwise very accurate when well below 1 like x = 0.2

while True:
  value = float(input("What x?: "))
  start = time.time()
  approx = arcsin(value)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")