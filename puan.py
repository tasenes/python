# Başlangıç puanı
toplam_puan = 0

# Yaşa göre puan
yas = int(input("Yaşınızı girin: "))
if yas < 20:
    toplam_puan += 100
elif yas <40:
    toplam_puan+=50
else:
    toplam_puan+=30
    
# Eve göre puan
ev_var_mi = input("Eviniz var mı? (Evet/Hayır): ")
if ev_var_mi == "evet":
    toplam_puan += 30

# Arabaya göre puan
araba_var_mi = input("Arabanız var mı? (Evet/Hayır): ")
if araba_var_mi == "evet":
    marka = input("Arabanızın markası nedir? (Togg/Tofaş): ")
    toplam_puan += 50  # Genel araba puanı
    if marka == "togg":
        toplam_puan += 100
    elif marka == "tofaş":
        toplam_puan += 30

# Sonuç
print(f"Toplam puanınız: {toplam_puan}")
