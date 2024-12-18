def sifre_dogrulama():
    deneme_sayisi = 0
    while True:
        sifre = input("Şifreyi girin: ")
        deneme_sayisi += 1
        if sifre == "Enes":
            print(f"Giriş başarılı. Şifreyi {deneme_sayisi} denemede girdiniz.")
            break
        else:
            print("Tekrar deneyiniz")

sifre_dogrulama()
