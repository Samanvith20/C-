
myname="Samanvith Reddy"
print(myname)

#  To access the string use the following syntax
first_char=myname[0]
second_char=myname[1]
last_char=myname[-1]
print(first_char)
print(second_char)
print(last_char)

# to get the length of the string
length=len(myname)
print(length)

#  to get the string in reverse
reverse=myname[::-1]
print(reverse)

# to check the string is empty or not
check_empty=myname=="" or myname==" "
print(check_empty)

# to  apply slice 

print(myname[0:5])
print(myname[0:5:2])
print(myname[0:5:3])
print(myname[0:5:4])
print(myname[2:])
print(myname[:5])

# convert from string to list
convertolist=myname.split(",")
print(convertolist)

# convert from list to string
convertostring=",".join(convertolist)
print(convertostring)

#  String formatting
name="Samanvith Reddy"
age=22
print("My name is {} and my age is {}".format(name,age))
 
 # to print in same line
chai = "He said \"masala chai is awesome to drink.\"" 
print(chai)

#  to print in different line
chai = "He said \"masala chai is awesome to drink.\"\nHe also said \"masala chai is good for health.\""
print(chai)

 # to check if a string is present in given string
chai="masala chai"
print("masalaa" in chai) # False
print("masala" in chai) # True

# to check if a string is not present in given string
chai="masala chai"
print("masalaa" not in chai) # True
print("masala" not in chai) # False