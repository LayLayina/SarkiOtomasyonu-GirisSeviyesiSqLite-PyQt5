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
