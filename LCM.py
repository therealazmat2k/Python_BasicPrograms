#This is a helper function for lcm_of_two_numbers function
def gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 < num2:
        return gcd(num1, num2-num1)
    return gcd(num1-num2, num2)
#This is a helper function for lcm function
def lcm_of_two_numbers(num1, num2):
    return num1*num2//gcd(num1, num2)
def lcm(*args):
    if len(args) < 2:
        return "At least two numbers are required to calculate lcm"
    lcm = lcm_of_two_numbers(args[0], args[1])
    for i in range(2, len(args)):
        lcm = lcm_of_two_numbers(lcm, args[i])
    return lcm
print(lcm_of_two_numbers(5, 40))
print(lcm(10,20,30,40))
