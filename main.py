def hesabla(x, epsilon):
    cem = 0
    term = x
    n = 1
    while abs(term) > epsilon:
        cem += term
        n += 1
        term = (-1) ** (n - 1) * (x ** n) / n
    return cem

x = 0,1
epsilon = 0.01
print(hesabla(x, epsilon))

