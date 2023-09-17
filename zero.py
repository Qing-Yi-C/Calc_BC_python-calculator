# Newton's method
# Qing Yi

import time

def fx (x): # example: what is the 127th root of 21694201234567890?
  return (x**127) - 21694201234567890

def derivative(function, value):
  h = float((0.1)**12)
  num = function(value + h) - function(value)
  return float(num) / h

def zero(function, guess, N):
  n = 0
  xcurrent = guess
  while n < N:
    deriv = derivative(function, xcurrent)
    xnext = xcurrent - ((function(xcurrent)) / deriv)
    n+=1
    xcurrent = xnext
  return xnext

while True:
  guess = float(input("Guess?: "))
  value = float(input("Number of iterations?: "))
  start = time.time()
  approx = zero(fx, guess, value)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")