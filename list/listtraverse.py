b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(b):
    print(b[i],i)
    i += 1

for i in b:
    print(i)

n = len(b)
for i in range(n):
    print(i,":",b[i])
