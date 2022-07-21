def check_leap(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        print(" The Year is a leap Year ")
    else:
        print(" The year is not leap year ")


check_leap(2000)
