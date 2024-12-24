# Kullanıcıdan 4 basamaklı bir sayı alalım
sayi = int(input("4 basamaklı bir sayı girin: "))

# Basamakları bulma
binler = sayi // 1000
yuzler = (sayi // 100) % 10
onlar = (sayi // 10) % 10
birler = sayi % 10

# Sonuçları yazdırma
print("Binler basamağı: ", binler)
print("Yüzler basamağı: ", yuzler)
print("Onlar basamağı: ", onlar)
print("Birler basamağı: ", birler)

# Kullanıcıdan 4 basamaklı bir sayı alalım
sayi = int(input("4 basamaklı bir sayı girin: "))

# Basamakları bulma
binler = (sayi // 1000) * 1000
yuzler = (sayi // 100 % 10) * 100
onlar = (sayi // 10 % 10) * 10
birler = sayi % 10

# Sonuçları yazdırma
print(f"{binler} + {yuzler} + {onlar} + {birler}")
