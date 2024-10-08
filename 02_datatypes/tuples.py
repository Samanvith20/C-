# create atuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# access a tuple
print(my_tuple[0])

# change a tuple
# my_tuple[0] = "orange"
# print(my_tuple)
# we cannot change because tuples are immutable

# nested tuple  
my_tuple = ("apple", [1, 2, 3], True)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# add a tuple
my_tuple = my_tuple + ("orange",)
print(my_tuple)




# The main difference between tuples and lists is that tuples are immutable, whereas lists are mutable. This means that you can't change the elements of a tuple once it's been created, unlike a list which can be modified freely.
