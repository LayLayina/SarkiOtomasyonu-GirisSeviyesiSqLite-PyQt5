from os import scandir
import sqlite3 as sq

#---------------VERİTABANI OLUŞTUR-----------------#
#--------------------------------------------------#
global conn
global curs
conn = sq.connect("veritabanı.db")
curs = conn.cursor()

#----------------TABLO OLUŞTUR---------------------#
#--------------------------------------------------#

sarkı_sorgu = ("CREATE TABLE IF NOT EXISTS sarkılar (isim TEXT NOT NULL,sanatcı TEXT NOT NULL,albüm TEXT NOT NULL,sirket TEXT NOT NULL,süre TEXT NOT NULL)")
curs.execute(sarkı_sorgu)
conn.commit()

#------------------BAĞLANTI KES--------------------#
#--------------------------------------------------#

def baglantı_kes():
    conn.close()

#----------------ŞARKI EKLE------------------------#
#--------------------------------------------------#

def sarkı_ekle(isim,sanatcı,albüm,sirket,süre):
    curs.execute("INSERT INTO sarkılar VALUES (?,?,?,?,?)",(isim,sanatcı,albüm,sirket,süre))
    conn.commit()
    

#-------------------ŞARKI GÖSTER---------------------#
#----------------------------------------------------#

def sarkı_goster():
    goster_sorgu = "Select * From sarkılar"

    curs.execute(goster_sorgu)

    sarkılar = curs.fetchall()

    if (len(sarkılar) == 0):
        print("Şarkı Bulunmuyor...")

    else:
        for i in sarkılar:
            #sarkı = sarkılar(i[0],i[1],i[2],i[3],i[4])
            print(sarkılar)


#---------------ŞARKI SORGULA------------------------#
#----------------------------------------------------#

def sarkı_sorgula(isim):

        sorgu = "Select * From sarkılar where isim = ?"

        curs.execute(sorgu,(isim,))


        sarkılar = curs.fetchall()


        if (len(sarkılar) == 0):
            print("Böyle Bir Şarkı Bulunmuyor....")

        else:
            sarkı = sarkılar[0][0],sarkılar[0][1],sarkılar[0][2],sarkılar[0][3],sarkılar[0][4]
            print(sarkı)


#-----------------ŞARKI SİL---------------------------#
#-----------------------------------------------------#

def sarkı_sil(isim):
        sorgu = "Delete From sarkılar where isim = ?"

        curs.execute(sorgu,(isim,))


#--------------------SÜRE HESAPLA-----------------------#
#-------------------------------------------------------#

def süre_hesapla():
        sorgu = "Select SUM(süre) From sarkılar"

        curs.execute(sorgu)

        data = curs.fetchall()

        print(data[0][0])



#-----------------KULLANICI İŞLEMLERİ-------------------#
#-------------------------------------------------------#

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

while True:
    
    işlem = input("Yapmak İstediğiniz İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        baglantı_kes()
        break

    elif (işlem == "1"):
        sarkı_goster()

    elif (işlem == "2"):
        isim = input("Sorgulamak İstediğiniz Şarkıyı Giriniz:")
        sarkı_sorgula(isim)

    elif (işlem == "3"):
        isim_ekle = input("Lütfen Şarkı İsmi Giriniz:")
        sanatcı = input("Lütfen Sanatçı Giriniz:")
        albüm = input("Lütfen Albüm İsmi Giriniz:")
        sirket = input("Lütfen Prodüksiyon Şirketini Giriniz:")

        try:
            süre = int(input("Lütfen Süreyi Giriniz:"))
            
        except Exception:
            print("Lütfen Sayısal Bir Değer Giriniz...")

        
        sarkı_ekle(isim_ekle,sanatcı,albüm,sirket,süre)
        print("Şarkı Başarıyla Eklendi...")

    elif (işlem == "4"):
        isim_sil = input("Hangi Şarkıyı Silmek İstiyorsunuz?:")
        sarkı_sil(isim_sil)
        print("Şarkı Başarıyla Silindi....")

    elif (işlem == "5"):
        süre_hesapla()


    














