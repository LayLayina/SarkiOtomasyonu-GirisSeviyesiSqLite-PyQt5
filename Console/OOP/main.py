"""
Proje 2
Siz de bir tane Şarkı projesi geliştirmeye çalışın.
Örnek özellikler;
1. Şarkı İsmi 
2. Sanatçı
 3. Albüm
4. Prodüksiyon Şirketi
5. Şarkı Süresi
Örnek Metodlar;
1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
2. Şarkı Ekle
3. Şarkı Sil
"""

import sqlite3 as sq

class Sarkı():
    def __init__(self,isim,sanatcı,albüm,sirket,süre):
        
        self.isim = isim
        self.sanatcı = sanatcı
        self.albüm = albüm
        self.sirket = sirket 
        self.süre = süre

    def __str__(self):
        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirket: {}\nŞarkı Süre: {}".format(self.isim,self.sanatcı,self.albüm,self.sirket,self.süre)


class Mp3():
    def __init__(self):

        self.veritaban_baglantı_connect()

    def veritaban_baglantı_connect(self):

        self.connect = sq.connect("veritabanı.db")

        self.curs = self.connect.cursor()

        sorgu = "Create Table If not exists sarkılar (isim TEXT NOT NULL, sanatçı TEXT NOT NULL, albüm TEXT NOT NULL, \
            sirket TEXT NOT NULL, süre INT NOT NULL)"

        self.curs.execute(sorgu)

        self.connect.commit()

    def connect_kes(self):
        self.connect.close()

    def sarkıları_goster(self):
        sorgu = "Select * From sarkılar"

        self.curs.execute(sorgu)

        sarkılar = self.curs.fetchall()

        if (len(sarkılar) == 0):
            print("Şarkı Bulunmuyor....")
        
        else:
            for i in sarkılar:
                sarkı = Sarkı(i[0],i[1],i[2],i[3],i[4])
                print(sarkı)

    
    def sarkı_sorgula(self,isim):

        sorgu = "Select * From sarkılar where isim = ?"

        self.curs.execute(sorgu,(isim,))


        sarkılar = self.curs.fetchall()


        if (len(sarkılar) == 0):
            print("Böyle Bir Şarkı Bulunmuyor....")

        else:
            sarkı = Sarkı(sarkılar[0][0],sarkılar[0][1],sarkılar[0][2],sarkılar[0][3],sarkılar[0][4])
            print(sarkı)

    def sarkı_ekle(self,sarkı):
        sorgu = "INSERT INTO sarkılar VALUES (?,?,?,?,?)" 

        self.curs.execute(sorgu,(sarkı.isim,sarkı.sanatcı,sarkı.albüm,sarkı.sirket,sarkı.süre))

        self.connect.commit()

    def sarkı_sil(self,isim):
        sorgu = "Delete From sarkılar where isim = ?"

        self.curs.execute(sorgu,(isim,))

    def süre_hesapla(self):
        sorgu = "Select SUM(süre) From sarkılar"

        self.curs.execute(sorgu)

        data = self.curs.fetchall()

        print(data[0][0])


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