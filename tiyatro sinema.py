tercih=input("sinema/tiyatro hangisini tercih edersin?:")
ogrenci_misin=input("öğrenci misin?:")

fiyat=0
indirim=0.5

if tercih=="sinema":
    fiyat+=15
elif tercih=="tiyatro":
    fiyat+=10
if ogrenci_misin == "evet":
    fiyat*=indirim
print(fiyat)
