import re

find_functions = []

for function in dir(re):
    if "find" in function:
        find_functions.append(function)

sorted(find_functions)
print(find_functions)