a={"a":1,"b":2}
print(a["a"])

# get method
print("get value : ",a.get("a"))

# items method
print("items in the dictionary :",a.items())

# values method (it only gives the values in dictionary)
print("values in the dictionary :",a.values())

# keys method (it only gives the keys in dictionary)
print("keys in the dictionary :",a.keys())

#pop method
# the popped value return in the terminal
print("pop value : ",a.pop("b"))
print("after pop method",a)
