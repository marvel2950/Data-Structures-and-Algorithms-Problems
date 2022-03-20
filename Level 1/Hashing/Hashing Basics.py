d = {}
d[1] = 5
d[6] = 8
print(d)
for i,j in d.items():
    print(i,j)
print(list(d.keys()))
print(d.values())

d[6] = 'r'
print(d)

if 9 in d:
    print("Yes")
else:
    print("No")