class Solution:
    def printFibb(self, n):
        n1, n2 = 0, 1
        arr = []
        if n == 0:
            return 'Please enter positive number.'
        elif n == 1:
            return [0]
        else:
            for i in range(n):
                arr.append(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth

            return arr

    def printArr(self, array):
        n = len(array)
        for i in range(1, n):
            print(array[i], end=" ")
        return None


obj = Solution()
output = obj.printFibb(6)
obj.printArr(output)
# 1  1  2  3  5  8  13

'''
def printFibb(n):
    output = []
    n1, n2 = 1, 1

    for i in range(n):
        output.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth

    return output

print(printFibb(6))
'''