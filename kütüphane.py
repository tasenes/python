kutuphane=["küçük prens","chalie'ni çikolata fabrikası","Ağaçta bir kuş","Pippi uzun çorap","kırmızı başlıklı kız"]
ara=input("hangi kitabı araştırmak istiyorsun?: ")

if ara == "küçük prens":
    print("Küçük Prens kitabı 117 sayfadır.")
    
if ara == "chalie'nin çikolata fabrikası":
    print("Chalie'nin Çikolata Fabrikası kitabı 190 sayfadır.")
    
if ara == "ağaçta bir kuş":
    print("Ağaçta Bir Kuş kitabı 150 sayfadır.")
    
if ara == "pippi uzun çorap":
   print("Pippi Uzun Çorap kitabı 120 sayfadır.")
    
if ara == "kırmızı başlıklı kız":
    print("Kırmızı Başlıklı Kız kitabı 32 sayfadır.")
    
else:
    print("Hayır,listede yok.")

kutuphane.append(input("hangi kitabı eklemek istiyorsun?: "))
print (kutuphane)

print(kutuphane.index(input("hangi kitabın hangi sırada olduğunu öğrenmek istiyorsun?: ")))
