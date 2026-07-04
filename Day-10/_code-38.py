rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))