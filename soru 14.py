
a = []
for i in range(1,121212):
    for j in range(1,121212):
        if i*j == 121212:
            a.append((abs(i-j),i,j))

for k in a:
    if k==min(a):
        print(k[1],k[2])
        break
