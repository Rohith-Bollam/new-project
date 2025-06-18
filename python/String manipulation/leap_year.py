year=int(input('enter the year'))
if year%100==0 and year%400!=0:
    print("its not a leap year")
elif year%4==0:
    print("its a leap year")
else:
    print("its a leap year")