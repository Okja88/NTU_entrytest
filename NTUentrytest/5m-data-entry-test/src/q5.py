def check_divisibility(num, divisor, /):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    choice = input('Key in 1 for a set of number and divisor: 10,2'
                   '\nOR '
                   '\nKey in 2 for a set of number and divisor: 7,3 '
                   '\nOR '
                   '\nKey in 3 to provide own set of number and divisor: '
                   )
    choice = int(choice)
    if str(num).isnumeric() and str(divisor).isnumeric():
        if choice == 1:
            num, divisor = 10, 2
            if num % divisor == 0: #To check if divisor is 2, no remainder
                print("Divide by two")
                print(f"This is valid as a num and a divisor: True")
        elif choice == 2:
            num, divisor = 7, 3
            if num % divisor != 0:
                print("Not divided by 2")
                print(f"This is not valid for divisibility")
        elif choice == 3:
            num = input('Key in a number: ')
            divisor = input('Key in a divisor: ')

            num = int(num)
            divisor = int(divisor)

            if str(num).isnumeric() and str(divisor).isnumeric():
                if num % divisor == 0: #To check if divisor is 2, no remainder
                    print(f"This is valid as a num and a divisor: True")
                if num % divisor != 0:
                    print(f"This is not valid for divisibility")
            else:
                print("This is not valid")

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
#num, divisor = 10,2
num, divisor = 7,3
check_divisibility(num,divisor)
