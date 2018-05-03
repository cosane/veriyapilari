# 100 kişinin isim bilgisini kullanıcıdan alıp
# bunu bir listeye giren program.
# boş girişler ve rakamla başlayan isimler
# kabul edilmez.
# GEÇ ve ÇIK anahtar kelimeleri o sırayı atlamayı
# ya da isim talep etme işinden tamamen vazgeçmeyi
# sağlar.

isimler = []
isim = ''
def ilkHarfiKontrolEt(metin):
    # kendisine verilen metnin ilk karakterini
    # kontrol eder ve eğer bir rakama rastlarsa
    # False sonuç döndürür. Rastlamazsa True döner.
    if len(metin) > 0:
        for sayı in range(10):
            if metin[0] == str(sayı):
                return False
    return True

for sayac in range(100):
    while isim == '' or ilkHarfiKontrolEt(isim) == False:
        # isim değişkeni boşsa veya ilk karakter rakam
        # ise sürekli istemeye devam etsin diye while
        # döngüsü kurduk
        isim = input(str(sayac+1) + ' numaralı ismi girin: ')
    
    if isim == "ÇIK":
        break
    if isim == "GEÇ":
        # girdiyi temizle
        isim = ''
        print("GEÇİLDİ")
        # listeye boş bir isim ekle
        isimler.append('')
        continue

    # girdiyi listeye ekle
    isimler.append(isim)
    # girdiyi temizle
    isim = ''

# kaç kişilik bir liste olduğunu yazdır
print("toplam", len(isimler), "kişi mevcut")

# listedeki tüm isimleri sırayla yazdır
for sıradaki in isimler:
    print(sıradaki)