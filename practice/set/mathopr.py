a = {1, 2, 3, 4}
b = {3, 4, 5, 6, 7}
# union()
print(a.union(b))
print(a | b)
# intersection()
print(a.intersection(b))
print(a & b)

# difference()
print(a.difference(b))
print(b.difference(a))
print(a - b) # b - a

# symentric_difference()
print(a.symmetric_difference(b))
print(a ^ b)
