m = float(input("Enter your marks (0 to 100): "))


if 90 <= m <= 100:
    print("Grade: A+")
elif 80 <= m < 90:
    print("Grade: A")
elif 70 <= m < 80:
    print("Grade: B")
elif 60 <= m < 70:
    print("Grade: C")
elif 50 <= m < 60:
    print("Grade: D")
elif 0 <= m < 50:
    print("Grade: Fail")
else:
    print("Invalid input")
