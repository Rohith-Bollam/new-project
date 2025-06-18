import math
a=int(input())
b=int(input())
c=int(input())
e=(-b)/2*a
f=math.sqrt(b**2-4*a*c)/2*a

print(f"Roots:({e+f},{e-f})")