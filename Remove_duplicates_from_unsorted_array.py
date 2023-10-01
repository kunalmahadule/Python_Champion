# Remove duplicates form unsorted array

# approach 1
A = [1, 10, 1, 4, 1, 2, 6, 8, 8, 5, 8, 9]
N = len(A)
out = []
def removeDuplicate(A, N):
    return list(set(A))  # set remove duplicates but also sort the array

a = removeDuplicate(A, N)
print(a)

# approach 2 from ChatGpt
# This function remove duplicates but not sort the array
nums = [1, 10, 1, 4, 10]

unique_nums = set()
result = []
for num in nums:
    if num not in unique_nums:
        unique_nums.add(num)
        result.append(num)

print("Array after removing duplicates:", result)