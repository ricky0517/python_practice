i = 10
while i < 50:
    print(i)
    i += 1
    if i > 30:
        break
    print("last statement")
print("broke here")

b = [1,2,3,4,5,6]
for x in b:
    if x == 3:
        break
    print(x)
print("done")