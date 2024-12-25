sayilar1=int(input("1.sayıyı giriniz: "))
sayilar2=int(input("2.sayıyı giriniz: "))
sayilar3=int(input("3.sayıyı giriniz: "))
if sayilar1<sayilar2<sayilar3:
    print("en büyük sayı:",sayilar3)
elif sayilar2<sayilar3<sayilar1:
    print("en büyük sayı:",sayilar1)
else:
    print("en büyük sayı:",sayilar2)
