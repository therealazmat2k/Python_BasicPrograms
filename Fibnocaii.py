
def fibonacci(n, seed1=0, seed2=1):
    if n < 2:
        return # Return because fibonacci sequence must be at least 2 elements long

    fib_arr = [seed1, seed2]
    if n == 2:
        return fib_arr

    for i in range(2, n):
        fib_arr.append(seed1+seed2)
        seed1, seed2 = seed2, fib_arr[i]

    return fib_arr

n = 10

print(f"Fibonacci sequence of {n} terms = {fibonacci(n)}")
