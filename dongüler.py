import random
while True:
 n = random.randint(1, 20)
 print("Rastgele seçilen ", n)
 if n % 2 == 0:
     print("Çift sayı seçildi, döngü bitti")
     break

import random
while True:
 n = random.randint(1, 20)
 print("Rastgele seçilen ", n)
 if n % 2 == 0:
   print("Çift sayı seçildi, döngü bitti")
   break


sayi = int(input("Bir sayı girin: "))
for i in range(1, 10):
 if i == sayi:
   break
   print(i)
print("Döngü sona erdi")


sayi = int(input("Bir sayı girin: "))
for i in range(1, 10):
 if i == sayi:
  break
 print(i)
print("Döngü sona erdi")


metin = "Ankara"
for i in metin:
 if i == 'r':
   break
 print(i)


sayilar=[10, 11, 12, 13, 14, 15, 16]
for aranan in sayilar:
 print(aranan)
 if(aranan==14):
  print("14 sayısı bulundu")
  break


while True:
    girilensayi=int(input("bir sayı giriniz ve 1'den 5'e kadar olsun:"))
    if  1 <= girilensayi <= 5 :
        print(girilensayi,"girildiği için döngü sonda erdi")
        break
        




while True:
    sifre=input("En az 8 haneli bir şifre giriniz:")
    if len(sifre) >=8 : 
        print("şifreniz onaylandı")
        break
    else:
        print("Lütfen En az 8 haneli şifre girinizi")





harfler = ["a", "b", "c", "d", "e", "f", "g", "h"]  

for harf in harfler:  
    if harf == "e":
        print("döngü durdu")
        break  
    print(harf)  





denemesayisi=0
while True:
    sifre=input("Şifreyi giriniz:")
    denemesayisi+=1
    if sifre=="Python":
        print("Giriş Başarılı")
        print(denemesayisi,"tekrarda girdiniz")
        break
    else:
        print("tekrar deneyiniz")





while True:
    oyunbaslama=input("oyun başlatılsınmı?:")
    if oyunbaslama=="evet":
       print("oyun başlatıldı")
    elif oyunbaslama == "hayır":
         print ("oyun sona erdi")
         break
    oyunadevametme=input("oyuna devam edecek misin: ")
    if oyunadevametme=="evet":
       print ("oyun devam ediyor")
    elif oyunadevametme == "hayır":
         print("oyun sona erdi")
         break
    else:
         print("Yanlış Cvp evet/hayır yazın")



toplam=0
sayac=0
while True:
    sayi=int(input("Bir sayı giriniz:"))
    if sayi == 1:
        break
    toplam += sayi
    sayac+=1

if sayac > 0:
    print("sayıların ortalaması",toplam / sayac)




def toplama():
  sayi_adedi = int(input("Kaç tane sayı toplamak istersiniz? "))
  toplam = 0

  for i in range(sayi_adedi):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    toplam += sayi

  print("Sayıların toplamı:", toplam)

toplama()






isim=input("İsminizi Giriniz:")
#isim=["P","Y","T","H","O","N"]
for ad in isim:
    print(ad*5)





ayilar=[10,11,12,13,14,15,16,17,18,19,20]
for sayi in sayilar:
if sayi%3==0:
print(sayi)




alan_adi=”bilişim”
toplam=0
for aranan in alan_adi:
if aranan==”i”:
toplam=toplam+1
print(“Bu metinde toplam “,toplam,” adet i vardır”)





i=1
sonuc=1
faktoriyel=int(input(“Faktoriyeli hesaplanacak sayıyı giriniz: “))
while (i<=faktoriyel):
sonuc=i*sonuc
i=i+1
print(“Sonuc=”,sonuc)
