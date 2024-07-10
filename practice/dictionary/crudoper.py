a = dict({1: "java", 2: "c++"})
print(a)

a[1] = "Terraform"
print(a)
a[5] = "Python3"
print(a)
a.pop(2)
print(a)
a.popitem() # pops random
print(a)

b = dict({1: "java", 2: "c++"})
b[1] = "Terraform"
b[5] = "Python3"
print(b)

del b[2]
print(b)
# del b
# print(b)

b.clear()
print(b)
