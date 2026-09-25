n = int(input("Enter N: "))
largest = 1  # Starting with the first number in the range 1 to N

for i in range(1, n + 1):
    if i > largest:
        largest = i

print(f"The largest number from 1 to {n} is:", largest)
