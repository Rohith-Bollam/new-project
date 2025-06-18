# set union
s1={1,2,3}
s2={3,4,5}
print("union",s1.union(s2))

# set intersection
print("intersection",s1.intersection(s2))

# set difference
print("difference of s1",s1.difference(s2))
print("difference of s2",s2.difference(s1))

# set symmetric difference 
# ->it returns the value which intersection can't
print("symmetric difference ",s1.symmetric_difference(s2))

# check an element in the set
print(2 in s1)
print(6 in s2)

# length in set
print("length of  s1",len(s1))

# frozen sets this are immutable (cant be changed)
a=frozenset(s1)

# set comrprehension
b={x**2 for x in range(1,6)}
print(b)