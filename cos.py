# power series
# Qing Yi and Susan 

import time


def factorial(x):
  a = 1
  for i in range(1, x + 1):
    a *= i
  return a


def absolute(number):
  if number < 0:
    return number * -1
  else:
    return number


def cos(x, digits):
  next = 1
  old = 0
  n = 0
  error = (0.1)**(digits + 1)
  while absolute(next - old) >= error:
    add = ((-1)**n) * ((x**(2 * n)) / (factorial(2 * n)))
    old = next
    next += add
    n += 1
  return next - 1

def cosfin(x,digits):
 if abs(x) > 2:
    y=abs(x)
    turns=0 
    while y>=2: 
      y = y/2
      turns +=1
    cos1= cos(y, digits*2)
    cos2= (2*(cos1)**2) - 1
    for i in range (1, turns): 
      cos2= (2*(cos2)**2) - 1
      y *= 2
    return (cos2)
 else: 
   return(cos(x, digits))

while True:
  value = float(input("What x?: "))
  digits = float(input("How many correct decimal places?: "))
  start = time.time()
  approx = cosfin(value, digits)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")
