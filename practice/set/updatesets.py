# add()
import abc

s = {1,2,3}
print(s)
s.add(10)
print(s)

s.update([105,22])
print(s)
s.update(s, range(20))
print(s)

# copy()
a = s.copy()
print(a)