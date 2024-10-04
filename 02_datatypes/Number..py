import math
import random
#Integers
x=10
y=20
print(x+y)

#Float
x=10.5
y=20.5
print(x+y)

#Complex
x=10+20j
y=20+30j
print(x+y)

#Boolean
x=True
y=False
print(x or y)

# concatination
x="Samanvith"
y="Reddy"
print(x+y)

#Assignment(Numbers)
x=10
y=20
z=30
print(x,y,z)
sum=x+1
multipy=y*3
print(sum,multipy)
print(x<y and y<z)

#Comparision
number1=5.0
number2=8.0
print(number1==number2)
print(number1!=number2)
print(1==2<5)

#math
x=math.sqrt(4)
y=math.floor(4.9)
z=math.trunc(4.5)
print(x,y,z)
#random
mychoice=[44,12,89]
result=random.choice(mychoice)
print(result)
shuffle=random.shuffle(mychoice)
randomnumber=random.random()
randombetween=random.randint(1,10)
print(randomnumber)
print(shuffle)
print(randombetween)

#binary
x = int('1010', 2)  # Convert binary string to an integer
print(x)  

#decimal
a = int('34', 10)  # Convert decimal string to an integer
print(a)  

#hexadecimal
y = int('1A', 16)  # Convert hexadecimal (base 16) to decimal
print(y) 

#octal
z = int('17', 8)  # Convert octal (base 8) to decimal
print(z)  
 



