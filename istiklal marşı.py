istiklal_marsı="""
Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.

Çatma, kurban olayım çehreni ey nazlı hilâl!
Kahraman ırkıma bir gül… ne bu şiddet bu celâl?
Sana olmaz dökülen kanlarımız sonra helâl,
Hakkıdır, Hakk’a tapan, milletimin istiklâl.
"""

istiklal_marsı=istiklal_marsı.lower()
karaktersilimi=[",","!","?",":",";","."]
for degis in karaktersilimi:
    istiklal_marsı=istiklal_marsı.replace(degis,"")
#print (istiklal_marsı)
istiklal_marsı=istiklal_marsı.split()

harf_secimi=input("hangi kelime/harfi aramak istiyorsunuz?:").lower()
toplam=0
for aranan in istiklal_marsı:
    if aranan==harf_secimi:
        toplam+=1
print("bu metinde toplam",toplam,"adeti",harf_secimi,"vardır?: ")
