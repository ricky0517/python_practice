# unorderer
# duplicate values are not allowed
# insertion order is not preserved
# mutable

s = {1,2,3,4,5}
print(s)

s = {1,1}
print(s)

s = {1, "e", "hey"}
print(s)

# list to set
l = [1,2,3]
s = set(l)
print(s)
print(type(s))
a = {1,2,4}
print(a)