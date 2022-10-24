a=int(input("bir sayı giriniz"))
for i in range(2,a):
    if a%i==0:
        print("asal değildir")
        break
    else:
        print("asaldır")
