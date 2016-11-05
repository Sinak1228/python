def sum(a,b):
    return a+b
    # 수행문

def sub(a,b):
    return a-b
    #수행문

def mul(a,b):
    return a*b
    #수행문

def div(a,b):
    return a/b
    #수행문

def sumAtoB(a,b):
    for i in range(a, b+1):
        sum = sum + 1
    return sum
    #수행문

print(sum(15, 10))
print(sub(15, 10))
print(mul(15, 10))
print(div(100, 10))
print(sum(1, 10))
