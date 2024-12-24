metin ="""
Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.
Çatma, kurban olayım çehreni ey nazlı hilâl!
Kahraman ırkıma bir gül… ne bu şiddet bu celâl?
Sana olmaz dökülen kanlarımız sonra helâl,
Hakkıdır, Hakk’a tapan, milletimin istiklâl."""

silinicekler = [",", ".", "?", "!",";"]
for degis in silinicekler:
    metin = metin.replace(degis, "")

kelimeler = metin.split()

aranan = input("hangi kelimeyi aramak istiyosun?  ")
bulunansayisi=0
toplamkelimeler=0

for kelime in kelimeler:
    toplamkelimeler+=1
    if(kelime == aranan):
        bulunansayisi+=1
print("bu metinde",toplamkelimeler, "kelime var , aradığınız ('", aranan, "') dan", bulunansayisi, "adet vardır")        
