# 1
# Python is widely used for web development, data analysis, artificial intelligence, scientific computing, automation, machine learning etc.

# 2
# Programming is the process of writing instructions (called code) that a computer can understand and execute to perform specific tasks or solve problems.

# 3
# Python is a high-level, interpreted, object-oriented programming language which is easy to learn and  use.

# 4
a=int(input("enter a number to check positive or negative or zero:"))
if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
else:
    print("the number is zero")

# 5
b=int(input("enter number for factorial:"))
factorial=1
for i in range(1,b+1):
    factorial=factorial*i
print("the factorial of",b,"is",factorial)

# 6
n = int(input("Enter number:"))
a = 0
b = 1
for i in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c

# 7
# Memory management in Python is handled by the Python memory manager, which allocates and deallocates memory for objects as needed. 
# It uses reference counting and garbage collection to manage memory efficiently.

# 8
# The continue statement skips the current iteration of a loop and moves to the next iteration.

# 9
c=int(input("enter a number to swap:"))
d=int(input("enter another number to swap:"))
# with temp
temp=c
c=d
d=temp
print("after swapping c is",c,"and d is",d)
# without temp
c,d=d,c
print("after swapping c is",c,"and d is",d)

# 10
d=int(input("enter a number to check even or odd:"))
if d%2==0:
    print("the number is even")
else:
    print("the number is odd")

# 11
ch=input("enter a character to check vowel or consonant:")
if ch in 'aeiouAEIOU':
    print("It is vowel")
else:
    print("It is consonant")

# 12
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b or b == c or a == c:
    print("Sum = 0")
else:
    print("Sum =", a + b + c)

# 13
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
if(a+b==0 or a-b==0 or a==b):
    print("TRUE")
else:
    print("FALSE")

