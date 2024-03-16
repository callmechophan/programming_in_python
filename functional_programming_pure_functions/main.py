# +----------------------------+------------+------------+
# |                            | traditional|        pure|
# +-----------------------------------------+------------+
# |access global state         |          v |          x |
# |modify global variables     |          v |          x |
# |access local state          |          v |          v |
# |change args                 |          v |          x |
# |output depeneds on input    |          x |          v |
# +----------------------------+------------+------------+
# 
# pure functions
# - a pure functions is used in functional programming because it does not change args


arr = [1, 2, 3]

def add_to_lists(lists, element):
    new_lists = lists.copy()

    new_lists.append(element)

    return new_lists

new_arr = add_to_lists(arr, 4)
print(arr)
print(new_arr)
