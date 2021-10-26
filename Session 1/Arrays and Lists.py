# Intro to lists
li = [1,2,3,4]
li1 = ['1', '2', '3', '4']
li2 = [1, 2, 'a', 'b', '3', 'c', 5]
li3 = [1,2,3,[3,4,5],li1]

print(li)
print(li1)
print(li2)
print(li3)

# Operations on lists
li = []
li.append(2)
li.append(3)
li.extend([4,5,6,7,8,9,10,9])
li.pop(3) # 3 is index
li.remove(4) # 4 is element in a list
print(li)

print()
c = li.count(9) # 9 is an element in list
print("Count =", c)

ind = li.index(3) # 3 is an element in list
print("Index =", ind)

# nums = li
# nums[2] = 10
# print(nums)
# print(li)

nums = li.copy()
nums[2] = 10
print("nums =", nums)
print("li =", li)

li.sort()
print("Sorted li =", li)

print()
print("Sum of all the elements in list =", sum(li))
print("Minimum element in list =", min(li))
print("Maximum element in list =", max(li))

print()
# Looping on Lists
li = [2,1,3,2,4,5,6,8,10]

# Print sum of even numbers and sum of odd numbers in a list
sum_even = 0
sum_odd = 0
for i in range(len(li)):
    if li[i] % 2 == 0:
        sum_even = sum_even + li[i]
    else:
        sum_odd = sum_odd + li[i]

print("Sum of even numbers =", sum_even)
print("Sum of odd numbers =", sum_odd)

odd_sum = sum(li) - sum_even
print("Sum of odd numbers =", odd_sum)

# Alternantive way of for loop
li = [2,1,3,2,4,5,6,8,10]
es = 0
for ele in li:
    if ele % 2 == 0:
        es = es + ele
print("Sum of even numbers =", es)
print()

# Slicing in lists
li = [12,11,13,12,14,15,16,18,10]
print(li[:]) # from 0 to last index
print(li[2:]) # from index 2 to last index
print(li[:5]) # from 0 to index 4, index 5 is exclusive
print(li[2:6]) # from index 2 to index 5, 6 is exclusive
print(li[::2]) # from index 0 to last index at a gap of 2
print(li[::-1]) # Reverse of a list
print(li[::-2]) # from last index to 0 index at a gap of 2

print()

# Space separated input
li = [int(x) for x in input().split()]
print(li)

li1 = [x for x in input().split()]
print(li1)

# Line seprated input
n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
print(li)



