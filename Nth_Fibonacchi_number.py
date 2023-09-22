n = int(input("Enter a number: "))

n1, n2 = 1, 1
arr = []
if n == 0:
    print("Enter positive integer")
elif n == 1:
    print("1 is the 2nd fibonacci number")
else:
    for i in range(n):
        # if i != 0:
        arr.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth

    # arr.remove(0)
    print(arr)
    # print(arr.index(2))
    print()
    print(arr[n-1],f" is the {n} number of fibonacci series")


# 354,224,848,179,261,915,075 -->100