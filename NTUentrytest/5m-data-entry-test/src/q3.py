import regex as re
import json
def update_dictionary(dct, key, value, /):
    ##dct, key, value, /
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    new_dct = {}

    # Check if key, value exist
    if new_dct.get(key) is not None:
        print("Key present and the value is: ", new_dct[key])
        # Update the value to the key
        new_dct[key] = value
        return new_dct
    print("Orginal dictionary: ",new_dct)

    if new_dct.get(key) is None:
        print("No key present")
        # Update the value to the key
        new_dct.update({key: str(value)})

        # Check items in dictionary match
        try:
            for i in dct:
                if "age" in dct:
                    # print("key 'age' exists")
                    new_dct.update({key: str(value)})
                if "name" in dct:
                    # print("key 'name' exists")
                    s = str(dct)
                    for i in range(3):
                        # if dct[i] is re.match(r"a-zA-Z", s):
                        if dct[i] is not "name":
                            new_dct.update({"name": dct[i]})
                # print(new_dct)
        except KeyError:
            print("Key 'age' does not exist")
    print("Updated dictionary: ", new_dct)





# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
dct = {}, "name", "Alice"
#update_dictionary({"age": 25}, "age", 26)
dtc = {"age": 25}
update_dictionary(dct,"age", 26)
#update_dictionary(dct,)