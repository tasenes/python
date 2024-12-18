def sifre_dogrulama():
    while True:
        sifre = input("Şifreyi girin: ")
        if sifre == "Python":
            print("Giriş başarılı")
            break
        else:
            print("Tekrar deneyiniz")

sifre_dogrulama()
