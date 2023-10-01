arr = []
key = int(input("Enter the key you want to search in the array:  "))
n = int(input("Enter the size of the array: "))

for i in range(n):
    a = int(input(f"Enter the {i}th element of the array:  "))
    arr.append(a)

arr.sort()
print(arr)
low = 0
high = n - 1

for i in range(n):
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"The index of the key element is {mid}")
        exit()
    elif arr[mid] > key:
        high = mid - 1
    elif arr[mid] < key:
        low = mid + 1

if key not in arr:
    print("\n\nKey is not present in the array")


# approach 2
# def binary_Search(nums,k,n):
#     if k not in arr:
#         return -1
#     return arr.index(k)

# a = binary_Search(arr,key,n)
# print(a)


