#Sampson

def e(x):
  a=1
  for i in range(1,100):
    a+= x**i / factorial(i)
  return a

def factorial(x):
  a=1
  for i in range(1,x+1):
    a*=i
  return a

while True:
  a = float(input("x?: "))
  approx = e(a)
  print("Answer:", approx)