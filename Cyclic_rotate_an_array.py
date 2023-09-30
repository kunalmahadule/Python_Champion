'''Given an array, rotate the array by one position in clock-wise direction.
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4'''
# def rotate(arr, n):
#     arr.insert(0, arr[n - 1])
#     # n = len(arr)
#     arr.pop(arr[n - 1])
#     return arr


def rotate( arr, n):
    x=arr.pop()
    arr.insert(0,x)
    return arr

arr = [2, 1]
n = len(arr)
print(rotate(arr, n))

