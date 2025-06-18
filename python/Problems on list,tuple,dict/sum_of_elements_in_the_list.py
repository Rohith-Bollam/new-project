a=[10,20,30,40,50]
sum=0
'''
for i in range(0,len(a)):
    sum=sum+a[i]
    if(len(a)-1==i):
        print("sum of elements :",sum)
    '''

# OR

for i in a:
    sum=sum+i
    
print("sum of elements :",sum)


