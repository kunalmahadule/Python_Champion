size = int(input("Enter the size of the array: "))
print()
arr = []
for i in range(0, size):
    i = int(input(f"Enter {i}th element: "))
    arr.append(i)
print()
print(arr)
max = 0
min = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print()
print("Maximum element = ", max)
print("Minimum element = ", min)
