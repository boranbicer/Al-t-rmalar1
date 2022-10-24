a=int(input("3 veya 4 basamaklı bir sayı giriniz"))
if int(str(a))==int(str(a)[::-1]):
    print("palindromiktir")
else:
    print("palindromik değildir")
