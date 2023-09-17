#Susan 


def f(x): 
  return x**2

def integrate(a,b): 
  n=1000
  h = (b-a)/n
  sum= 0
  for i in range (1,n+1): 
    sum+= (f(a+ i*h) + f(a+ (i-1)*h))/2
  return(sum * h)

print(integrate(3,2))

