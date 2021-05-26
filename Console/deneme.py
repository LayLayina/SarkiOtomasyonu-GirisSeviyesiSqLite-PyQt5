from main import *
print("""***********************************
Kütüphane Programına Hoşgeldiniz.
İşlemler;
1. Şarkıları Göster
2. Şarkı Sorgulama
3. Şarkı Ekle
4. Şarkı Sil 
5. Süre Hesapla
Çıkmak için 'q' ya basın.
***********************************""")

mp3 = Mp3()

while True:

    işlem = input("Yapmak İstediğiniz İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Programdan Çıkılıyor....")
        break

    elif (işlem == "1"):
        mp3.sarkıları_goster()

    elif (işlem == "2"):
        isim = input("Sorgulamak İstediğiniz Şarkı İsmini Giriniz:")
        mp3.sarkı_sorgula(isim)

    elif (işlem == "3"):
        isim = input("Şarkı İsmi Giriniz:")
        sanatcı = input("Sanatçı İsmi Giriniz:")
        albüm = input("Albüm İsmi Giriniz:")
        sirket = input("Prodüksiyon Şirketinin İsmini Giriniz:")
        try:
            süre = int(input("Şarkının Süresini Giriniz:"))

        except Exception:
                print("Lütfen Sayı Değeri Giriniz:")

        yeni_sarkı = Sarkı(isim,sanatcı,albüm,sirket,süre)

        mp3.sarkı_ekle(yeni_sarkı)
        print("Şarkı Eklendi...")

    elif (işlem == "4"):
        islem = input("Silmek İstediğiniz Şarkı İsmini Giriniz:")

        mp3.sarkı_sil(islem)

    elif (işlem == "5"):
        mp3.süre_hesapla()

    else:
        print("Geçersiz İşlem...")