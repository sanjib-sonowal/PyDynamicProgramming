# List
print("***LIST***")
mylist = ["abc", "mno", "xyz", 10, 83.5, 10+3j]
print(mylist)
print(mylist[2])
print(mylist[0:3])
print(mylist[3:])

print("***REPEAT LIST***")
print(mylist * 3)

print("***COMBINE LIST***")
newlist = ["pqr", 7, 3.14]
print(mylist + newlist)

print("***UPDATE LIST ELEMENT***")
newlist[1] = "Seven"
print(newlist)

# Tuples
# Note: It cannot be updated rest same as List.
print("***TUPLE***")
mytuple=("abc", 10, 10-3j)
print(mytuple)
