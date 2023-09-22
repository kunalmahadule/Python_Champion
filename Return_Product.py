arr = [1,2,3,4]
res = 1

for x in arr:
    res = res*x

print(res)

'''
GFG SOLUTION
#User function Template for python3

# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    
    # arr = [1,2,3,4]
    res = 1
    
    for x in arr:
        res = res*x
    
    return (res)%mod
'''