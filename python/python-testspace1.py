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

#you can use operators with strings
helloworld = "hello" + " " + "world"
print (helloworld)

#you can multiply word strings 
lotsofhellos = "hello "*10
print(lotsofhellos)

#you can join lists with operators
even_numbers = [0,2,4,6,8]
odd_numbers=[1,3,5,7,9]
all_numbers=odd_numbers+even_numbers
print(all_numbers)

#you can multiply lists
print([1,2,3]*3)

#exercise to create 10 x and 10 y variables
#also make a big list by mixing the x and y lists

x=object()
y=object()

x_list=[x]*10
y_list=[y]*10
big_list=x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# https://www.learnpython.org/en/String_Formatting

#python uses C-style string formatting to create strings
#the "%" operator can format variable sets in a "tuple" (fixed size list)
#together with a format string to contain normal text with "argment specifiers"
#i.e %s and %d

#this prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#you can use multiple argument specifiers using a tuple
#this prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old" % (name, age))

#a non-string object can be formatted using the %s operator as well.
#it will return with the "repr" method
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

## Here are some basic argument specifiers to know

## %s - String (or any object with a string representation, like numbers)

## %d - Integers

## %f - Floating point numbers

## %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

## %x/%X - Integers in hex representation (lowercase/uppercase)

#This should print "Hello John Doe. Your current balance is $53.44
data = ("John", "Doe", 53.44)
format_string = "Hello"
first=data[0]
last=data[1]
balance=data[2]

print("%s, %s %s. Your current balance is $%.2f." % (format_string, first, last, balance))

#Strings can be defined as anything between quotes
astring = "Hello world!"

astring2 = 'Hello world'

#You can use single quotes to assign a string. You may face problems if the value inside also has single quotes.
#Here is a work around using double quotes
print("single quotes are ' '")

#this is the total count of characters in astring
print (len(astring))

#this is the location of the first 'o' in astring. index starts with the zeroth index as the first position.
print (astring.index("o"))

#this counts the number of l's in the string
print(astring.count("1"))

l1