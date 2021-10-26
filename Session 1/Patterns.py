# Basic Patterns
print("BASIC PATTERN")
n = 5
for i in range(0,n):
    for j in range(0, i+1):
        print('*', end = ' ')
    print()
print()

n = 5
for i in range(0,n):
    for j in range(n-i):
        print("*" , end=" ")
    print()
print()

# Square Patterns
print("SQUARE PATTERN")
rows = cols = 5
for i in range(rows):
    for j in range(cols):
        print("*" , end=" ")
    print()
print()

# Rectangular Pattern
print('RECTANGULAR PATTERN')
rows = 5
cols = 4
for i in range(rows):
    for j in range(cols):
        print("*" , end=" ")
    print()
print()

# Triangular Pattern
print('TRIANGULAR PATTERN UPWARD')
n = 5
for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ")
print()

print('TRIANGULAR PATTERN UPWARD WAY 2')
n = 5
for i in range(0,n):
    print(" "*(n-i-1) + "* "*(i+1))
print()

print('TRIANGULAR PATTERN DOWNWARD WAY 1')
n = 5
for i in range(0, n):
    for j in range(0, i):
        print(end = ' ')
    for j in range(0, n-i):
        print("*", end=" ")
    print(" ")

print('TRIANGULAR PATTERN DOWNWARD WAY 2')
n = 5
for i in range(0,n):
    print(" "*i + "* "*(n-i))
print()

# Character Pattern
print("CHARACTER PATTERN")
n = 5
x = 0
for i in range(0,n):
    for j in range(0, i+1):
        print(chr(65+x) , end=" ")
        x = x + 1
    print()
print()

n = 5
x = 0
for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=" ")
    for j in range(0, i + 1):
        print(chr(65+x), end=" ")
        x = x + 1
    print(" ")
print()

# Reversed Pattern
print('REVERSED PATTERN')
n = 5
for i in range(0,n):
    print(" "*i + "*"*(n-i))
print()

# Question Set
# Prime number
# Palindrome number
# Sum of n numbers
# sum of n even numbers
# sum of n odd numbers
# reverse of a number
