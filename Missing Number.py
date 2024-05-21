'''N = 4
A[] = {1, 4, 3}
Output:
2
Explanation:
Vaibhav placed 4 integers but he picked
up only 3 numbers. So missing number
will be 2 as it will become 1,2,3,4.'''


def missingNumber(A, N):
    # Your code goes here
    A.sort()

    maxA = max(A)
    minA = min(A)

    for i in range(minA, maxA + 1):
        if i not in A:
            return i


# A = [1, 4, 3]
A = [2, 5, 3, 1]
N = len(A)

res = missingNumber(A, N)
print(res)
