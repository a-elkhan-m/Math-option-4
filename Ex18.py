import math

x = 5.34 - 2 * math.pi
s = 0
k = 0

while True:
    a = (-1)**k * x**(2*k+1) / math.factorial(2*k+1)
    s += a

    if abs(a) < 10**-6:
        break

    k += 1

print(s)
print(k + 1)
