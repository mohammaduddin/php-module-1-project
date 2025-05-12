
# The sum of numbers from 1 to 100

sum_of_numbers = 0
n = int(input("enter a number:"))

for i in range(1, n+1):
    sum_of_numbers = sum_of_numbers + i
    print(i, end=" ")
    
print("\nThe sum of numbers from 1 to 100 is:", sum_of_numbers)

