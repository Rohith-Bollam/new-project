"""
a=[1,2,3,2,1,4,2,5]
b=a.count(2)
print("count of 2 =",b)"
"""
# OR
a=[1,2,3,2,1,4,2,5]
b=2
count=0
for i in a:
    if b==i:
        count+=1

print("count of 2 =",count)

# OR

# using comphrension
l=[int(x) for x in input().split(",")]
n=int(input("enter counting number"))
count=0
for i in a:
    if b==i:
        count+=1

print("count of 2 =",count)