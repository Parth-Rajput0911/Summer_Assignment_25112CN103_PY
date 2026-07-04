def reverse(num, rev):
    if num == 0:
        return rev
    return reverse(num // 10, rev * 10 + num % 10)

num = int(input("Enter number: "))
print("Reverse =", reverse(num, 0))