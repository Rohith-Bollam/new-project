num1=int(input("enter num1 value"))
num2=int(input("enter num2 value"))
operator=input("enter operator value")
if operator=='+':
    value=num1+num2
    print(value)
elif operator=='-':
    value=num1-num2
    print(value)
elif operator=='*':
    value=num1*num2
    print(value)
elif operator=='/':
    value=num1/num2
    print(value)
else:
    print('the operator is invalid')



