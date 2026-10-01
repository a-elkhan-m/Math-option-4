import math

t = 0.21
eps = 10**-8

# e^t
e = 1
term = 1
k = 1

while abs(term) >= eps:
    term = term * t / k
    e += term
    k += 1

# cos(t)
c = 1
term = 1
k = 1

while abs(term) >= eps:
    term = -term * t*t / ((2*k-1)*(2*k))
    c += term
    k += 1

F = e * c

print("F =", F)
print("e^t =", e)
print("cos(t) =", c)
