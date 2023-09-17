# tan = sin/cos (use power series for both sin and cos to find tan)
# Qing Yi

import time

def factorial(x):
  a=1
  for i in range(1,x+1):
    a*=i
  return a

def absolute(number):
  if number < 0:
    return number * -1
  else:
    return number

def f(x): 
  return float(1) / (1 + (x**2))
  
def integrate(a,b): 
  n=1000000
  h = (b-a)/n
  sum= 0
  for i in range (1,n+1): 
    sum+= (f(a+ i*h) + f(a+ (i-1)*h))/2
  return sum * h

def arctan(x):
  if (x > 1):
    x = (x) / (1 + (1 + x**2)**0.5)
    return 2 * arctan(x)
  else:
    return integrate(0,x)

def cos(x, digits):
  next = 1
  old = 0
  n = 0
  error = (0.1)**(digits + 1)
  while absolute(next - old) >= error:
    add = ((-1)**n) * ((x**(2*n))/(factorial(2*n)))
    old = next
    next += add
    n+=1
  return next - 1

def cosfin(x,digits):
  y=x
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

def sinfin(x,digits): 
  final=(1-cosfin(2*x, digits*2))/2
  
  return(final**0.5)

def pi():
  return((4*(4*arctan(1/5) - arctan(1/239))))

def check_sign(x):
  pie = pi()
  if (x % (2 * pie) <= pie):
    return True
  elif(x % (2 * pie) > pie):
    return False

def sinfin2(x, digits):
  positive = check_sign(x)
  sin = sinfin(x, digits)
  if (positive == False and sin > 0):
    return -1 * sin 
  else:
    return sin

def tan(x, digits):
  return sinfin2(x, digits) / cosfin(x, digits)

while True:
  value = float(input("What x?: "))
  digits = float(input("How many correct decimal places?: "))
  start = time.time()
  approx = tan(value, digits)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")