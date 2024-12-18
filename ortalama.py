def ortalama_hesapla():
    toplam = 0
    sayac = 0

    while True:
        sayi = input("Bir sayı girin (1 ile durdurun): ")
        if sayi == "1":
            break
        if len([harf for harf in sayi if harf not in "0123456789"]) == 0 and sayi:
            toplam += int(sayi)
            sayac += 1
        else:
            print("Lütfen geçerli bir sayı girin.")

    if sayac == 0:
        print("Hiç geçerli sayı girilmedi.")
    else:
        ortalama = toplam / sayac
        print("Girilen sayıların ortalaması:", int(ortalama * 100) / 100)

ortalama_hesapla()
