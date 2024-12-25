sayi = input("Lütfen 4 basamaklı bir sayı girin: ")


if len(sayi) == 4 and sayi.isdigit():
    
    binler = sayi[0]
    yuzler = sayi[1]
    onlar = sayi[2]
    birler = sayi[3]
    
   
    print(f"Binler basamağı: {binler}")
    print(f"Yüzler basamağı: {yuzler}")
    print(f"Onlar basamağı: {onlar}")
    print(f"Birler basamağı: {birler}")
else:
    print("Lütfen geçerli bir 4 basamaklı sayı girin.")
