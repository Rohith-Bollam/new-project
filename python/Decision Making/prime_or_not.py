a=int(input('enter the value'))
b=(a**0.5)+1
c=int(b)
v=0
for i in range(2,c):
    if a%i==0:
         print("its a not prime")
         v=1
if v!=1:
     print("its a prime")



