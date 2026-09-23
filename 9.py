a = int(input("Enter first no. ="))
b = int(input("Enter second no. ="))
print("Value of A =", a)
print("Value of B =", b)
'''
c=0
c=a
a=b
b=c
'''

a, b=b, a
print("Swapped value of A =", a)
print("Swapped value B =", b)
