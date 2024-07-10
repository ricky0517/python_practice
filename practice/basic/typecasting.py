a = 1 + 2.4
print(a, type(a))
# implicit type casting

b = int(a) + 4
print(b, type(b))

c = "341"
d = 1 + int(c)
print(d)

print(int("1"))

print(float("23.456"))

print(complex(123))
print(complex(True))

print(complex("56"))
print(bool(0))
print(bool(5))

print(str(10.5 + 3j))
