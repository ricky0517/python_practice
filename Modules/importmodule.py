import module as m

# module aliasing
c = m.add(3, 50)
print(c)
print(m.sub(40, 5))

from module import *

print(add(5, 60))
print(sub(50, 5))