# 14
a=int(input("enter a number for sum:"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print("the sum is",sum)

# 15
text = input("Enter a string: ")
length = len(text)
print("Length of string is:", length)

# 16 NOT CLEAR WITH LOGIC

# 17
# Negative indexes are used in Python to access elements from the end of a sequence (like strings, lists, or tuples).

# 18
string = input("Enter main string: ")
substring = input("Enter substring: ")
count = string.count(substring)
print("Occurrences:", count)

# 19
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# 20
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
new_str1=str1[:2] + str2[2:]
new_str2=str2[:2] + str1[2:]
print("New first string:", new_str1)
print("New second string:", new_str2)

# 21
string = input("Enter a string: ")
if (len(string) < 3):
    print(string)
elif(string.endswith("ing")):
    print(string + "ly")
else:
    print(string + "ing")

# 22
def rev_str(s):
    if len(s)%4==0:
        return s[::-1]
    else:
        return s
string = input("Enter a string: ")
result = rev_str(string)
print("Result:", result)

# 23
string1 = input("Enter first string: ")
if len(string1) > 2:
    print("empty string")
else:
    new_string=string1[:2]+string1[-2:]
    print("New string:", new_string)

# 24
def insert_middle(str1, str2):
    mid = len(str1) // 2
    return str1[:mid] + str2 + str1[mid:]

s1 = input("Enter first string: ")
s2 = input("Enter string to insert: ")

result = insert_middle(s1, s2)
print("Result:", result)

# 25
# A List in Python is a collection of ordered and mutable elements.
# Lists allow duplicate values and are written using square brackets [ ].

# 26
list1 = [10, 20, 30, 40]
list1.pop()
print(list1)

# 27
list2= [2, 33, 222, 14, 25]
print(list2[-1])

# 28
# Append() method is used to add an element at the end of a list.
# Extend() method is used to add all elements of an iterable (like another list) to the end of the list.

# 29
def list_operations(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)

    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Sum:", total)

nums = [10, 20, 5, 40, 15]

list_operations(nums)

# 30
# Two lists can be compared using the == operator. If the lists have the same elements in the same order, they are considered equal.

# 31
def count_strings(strings):
    count = 0
    for s in strings:
        if len(s) > 2 and s[0] == s[-1]:
            count += 1
    return count
string_list = ['abc', 'xyz', 'aba', '1221']
result = count_strings(string_list)
print("Count:", result)

# 32
list1 = [1, 2, 3, 2, 4, 1, 5]
unique_list = list(set(list1))
print(unique_list)

# 33
list1 = []
if not list1:
    print("List is empty")
else:
    print("List is not empty")

# 34
def common_member(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

print(common_member([1,2,3], [3,4,5]))

# 35
squares = [x**2 for x in range(1,31)]

print("First 5:", squares[:5])
print("Last 5:", squares[-5:])

# 36
def unique_elements(list1):
    unique_list=[]
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
list1 = [1, 2, 3, 2, 4, 1, 5]
result = unique_elements(list1)
print(result)

# 37
char_list = ['H','e','l','l','o']
string = ''.join(char_list)
print(string)

# 38
import random
list1 = [10, 20, 30, 40, 50]
print(random.choice(list1))

# 39
list1 = [10, 5, 8, 3, 7]
list1.sort()
print("Second smallest:", list1[1])

# 40
list1 = [1,2,2,3,4,4,5]
unique = list(set(list1))
print(unique)

# 41
list1 = [1,2,3,4,5]
sublist = [3,4]

if all(item in list1 for item in sublist):
    print("Sublist exists")
else:
    print("Sublist not found")

# 42
list1 = [10, 20, 30]
a, b, c = list1
print(a)
print(b)
print(c)

# 43
# A tuple is a collection of elements in Python that is ordered and immutable .
# tuple is different from list because it cannot be modified after creation and is defined using parentheses ( ).

# 44
tuple1 = (10, "Hello", 3.14, True)
print(tuple1)

# 45
list1 = [(1,2), (3,4), (5,6)]
list2, list3 = zip(*list1)
print(list(list2))
print(list(list3))

# 46
list1 = [('a',1), ('b',2), ('c',3)]
dict1 = dict(list1)
print(dict1)

# 47
t = (('a', 1), ('b', 2), ('c', 3))
d = dict(t)
print(d)

# 48 WAS ABSENT IN DICTIONARY TOPIC 

# 49
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {**d1, **d2}
print(d3)

# 50
d = {'a': 10, 'b': 20, 'c': 30}
key = input("Enter key to check: ")
if key in d:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")

# 51
d = {'a':1,'b':2,'c':3}

for key, value in d.items():
    print(key, value)

# 52
# The in operator checks if the specified key is present in the dictionary.
#  If the key exists, it returns True; otherwise, it returns False.

# 53
d = {}
for i in range(1, 16):
    d[i] = i
print(d)

# 54
d = {'a':1,'b':2,'c':3}
keys = ['a','b']
if all(k in d for k in keys):
    print("All keys exist")
else:
    print("Keys missing")

# 55
d1 = {'a':10,'b':20}
d2 = {'c':30,'d':40}
d1.update(d2)
print(d1)

# 56
keys = ['a','b','c','d']
values = [400,400,300,400]
d = dict(zip(keys, values))
print(d)

# 57
d = {'a': 500, 'b': 200, 'c': 700, 'd': 100, 'e': 900}
values = sorted(d.values())
top3 = values[-3:]
print("Highest 3 values:", top3)

# 58 DON'T KNOW HOW TO DO THIS

# 59, 60
s="w3resource"
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
print(d)

# 61
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = 5
print("Factorial:", factorial(num))

# 62
def check_range(n):
    if n in range(1,10):
        print("Number is in range")
    else:
        print("Number is not in range")

check_range(5)

# 63
def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i

    if sum == n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

perfect_number(6)

# 64
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("madam")

# 65
# There are two main types of functions:
# Built-in Functions
# Predefined functions provided by Python.
# Example: print(), len(), type()
# User-defined Functions
# Functions created by the programmer using def.

# 66
import random
list1 = [10,20,30,40]
print(random.choice(list1))

# 67
import random
print(random.choice(range(1,10)))

# 68
import random
print(random.randint(1,100))

# 69
# In Python, the starting value for generating random numbers is set using the seed() function from the random module.
# The seed() function initializes the random number generator so that it produces the same sequence of random numbers every time the program runs with the same seed value.

# 70
# the items of a list can be randomized in place using the shuffle() function from the random module.

# 71
# A file function in Python is used to create, read, write, and modify files.
# w – Write (create or overwrite file)
# r – Read a file

# 72
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

# 73
file=open("sample.txt","a")
file.write("This is an additional line.\n")
file.close()

file=open("sample.txt","r")
content=file.read()
print(content)

# 74
file=open("sample.txt","r")
n=1
for i in range(n):
    line=file.readline()
    print(line)
file.close()

# 75
file=open("sample.txt","r")
lines=file.readlines()
n=2
for line in lines[-n:]:
    print(line)
file.close()

# 76
file=open("sample.txt","r")
lines=file.readlines()
print(lines)
file.close()

# 77
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# 78
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word is:", longest)

# 79
file = open("sample.txt", "r")
count = 0
for line in file:
    count += 1
print("Number of lines:", count)
file.close()

# 80 DON'T KNOW HOW TO DO THIS

# 81
data = ["Apple", "Banana", "Mango"]

file = open("output.txt", "w")
for item in data:
    file.write(item + "\n")
file.close()

# 82
file1 = open("source.txt", "r")
file2 = open("destination.txt", "w")

content = file1.read()
file2.write(content)

file1.close()
file2.close()

# 83
# An error is a problem in a program that prevents it from running correctly.
# Exception handling allows a program to handle runtime errors without crashing.

# 84
#  Try block can have multiple except blocks to handle different types of exceptions. The except block that matches the type of exception raised will be executed.
# Built in exceptions are: division by zero, index out of range, file not found, value error, etc.

# 85
# The else block executes when no exception occurs in the try block.

# 86
# one block of except can handle multiple exceptions.

# 87
# The finally block always executes, whether an exception occurs or not.

# 88
# Output will be false because '1' and 1 are of different types.
# Python does not automatically convert types for comparison.

# 89
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program finished")


# 90
num = int(input("Enter an odd number: "))
try:
    if num % 2 == 0:
        raise Exception("Even number entered")
    else:
        print("You entered an odd number:", num)
except Exception as e:
    print("Error: you cannot enter an even number", e)
