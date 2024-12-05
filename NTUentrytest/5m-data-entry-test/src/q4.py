import re
def string_reverse(s,/):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    #s = input('Key in a valid string to obtain the inverse string: ')
    s = str(s)
    if re.match(r"^[a-zA-Z0-9]+$", "s" ):
        print("Entry is valid! The reversed string is: ", s[::-1])
    else:
        print("Entry is not valid!")

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

string_reverse("Hellow World")
string_reverse("Python")