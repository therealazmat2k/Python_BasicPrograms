def check_prime(inp_num):
    if inp_num <= 1:
        return "Please enter a valid number"

    flag = 0
    for i in range(2, inp_num//2 + 1):
        if inp_num % i == 0:
            flag = 1
            break
        else:
            continue

    return True if flag == 0 else False

def prime_in_range(start, end):
    if start < 2:
        start = 2

    for i in range(start, end+1):
        if check_prime(i):
            print(i)


prime_in_range(1, 50)
