#Susan 
import time
def ln(x, digits):
  n = 1
  while n > 0:
    if (x - 1)**n / n < (1 * 10**(-(digits+1))):
      n = n
      break
    else:
      n = n + 1
  value = 0
  for i in range(1, n):
    value += ((-1)**(i - 1)) * (x - 1)**i / i
  return (value)

def lnn(x, digits): 
  p=0
  if x >= 1.5:
    while x>=1.5: 
      x = x/1.5 
      p = p + 1 
    final= (ln(1.5,digits*2) * p) + ln(x,digits)
  else:
    final= ln(x,digits)
  return(final)

def lnfin(x,digits): 
  if x < 1: 
    solution= -lnn((x**(-1)), digits)
  else:
    solution= lnn(x,digits)
  return(solution)

def log(a,b,digits): 
  solution= lnfin(b,digits)/lnfin(a,digits)
  return(solution)

while True:
  a = float(input("base?: "))
  b = float(input("x?: "))
  digits = float(input("digits?:"))
  start = time.time()
  approx = log(a,b,digits)
  end = time.time()
  print("Answer:", approx)
  print("Time took:", end - start, "seconds")
  