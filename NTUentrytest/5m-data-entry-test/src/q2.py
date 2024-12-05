def find_and_replace( lst, /,):

    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    choice = input('Key in 1 for numeric list of [1, 2, 3, 4, 2, 2], 2, 5,'
                   '\nOR '
                   '\nKey in 2 for string list of ["apple", "banana", "apple"], "apple", "orange" : ')
    choice = int(choice)
    if choice == 1:
        #print(lst)
        lst = [[1, 2, 3, 4, 2, 2], 2, 5]
        # print(lst[2])
        new_lst = []
        python_indices = [index for (index, item) in enumerate(lst)]
        # print(python_indices)
        for i in lst[0]:
            # print(i)
            new_lst.append(i)
            # print(new_lst)
        # print(lst[1])
        # print(lst[2])
        b = lst[1]
        c = lst[2]
        new_lst.insert(6, b)
        new_lst.insert(7, c)
        print(f"Original List: ",new_lst)

        counter = 2
        i = 0
        r_item = 9
        for i in range(len(new_lst)):
            while i < len(new_lst):
                # replace counter with r_num
                if new_lst[i] == counter:
                    new_lst[i] = r_item
                i += 1
        print(f"Replaced list: ", new_lst)
    elif choice == 2:
        lst = [["apple", "banana", "apple"], "apple", "orange"]
        # print(lst[0])
        # print(lst[1])
        # print(lst[2])
        new_lst = []
        python_indices = [index for (index, item) in enumerate(lst)]
        # print(python_indices)
        for i in lst[0]:
            # print(i)
            new_lst.append(i)
            # print(new_lst)
        b = lst[1]
        c = lst[2]
        new_lst.insert(3, b)
        new_lst.insert(4, c)
        print(f"Original List: ", new_lst)

        counter = "apple"
        i = 0
        r_item = "pear"
        for i in range(len(new_lst)):
            while i < len(new_lst):
                # replace counter with r_num
                if new_lst[i] == counter:
                    new_lst[i] = r_item
                i += 1
        print(f"Replaced List: " ,new_lst)

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

lst = [[1, 2, 3, 4, 2, 2], 2, 5]
#a= [["apple", "banana", "apple"], "apple", "orange"]
find_and_replace(lst)





# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
