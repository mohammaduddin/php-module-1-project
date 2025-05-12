# take user input as a number then multiplies all numbers,
# press 0 to get exit from the program.

numbers = []

while True:
    # try block to handle any issues/errors are catch while program is running
    try: 
        num = float(input("Enter a number to multiply     or   enter 0 to STOP the program:  "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")

if len(numbers) > 0:
    multiply = 1
    for number in numbers:
        multiply *= number
        print("The multiply of the numbers is: ", multiply)
else:
    print("No numbers were entered.")

# Output:
# Enter a number to multiply     or   enter 0 to STOP the program:  6
# Enter a number to multiply     or   enter 0 to STOP the program:  3
# Enter a number to multiply     or   enter 0 to STOP the program:  10
# Enter a number to multiply     or   enter 0 to STOP the program:  0
# The multiply of the numbers is:  6.0
# The multiply of the numbers is:  18.0
# The multiply of the numbers is:  180.0