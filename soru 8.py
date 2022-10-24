for i in range(100,1000):
    if i%2==0 and int(str(i)[0])!=int(str(i)[1]) and int(str(i)[0])!=int(str(i)[2]) and int(str(i)[1])!=int(str(i)[2]):
        print(i)
