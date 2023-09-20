# take an array from user and also take one int value from user as targeted value
# and then print the index position of such 2 values from arrays answer of addition
# is equal to the targeted value

Size = int(input("Enter the size of the array: "))
arr = []

i = 0
while i < Size:
    temp = int(input(f"Enter the {i}th position of the array: "))
    arr.append(temp)
    i += 1

print(arr)

print()
target = int(input("Enter the target position: "))
print()

for x in arr:
    for y in arr:
        if x+y==target:
            print(f"position: [{arr.index(x)},{arr.index(y)}]")
            print(f"because {x} + {y} = {target}")
            exit()

