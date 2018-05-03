isimler = []
isim = ''
def ilkHarfiKontrolEt(metin):
    if len(metin) > 0:
        for sayı in range(10):
            if metin[0] == str(sayı):
                return False
    return True

for sayac in range(4):
    while isim == '' or ilkHarfiKontrolEt(isim) == False:
        isim = input(str(sayac+1) + ' numaralı ismi girin: ')
    
    if isim == "ÇIK":
        break
    if isim == "GEÇ":
        isim = ''
        print("GEÇİLDİ")
        isimler.append('')
        continue
    isimler.append(isim)
    isim = ''

print("toplam", len(isimler), "kişi mevcut")

for sıradaki in isimler:
    print(sıradaki)