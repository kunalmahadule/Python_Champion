'''
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

row = 1
n = int(input())

while row <= n:
    column = 1
    while column <= n:
        print(column, "", end=" ")
        column = column + 1
    print()
    row = row + 1
'''

'''
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1

row = 1
n = int(input())
while row <= n:
    column = 1
    i = n
    while column <= n:
        print(i, "", end="")
        i = i - 1
        column = column + 1

    print()
    row = row + 1
'''

'''
1 2 3
4 5 6
7 8 9

row = 1
n = 3
i = 1
while row <= n:
    column = 1
    while column <= n:
        print(i, "", end="")
        i = i + 1
        column = column + 1
    print()
    row = row + 1
'''

'''
*
* *
* * *
* * * *

i = 1
n = int(input("enter the row: "))
while i <= n:
    print("* "*i)
    i += 1
'''

'''
1
2 2
3 3 3
4 4 4 4

i = 1
n = int(input("enter the row: "))
while i <= n:
    print(f"{i} "*i)
    i += 1
'''

'''
Write a python program to print below pattern
1
2 3
4 5 6
7 8 9 10

n = int(input("Enter row: "))
row = 1
i = 1

while row <= n:
    col = 1
    while col <= row:
        print(i, end=" ")
        col = col + 1
        i = i + 1

    print()
    row = row + 1
'''
'''
1
2 3
3 4 5
4 5 6 7

n = int(input("Enter row: ")) #4
row = 1

while row <= n:
    col = 1
    value = row # How to solve without this
    while col <= row:
        print(value, end=" ")
        col += 1
        value += 1

    print()
    row += 1
'''
'''
1
2 1
3 2 1
4 3 2 1

n = int(input("Enter row: "))
row = 1
while row <= n:
    col = 1
    # i = row
    while col <= row:
        # print(i, end=" ")
        print(row - col + 1, end=" ")
        # i = i - 1
        col = col + 1

    print()
    row = row + 1
'''
'''
A A A
B B B
C C C

n = int(input("Enter row: "))
row = 1
while row <= n:
    col = 1
    while col <= n:
        temp = int('A' + row - 1) #--> Problem is in that line
        char temp = 'A' + row - 1
        print(temp, end=" ")

        col += 1

    print()
    row += 1
'''
# timestamp = 28:00
'''
A B C
A B C
A B C

# 'A'+col-1
n = int(input('     : '))
row = 1

while row<=n:
    col = 1

    while col <=n:
        print('A', end=" ")
        col += 1

    print()
    row += 1
'''

'''
A B C
D E F
G H I
'''


j = 6
g = 3.3
print(j/g)













