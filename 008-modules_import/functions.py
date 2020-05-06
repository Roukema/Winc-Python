

def is_palindrome(s):
    # Calling reverse function
    reverse = s[::-1]
    # Checking if both string are equal or not
    if s == reverse:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


def is_even(n):
    if (n % 2) == 0:
        print(f"{n} is even")


def is_odd(n):
    if (n % 2) != 0:
        print(f"{n} is not even but odd")


# 2
def contains_only_ints(list_input):
    string_input = ""
    for elements in list_input:
        string_input += str(elements)

    if string_input.isdigit():
        print(f'list has only integers')
    else:
        print(f'list has not only integers')


def sum_list(list_input):
    resultaat = sum(list_input)
    print(f'the result is: {resultaat}')
