#1. Adı ders, elemanları sırasıyla B,İ,L,İ,Ş,İ,M olan bir liste oluşturarak aşağıdaki İşlemleri yapınız.

#A)Listeyi Alfabetik olarak sırala
ders1=["B","İ","L","İ","Ş","İ","M"]
ders1.sort()
print(ders1) #['B', 'L', 'M', 'İ', 'İ', 'İ', 'Ş']

#B)Listeyi tersten yazdırınız
ders2=["B","İ","L","İ","Ş","İ","M"]
ders2.reverse()
print(ders2)#['M', 'İ', 'Ş', 'İ', 'L', 'İ', 'B']

#C)Listede Kaç tane i olduğunu bulunuz
ders3=["B","İ","L","İ","Ş","İ","M"]
say=ders3.count("İ")
print(say)#3

#Ç)gerekli harfleri silerik listeyi B,İ,L,İ,M haline getiriniz
ders4=["B","İ","L","İ","Ş","İ","M"]
del ders4[4]
del ders4[4]
print(ders4)#['B', 'İ', 'L', 'İ', 'M']

#D)ders listesini alan listesini alan listesine kopyalayarak ekrana yazdırınız.

ders5=["B","İ","L","İ","Ş","İ","M"]
alan=ders5.copy()
print(alan)#['B', 'İ', 'L', 'İ', 'Ş', 'İ', 'M']
#E)Listenin tüm elamanlarını siliniz.

ders6=["B","İ","L","İ","Ş","İ","M"]
ders6.clear()
print(ders6)#[]

#F)L elemanının indeksini bulunuz.

ders7=["B","İ","L","İ","Ş","İ","M"]
print(ders7.index("L"))#2
