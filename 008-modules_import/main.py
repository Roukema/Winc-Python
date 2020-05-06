import functions

import data  # opdracht 2

functions.is_odd(2)
functions.is_odd(3)
functions.is_even(2)
functions.is_even(3)
functions.is_palindrome("foo")
functions.is_palindrome("foof")

print(dir(data))
print(data)

# 2
print(f"-----------check lst1 -------------")
lst1 = data.lst1
functions.contains_only_ints(lst1)
functions.sum_list(lst1)
print(f"-----------check lst2 -------------")
lst2 = data.lst2
functions.contains_only_ints(data.lst2)
