# Qing Yi

# enter numbers based on what is asked/given:
# 1 = original f(x)
# 2 = dy/dx only has x
# 3 = dy/dx has y and x in it

import time

# example function: f(x) = x^2
def fx (x): # original f(x)
  return x**2

def derivfx (x): # derivative only has x
  return 2 * x

# example derivative: dy/dx = y/x
def derivfxy (x, y): #  derivative has x and y 
  return x - y

def derivative(function, value): # derivative not known and not solvable
  h = 0.1**8
  num = function(value + h) - function(value)
  return num / h

def euler(function, initialx, endx, step):
  x = initialx
  ycurrent = fx(x)
  while x < endx:
    slope = derivative(function, x)
    ynext = ycurrent + (slope * step)
    x+=step
    ycurrent = ynext
  return ynext

def dxeuler(initialx, initialy, endx, step):
  x = initialx
  ycurrent = initialy
  while x < endx:
    slope = derivfx(x)
    ynext = ycurrent + (slope * step)
    x+=step
    ycurrent = ynext
  return ynext

def dxyeuler(initialx, initialy, endx, step):
  x = initialx
  ycurrent = initialy
  while x < endx:
    slope = derivfxy(x, ycurrent)
    ynext = ycurrent + (slope * step)
    x+=step
    ycurrent = ynext
  return ynext

while True:
  choice = int(input("Number?: "))
  if choice == 1:
    initialx= float(input("What start x?: "))
    endx = float(input("What end x?: "))
    step = float(input("Step size?: "))
    start = time.time()
    approx = euler(fx, initialx, endx, step)
    end = time.time()
    print("Answer:", approx)
    print("Time took:", end - start, "seconds")
  if choice == 2:
    initialx = float(input("What start x?: "))
    initialy = float(input("What start y?: "))
    endx = float(input("What end x?: "))
    step = float(input("Step size?: "))
    start = time.time()
    approx = dxeuler(initialx, initialy, endx, step)
    end = time.time()
    print("Answer:", approx)
    print("Time took:", end - start, "seconds") 
  if choice == 3:
    initialx = float(input("What start x?: "))
    initialy = float(input("What start y?: "))
    endx = float(input("What end x?: "))
    step = float(input("Step size?: "))
    start = time.time()
    approx = dxyeuler(initialx, initialy, endx, step)
    end = time.time()
    print("Answer:", approx)
    print("Time took:", end - start, "seconds")