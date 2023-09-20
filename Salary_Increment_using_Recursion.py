# 1. Write a program for take input from user =1.Enter first salary 2.Enter how may years salary do
# you want to print, in every year 10% of current salary will be add in next years salary.

currnetSalary = int(input("Enter Starting Salary:  "))
years = int(input("Enter Years:  "))
print(f"First Salary is:  {currnetSalary}")


for i in range(years):
    increment = currnetSalary * 0.1

    currnetSalary = currnetSalary + increment
    print(currnetSalary) #As per Aniket output

print(f"After {years} year your salary will be {currnetSalary}")
