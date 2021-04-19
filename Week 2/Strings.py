# Concatenation of Strings
a = 'ABC'
b = 'def'
concat_s = a + b
print(concat_s)
print()

#Slicing on strings
s = 'Abcdef dsce ! @ #'
print(s[:]) # complete string
print(s[:4]) # 0 to index 3, 4 is exclusive
print(s[4:]) # index 4 to last index
print(s[::3]) # from 0 index to last index at a gap of 3
print(s[::-1]) # Reverse of a string
print(s[::-3]) # from last to 0 inddex at gap of 3
print()

#Operations on strings
s = 'Hello ! World ! Hey ! Universe'

c = s.count('l')
print(c)

li = s.split()
print(li)

li = s.split('!')
print(li)

s1 = s.lower()
print(s1)

s2 = s.upper()
print(s2)

ind = s.index('!')
print(ind)

s1 = s.replace('!', '@')
print(s1)

s1 = s.replace('!', '#', 2)
print(s1)

s = 'abcdef'
a = s.islower()
print(a)

s = 'ABCDEF'
a = s.isupper()
print(a)

s = '1234'
a = s.isdigit()
print(a)

s = 'aBcDefr'
a = s.isalpha()
print(a)

s = 'abcDEFqwS12'
a = s.isalnum()
print(a)

print()

# Questions
# Remove vowels from a string
print("Remove vowels from string")
s = 'qwajnbe'
s1 = ''
for i in range(len(s)):
    if s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u':
        s1 = s1 + s[i]
print(s1)
print()

# Remove Consecutive Duplicates
print("Remove consecutive duplicates")
s = 'aaaabbbbcddde'
s1 = ''
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        s1 = s1 + s[i]
s1 = s1 + s[-1]
print(s1)
print()

# Count of highest Occuring character
print("Count of highest occuring character")
s1 = 'aaabbbaaaacdebdde'
li = []
s = set(s1)
for ele in s1:
    c = s1.count(ele)
    li.append(c)
print(max(li))
print()

# Merge String Alternately
print("Merge strings alternately")
word1 = 'abcd'
word2 = 'fgh'
s = ''
if len(word1) > len(word2):
    for i in range(len(word2)):
        s = s + word1[i] + word2[i]
    s = s + word1[len(word2):]
    print(s)

elif len(word1) < len(word2):
    for i in range(len(word1)):
        s = s + word1[i] + word2[i]
    s = s + word2[len(word1):]
    print(s)

else:
    for i in range(len(word1)):
        s = s + word1[i] + word2[i]
    print(s)
