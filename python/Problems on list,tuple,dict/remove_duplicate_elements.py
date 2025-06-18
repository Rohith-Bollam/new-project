a=[10,20,30,20,40,10,50]
b=[]
for i in a:
    if i in b:
        continue
    else:
        b.append(i)

print(b)

# OR

'''
    b=set(a)    converting list to set
    c=list(b)   converting set to list
    print(c)
'''