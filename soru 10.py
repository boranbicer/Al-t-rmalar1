a=[]
for i in range(10000,100000):
    if int(str(i)[0]) + int(str(i)[1])==int(str(i)[-1]) +int(str(i)[-2]):
        a.append(i)
print(len(a))
