
def leap_year_with_variable_arguments(*args):
    ans = []
    for arg in args:
        if arg <= 0:
            ans.append("NOT A VALID YEAR")
        else:
            ans.append(True if (arg % 400 == 0) or (arg % 100 != 0) and (arg % 4 == 0) else False)
    return ans

print(leap_year_with_variable_arguments(2000, 2002, 2022))
