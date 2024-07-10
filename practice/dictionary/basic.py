a = {}
print(type(a), a)

a = {1: "C", 2:" C++", 3:"Python"}
print(a, type(a))

# using dict()
a = dict({4: "C", 2:" C++", 3:"Python"})
print(a, type(a))

print(a[3])

# using get()
print(a.get(4))