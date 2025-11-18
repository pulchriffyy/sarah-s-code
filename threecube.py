def c(n):
    return n*n*n
def b(n):
    if n%3==0:
        return c(n)
    else:
        return False
print(b(21))
print(b(16))