l=[1,2,3,4]
# adds at last
l.append(5)
#(2, )first index value to insert
#( ,9) value to be inserted
#[1,2,9,3,4,5]
l.insert(2,9)
# remove from the list
# we should give the value to be removed
l.remove(9)
# it pop from the last element default
# we can give also the index value to remove
l.pop()
l.pop(0)
# gives the index value by our given value
a=l.index(4)
print("index value is:",a)
# count the given value how many are there
m=[1,1,1,2,3,1,4,5]
print("count is :",m.count(1))
# sort the value gien in the list
b=[32,43,1,2,12,21]
b.sort()
print("sorted is:",b)
#reverse the list
b.reverse()
print("reversed list is:", b)

print(l)