#WAP TO CALCULATE SUM OF FIRST N NATURAL NO
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)