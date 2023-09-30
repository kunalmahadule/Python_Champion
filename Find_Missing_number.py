# Missing number
''' Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:
Input:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}
n = len(A)
Output: 9'''

# A = [6, 1, 2, 8, 3, 4, 9, 10, 5]
A = [2]
d = 1
if len(A) == 1:
    if A[0]==2:
        print(d)
    else:
        print(d + 1)
n = len(A)
min_num = min(A)
max_num = max(A)
for x in range(min_num, max_num):
    if x not in A:
        print(x)

# def misnum(a, n):
#     d = 1
#     l = sorted(array)
#     for i in range(len(l)):
#         if l[i] != d:
#             return d
#         else:
#             d += 1
#     return d
#
#
# array = [6,1,2,8,3,4,9,10,5]
# n = len(array)
# print(misnum(array, n))
