# (1) Python Program to check if a Number Is Positive Or Negative

# Method 1: brute force
num = 15
if num > 0:
    print("+")
elif num < 0:
    print("-")
else:
    print("0")

# Method 2: Nested if else
numb = 15
if numb >=0:
    if numb == 0:
        print("0")
    else:
        print("+")
else:
    print("-")

# Method 3: Ternary operator
a = 15
print("positive" if a>0 else "negative")


# (2) Python Program to Check Whether a Number is Even or Odd

# Method 1: Brute force
b = int(input("Enter a num: "))
if b % 2 == 0:
    print('even')
else:
    print('odd')

# Method 2: Ternary Operator
c = 15
print("even") if c % 2 == 0 else print("odd")

# Method 3: Bitwise Operator
# If we have any number num doing bitwise ‘&‘ operation will give resultant as
# 1: If n is odd
# 0: if n is even

def isEven(num):
    return not num&1
num = 13
if isEven(num):
    print('even')
else:
    print('odd')


# (3) Python Program to Find the Sum of First N Natural Numbers

# Method 1: For loop
num = 5
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)

# Method 2: Using Formula for the Sum of Nth Term
# Formula -->  Sum = ( Num * ( Num + 1 ) ) / 2
num = 5
print(int(num*(num+1)/2))

# Method 3: Recursion
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))

# (4) Python Program to Find the Sum of N Natural Numbers

# It's same as First sum of First N natural numbers.

