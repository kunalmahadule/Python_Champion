'''
N = 4
arr[] = {1, 5, 3, 2}
Output: 1
Explanation:
Sum of first 2 elements is 1 + 5  = 6,
Sum of last 2 elements is 3 + 2  = 5,
To make the array balanced you can add 1.'''

# arr = [1, 5, 3, 2]
# n = len(arr)


def find_min_balance_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    min_balance_index = None
    min_balance = float('inf')

    for i in range(len(arr) - 1):
        left_sum += arr[i]
        right_sum = total_sum - left_sum
        balance = abs(left_sum - right_sum)

        if balance < min_balance:
            min_balance = balance
            min_balance_index = i

    return min_balance_index

# Example usage:
N = 4
arr = [1, 5, 3, 2]
min_balance_index = find_min_balance_index(arr)
print(min_balance_index)











