a=[15,2,7,25,10]
maxi=a[0]
mini=a[0]

for i in range(1,len(a)):
    if maxi<a[i]:
        maxi=a[i]
    if mini>a[i]:
        mini=a[i]
print("maximum",maxi)
print("minimum",mini)



    