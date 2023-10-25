arr = [11, 12, 13, 14, 15]
k = 1
result = [int(digit) for number in arr for digit in str(number)]
print(result)
print(result.count(k))
# print(out)