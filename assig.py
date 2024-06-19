a = 10
b = a
print(id(a), id(b))
print(a, b, type(a), type(b))
b += a
print(b)
print(id(a), id(b))
b -= a
print(b)
print(id(b))

# *= %= /= //= all works
