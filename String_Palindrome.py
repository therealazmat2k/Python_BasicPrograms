def string_reverse(inp_str):
    return inp_str[:: -1]


def check_palindrome(inp_str):
    rev_str = string_reverse(inp_str)

    if inp_str == rev_str:
        return True
    else:
        return False


print(check_palindrome("aba"))
