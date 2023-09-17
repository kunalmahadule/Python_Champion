n = 4

for i in range(1, n + 1):
    print("*" * i, end="")
    print(" " * ((n - i) * 2), end="")
    print("*" * i)
x = n
for j in range(1, n + 1):
    print("*" * x, end="")
    print(" " * ((n - x) * 2), end="")
    print("*" * x)
    x -= 1

