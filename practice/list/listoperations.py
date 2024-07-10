a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11]
a[1] = 100
print(a)
# update using index

# by slicing
a[1:4] = [40,50,60,35]
print(a)

# append function
a.append(300)
a.append(500)
print(a)

# extend
a.extend([4,5,6,7,8])
print(a)

a.append([4,5,6,7,8])
print(a)

b = [1,4,6,7]
c = [3,5,7]
c.extend(b)
print(c)
c.insert(2,4)
print(c)

# deleting elements
del c[0]
print(c)
del c[5:8]
print(c)

b.remove(4)
print(b)

b.pop(0)
print(b)
b.clear()
print(b)
