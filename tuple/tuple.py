#list
a = [1,2,3]
print(type(a))

#tuple
a = (1,2,3)
print(type(a))
b = (2)
print(type(b))

#tuple with single value
b = (2,)
print(type(b))

c = 2,3,4,5
print(type(c))

# list to tuple

x = [1,2,3,4]
z = tuple(x)
print(type(x),type(z))

# nested tuple
a = (1,2,3,(4,5,6))
print(a)
print(type(a))

a = 1,"w",2,"t",3
print(a)
print(type(a))