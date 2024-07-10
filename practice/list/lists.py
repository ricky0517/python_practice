# creating lists
# 2 ways

a = [] # empty list
print(a)

b = [1, 2, 3, 4, 5, 6]
print(b)

# using split function
s = "I am coder"
c = s.split()
print(c)

x = list(range(40, 60, 3))
print(x)

y = ["python", "rocks"]
print(y)

z = [1, "b"]
print(z)

q = [1, 2, ["a","b"]]
print(q)
print(q[1])
print(q[2])
print(q[2][1])

#  slicing # list-name[start: stop: step]
print(b[0: 6: 2])
print(b[6:0:-1])
