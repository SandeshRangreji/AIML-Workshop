# W/o Params and w/o return type
def add():
    a = 3
    b = 5
    ans = a + b
    print(ans)

add()

# with params and w/o return type
def add_(a, b):
    print(a+b)

add_(2,3)

# w/o params and with return type
def add():
    a = 5
    b = 9
    return a+b

ans = add()
print(ans)

# with params and with return type
def add(a, b):
    return a+b
ans = add(7,8)
print(ans)

# with default params
def add(a, b = 8):
    return a+b
ans = add(12)
print(ans)