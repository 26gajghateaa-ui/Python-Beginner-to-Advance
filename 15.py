a = int(input("Enter first no. = "))
b = int(input("Enter Second no. = "))
c = int(input("Enter Third no. = "))

if a >= b and a >= c:
    print(f"{a} is the greatest number")
elif b >= a and b >= c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")        
