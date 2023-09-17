#Sampson & Qing Yi

import time


def f(x):
  return

def g(x):
  return

def fgx(x):
  return g(x) - f(x)

def derivative(function, value):
  h = float((0.1)**12)
  num = function(value + h) - function(value)
  return float(num) / h

def zero(function, guess, N):
  n = 0
  xcurrent = guess
  while n < N:
    deriv = derivative(function, xcurrent)
    xnext = xcurrent - ((function(xcurrent) / deriv))
    n+=1
    xcurrent = xnext
  return xnext

def intersection(function, guess, N):
  return zero(function, guess, N)


while True:
  guess = float(input("Guess?: "))
  start = time.time()
  approx = intersection(fgx, guess, 1000000)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")
  
