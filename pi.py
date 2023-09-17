#Using trig identity: 4arctan(1/5) - arctan(1/239)=pi/4
#Calista

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

def pi():
  return((4*(4*arctan(1/5) - arctan(1/239))))

print(pi())
