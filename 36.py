n = int(input("Enter N: "))
smallest = 1  # In range 1 to N, 1 is the smallest

for i in range(1, n + 1):
    if i < smallest:
        smallest = i

print(f"The smallest number from 1 to {n} is:", smallest)
