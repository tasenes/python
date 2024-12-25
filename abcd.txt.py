A=toplam=0
sayi1=int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
if sayi1<sayi2:
    for sayilar in range(sayi1,sayi2):
        toplam+=sayilar
else:
    for sayilar in range(sayi2,sayi1):
        toplam+=sayilar
print(toplam)

C=carpım=1
sayi1=int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
for sayilar in range (sayi1,sayi2):
    carpım*=sayilar
print(carpım)

Ç=toplam=0
sayilar=[4,12,18,33]
for sayi in sayilar:
    toplam+=sayi
print(toplam)
