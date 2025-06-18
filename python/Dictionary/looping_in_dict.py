a={"a":1,"b":2,"c":3}
print(a)

# if you use "a" as a range it only gives the key value as output
  #  we should use methods items,values to return values from the dictionary
# keys
for key in a:
    print(key)

# values
for value in a.values():
    print(value)

# if you want to print both use items method

for i,j in a.items():
    print("key",i,"value",j)

# dictionary comrprehension
# same as in list,set,tuple but we should add key in the expression as shown below "x:"
b={x:x**2 for x in range(1,6)}
print(b)