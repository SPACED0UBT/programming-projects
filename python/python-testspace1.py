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

print("%s %s %s. Your current balance is $%.2f." % (format_string, first, last, balance))

# https://www.learnpython.org/en/Basic_String_Operations

#Strings can be defined as anything between quotes
astring = "Hello world!"
astring2 = 'Hello world'

#You can use single quotes to assign a string. You may face problems if the value inside also has single quotes.
#Here is a work around using double quotes
print("single quotes are ' '")

#this is the total count of characters in astring
print (len(astring))

#this is the location of the first 'o' in astring. it only counts to the first match. 
#index starts with the zeroth index as the first position.
print (astring.index("o"))

#this counts the number of l's in the string
print(astring.count("l"))

#this prints the characters from index 3 to index 6 - for addition/subtraction reasons
print(astring[3:7])

#this prints the characters from index 3 -> end
print(astring[3:])

#this prints the characters from index 6 <- start
print(astring[:7])

#this prints the characters at index 3 : index N-1 from the end (-N)
print(astring[3:-3])

# extended slice syntax
# this prints from index 3 to index 6, skipping every other character
print(astring[3:7:2])
print(astring[1:14:2])

#this prints the characters of string from 3 to 7 skipping one character
print(astring[3:7])
print(astring[3:7:1])

#instead of strrev (from C) you can reverse a string like this
print(astring[::-1])

#this prints a string with all uppercase and another all lowercase
print(astring.upper())
print(astring.lower())

#this checks if the string starts with "Hello" or ends with "asdfasdfasdf"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdfasdf"))

#this splits the string into many substrings grouped in a list
spacesplit = astring.split(" ")
print(spacesplit)

#Basic string operators test

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings, each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# Conditions
# https://www.learnpython.org/en/Conditions

# Python uses boolean logic to evaluate conditions. Results should be true or false
x = 2
print(x == 2) # prints out True (== means is)
print(x == 3) # prints out False
print(x < 3) # prints out True (< less than)
# not equals is !=

# You can make more complex expressions with "and" and "or" operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# You can use the "in" operator to check if a variable exists in an "iterable object container"
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Python uses indents instead of brackets to define code blocks. Usually a tab is 4 spaces, although any consistent size will work.
statement = False
different_statement = True
if statement is True:
    # do something
    pass
elif different_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass