import os

# dizin = os.listdir("/home/halil/Belgeler/Yeniden_Adlandir")    # Yeniden adlandirilacak dosyalarin bulunduğu dizin yolu
# dizin = input("Yeniden adlandirilacak dosyalarin bulunduğu dizin yolunu belirtin")

# if dizin == "":
#     dizin = dizin_orj
# else:
#     dizin = os.listdir(dizin)
# print(dizin)

dizin = os.getcwd()

Yeni_Dosya_Adi = input("Dosyalara Verilecek Yeni Adı Belirtin: ")

sayac_1 = 1
yeni_dosya_adi_listesi = []

for dosya_adi in dizin:
    if (dosya_adi.count(".") >=1 ):     # sadece dosyaları seçmek için bu kontrolü yazdım, Klasörleri adlandırmayacağım.
        uzanti_indeksi = dosya_adi.rfind(".")   # dosya uzantisinin indis değerini tespit ettim.
        uzanti = dosya_adi[uzanti_indeksi:]     # dosya uzantisini aldım
        yeni_dosya_adi_listesi.append(Yeni_Dosya_Adi + str(sayac_1) + uzanti)
        sayac_1 += 1

print(yeni_dosya_adi_listesi)

# sayac_2 = 0
# for i in dizin:
#     if (i.count(".") >=1 ):     # sadece dosyaları seçmek için bu kontrolü yazdım, Klasörleri adlandırmayacağım.
#         os.rename(dizin[sayac_2], yeni_dosya_adi_listesi[sayac_2])
#         sayac_2 += 1


