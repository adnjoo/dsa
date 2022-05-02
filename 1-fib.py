# Fibonacci sequence is an integer sequence defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.

# most common algorithm is a recursive function that calls itself
# as many times as needed until it computes the desired Fibonacci number
# the max depth of the call tree is n, and since each function call
# produces two additional calls, the TC of this algorithm is 2 ^ N

def fib(n):
    if n in {0, 1}:
        return n
    return fib(n-1) + fib(n-2)


print(fib(7))
