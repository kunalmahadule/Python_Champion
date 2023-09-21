# # For a given number N check if it is prime or not. A prime number is a number which is only
# # divisible by 1 and itself.
# N = int(input("Enter Number: "))
#
# if N % 1 == 0 and N % N == 0:
#     print("Yes, The number is Prime.")
# else:
#     print("No, The number is not Prime.")


import math

def isPrime(N):
    if N <= 1:
        return 0  # 0 and 1 are not prime

    if N <= 3:
        return 1  # 2 and 3 are prime

    if N % 2 == 0:
        return 0  # Even numbers greater than 2 are not prime

    sqrt_N = int(math.sqrt(N))

    for i in range(3, sqrt_N + 1, 2):
        if N % i == 0:
            return 0  # N is divisible by i, not prime

    return 1  # N is prime


# Example usage:
N1 = 5
result1 = isPrime(N1)
print(result1)  # Output: 1 (5 is prime)

N2 = 25
result2 = isPrime(N2)
print(result2)  # Output: 0 (25 is not prime)
