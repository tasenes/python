
# Kullanıcıya oyun devam etmek isteyip istemediği sorulacak
while True:
    cevap = input("Oyuna devam etmek istiyor musun? (Evet/Hayır): ")

    if cevap == "Evet":
        print("Oyuna devam ediyorsun...")
        # Burada oyunun devam ettiği kısmı ekleyebilirsiniz
    elif cevap == "Hayır":
        print("Oyun bitti. Hoşça kal!")
        break  # Döngüyü sonlandırır
    else:
        print("Lütfen geçerli bir cevap verin: Evet ya da Hayır.")
