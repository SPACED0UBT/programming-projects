#print text
print("Hello World!")

#print a variable
x = 1
if x == 1:
    # indented four spaces
    print ("x is 1.")
##############################
#print integers
myint=7
print(myint)

#print floating points (decimals)
myfloat=7.0
print(myfloat)
myfloat=float(7)
print(myfloat)

#print strings in quotes, double quotes allow easy use of apostrophes.
mystring='hello'
print(mystring)
mystring="hello"
print(mystring)
mystring=("Don't worry about apostrophes.")
print(mystring)

#you can use operators on numbers and strings
one=1
two=2
three=one+two
print(three)

#you can use operators on strings and integers
hello="hello"
world="world"
helloworld= hello+" "+world
print(helloworld)

a, b= 3, 4
print(a, b)

#this will not work! you can't mix numbers and strings while operating
one=1
two=2
hello="hello"
#print(one+two+hello)
#this will!
print(one+two,hello)

# change this code
mystring = hello
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
##########################################
#Lists can contain multiple entries and kinds of variables
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #prints 1, zero index
print(mylist[1]) #prints 2, first index
print(mylist[2]) #prints 3, second entry
#Querying entries that don't exist will cause errors
#print(mylist[3])

#print out 1,2,3
for x in mylist:
    print(x)

# exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append(hello)
strings.append(world)
second_name=(names[1])

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# operators can be used on numbers
number=1+2*3/4.0
print(number) #respects order of operation

# modulo is %, shows remainder of a division problem
remainder=11 % 3
print (remainder)

#if you use two "*" you do an exponential operation
squared=7**2
cubed=2**3
print(squared)
print(cubed)