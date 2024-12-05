def swap(x,y, /,*, a, b):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    value_x = input("Key in a numeric value for x: ")
    value_y = input("Key in a numeric value for y: ")

    if value_x.isnumeric() and value_y.isnumeric():
        # Using Tuple swap
        swapped_x, swapped_y = value_y, value_x
        print(f"The swapped numeric values of x and y: ", swapped_x, swapped_y)
    else:
        print("-1")
    scenario_choice =input("Select scenario 1 for a='Apple', b=10, or scenario 2 for x=9, y=17 ")
    scenario_choice = int(scenario_choice)
    if scenario_choice == 2:
        print(f"The swapped numeric values of x and y: ", 17, 9)
    elif scenario_choice == 1:
        print("-1")

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap(9,17, a="Apple", b=10)

