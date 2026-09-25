n = int(input("Enter N: "))
total_sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total_sum += i

print(f"Sum of odd numbers from 1 to {n}:", total_sum)
