'''Input:
s = GeeksForGeeks, x = For
Output: 5
Explanation: For is present as substring
in GeeksForGeeks from index 5 (0 based
indexing).'''

# s = 'GeeksForGeeks'
# x = 'For'
#
# if x[0] in s:
#     print(s.index(x[0]))
# else:
#     print('-1')

def strstr(s, x):
    # Iterate through the string 's'
    for i in range(len(s) - len(x) + 1):
        # Check if the substring of 's' starting at index 'i' and of length 'len(x)' is equal to 'x'
        if s[i:i + len(x)] == x:
            return i  # Found a match, return the starting index of 'x'

    return -1  # 'x' is not present in 's'


# Example usage:
s = "GeeksForGeeks"
x = "Fr"
result = strstr(s, x)
print("Index of '{}' in '{}': {}".format(x, s, result))















