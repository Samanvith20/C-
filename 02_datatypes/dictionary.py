#create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)

# accesss a value
print(my_dict["name"])

# change a value
my_dict["age"] = 31
print(my_dict)

# add a key-value pair
my_dict["country"] = "USA"
print(my_dict)

# remove a key-value pair
del my_dict["country"]
print(my_dict)

#nested dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
print(my_dict)

# access a nested dictionary
print(my_dict["address"]["city"])

# update a nested dictionary
my_dict["address"]["city"] = "New York City"
print(my_dict)

#length of a dictionary
print(len(my_dict))

#create an empty dictionary
empty_dict = {}
print(empty_dict)

#check if a key exists
print("name" in my_dict)
print("country" in my_dict)

# run a for loop in my dictioanry
for key, value in my_dict.items():
    print(key, value)
    # we use .items() to get the key-value pairs
    
    #squarednum
    squarednum = {x:x**2 for x in range(10)}
    print(squarednum)

# how to create a dict using key and values as sepeartely
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict.fromkeys(keys, values)
my_dict= dict(zip(keys, values))
# difference b/w using zip and fromkeys is 
# zip(), on the other hand, is used to combine two or more iterables (like lists or tuples) into pairs of tuples, which can then be used to construct a dictionary with distinct key-value pairs.
# fromkeys generates a new dictionary from the specified sequence of elements as keys and a user-supplied value
print(my_dict)