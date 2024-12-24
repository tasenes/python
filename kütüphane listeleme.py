kitap_isimleri = ["Kiraz Ağacı","Endülüs'te Bir Hafta","Rich Dad Poor Dad","Kapatuka"]
sayfa_sayisi = [207, 272, 292, 176]

soru = input("Arama mı yapacaksınız?")

if soru=="evet":
                
           aranacak_kitap = input("Hangi kitabı arıyorsunuz?")

           if aranacak_kitap in kitap_isimleri:
                                      siraNo=kitap_isimleri.index(aranacak_kitap)
                                      print(aranacak_kitap,"kütüphanede var",sayfa_sayisi[siraNo], "sayfadır")

           else:
                print(aranacak_kitap, "kitabı bizde yoktur.")

else:
     ekleme = int(input("kaçıncı siraya ekleme yapıcaksın?"))
     kitap_ismi= input("kitab ismi giriniz")
     sayfa= input("sayfa sayısı giriniz")
     kitap_isimleri.insert(ekleme,kitap_ismi)
     sayfa_sayisi.insert(ekleme,sayfa)
     print(kitap_isimleri)
     print(sayfa_sayisi)

