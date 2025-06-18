'''
def fun(a):
    a=a+10
    return a
a=5
a=fun(a)
print(a)
'''


def div(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

n=int(input())
div(n)