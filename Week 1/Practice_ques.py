# Sum of n numbers
print("SUM OF n NUMBERS")
n = 500
i = 1
c = 0
sum_ = 0
while c != n:
    sum_ = sum_ + i
    i = i + 1
    c = c + 1
print(sum_)

# Sum of n even numbers
print("SUM OF n EVEN NUMBERS")
n = 50
c = 0
i = 2
sum_ = 0
while c != n:
    sum_ = sum_ + i
    i = i + 2
    c = c + 1
print(sum_)

# Sum of n odd numbers
print("SUM OF n ODD NUMBERS")
n = 50
c = 0
i = 1
sum_ = 0
while c != n:
    sum_ = sum_ + i
    i = i + 2
    c = c + 1
print(sum_)

# Reverse of a number
print("Reverse of a number")
n = 4562
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)

# check if a number is palindrome or not
print("Check if a number is palindrome or not")
n = 1221
temp = n
rev = 0
while n > 0:
    a = n % 10
    rev = rev*10 + a
    n = n // 10

if rev == temp:
    print("Yes")
else:
    print("No")

