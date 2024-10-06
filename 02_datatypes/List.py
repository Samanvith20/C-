names=["Ram","Shyam","Hari"]
print(names)

# to add an element
names.append("Sita")
print(names)

# pop() removes the last element
names.pop()
print(names)

# to insert an element
names.insert(1,"Gita")
print(names)

# to remove an element
names.remove("Hari")
print(names)

# to delete an element  
del names[0]
print(names)    

# to clear the list 
names.clear()
print(names)

# to get the length of the list
length=len(names)
print(length)

# to add elements in the list using slicing
names[0:2]=["Ram","Shyam"]
print(names)

# to add elements in the list using extend
names.extend(["Gita","Hari"])
print(names)

# using index add an element
names[0]="Sita"
print(names)