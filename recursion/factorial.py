
# without recursion
def factorial_loop(n):
    if n == 0 or n == 1:
        return 1
    else:
        f = 1
        for v in range(1, n+1):
            f = f * v
        return f


# with recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_recursive(n-1) * n


print(factorial_loop(5))
print(factorial_recursive(5))