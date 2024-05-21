'''
N = 7
Arr[] = {1, 2, 3, 4, 5, 6, 7}
D = 2
Output: 3 4 5 6 7 1 2
Explanation:
Rotate by 1: [2, 3, 4, 5, 6, 7, 1]
Rotate by 2: [3, 4, 5, 6, 7, 1, 2]
'''

# arr = [1, 2, 3, 4, 5, 6, 7]
# print(arr)
# temp = arr.pop(0)
# arr.remove(arr[1])
# print(arr)

def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Handle the case where d is greater than the array length

    rotated_arr = arr[d:] + arr[:d]
    return rotated_arr

N = 7
arr = [1, 2, 3, 4, 5, 6, 7]
D = 2
rotated_result = rotate_array(arr, D)
print("Original Array:", arr)
print(f"Rotated Array by {D} positions:", rotated_result)











# d = 2
# i = 0
# print(arr)
# # temp = arr.pop(1)
#
# while i < d:
#     # print(i)
#     arr.remove(arr[i])
#     arr.append(arr[i])
#     i = i + 1
# print(arr)




