#2. Ası sayilar,elemanları sırasıyla 35,26,81,64 olan bir liste oluşturarak aşağıdaki işlemleri yapınız
#A) Listeyi büyükten küçüğe doğru sıralayınız

sayilar=["35","26","81","64"]
sayilar.sort()
print(sayilar)#['26', '35', '64', '81']

#B) Listeyi tersten yazdırınız.

sayilar2=["35","26","81","64"]
sayilar2.reverse()
print(sayilar2)#['64', '81', '26', '35']

#C) Listede kaç tane 26 tane elemanın oldğunu bulunuz

sayilar3=["35","26","81","64"]
say=sayilar3.count("26")
print(say)#1

#Ç) Listedeki 81 sayısını siliniz.

sayilar4=["35","26","81","64"]
del sayilar4[2]
print(sayilar4)#['35', '26', '64']

#D)Listenin tüm elemanlarını siliniz.

sayilar5=["35","26","81","64"]
sayilar5.clear()
print(sayilar5)#[]

#E)64 elemanının indeksini bulunuz.

sayilar6=["35","26","81","64"]
print(sayilar6.index("64"))#3

#F)Listeyi ondalikli_sayilar isimli,elemanları 1.4,6.8 olan liste ile birleştiriniz.

sayilar7=["35","26","81","64"]
ondalikli_sayilar=["1.4","6.8"]
sayilar7.extend(ondalikli_sayilar)
print(sayilar7)#['35', '26', '81', '64', '1.4', '6.8']
