# 3.Enter 3 angles(degree) and find the sum of 3 angles also find is a triangle or not.
# The sum of the angles of a triangle is always 180 degree.

angle1 = int(input("Enter the angle1: "))
angle2 = int(input("Enter the angle2: "))
angle3 = int(input("Enter the angle3: "))

sum = angle1 + angle2 + angle3
print(f"The sum of three angle is {sum}")

# Switch case in Python replacement
# Python 3.8 does not support match statement
'''
match sum:
    case 180:
        print("Trangle is valid")
    case default:
        print("Trangle is not valid")
'''

# using If-else
if sum == 180:
    print("Trangle is valid")
else:
    print("Trangle is not valid")



