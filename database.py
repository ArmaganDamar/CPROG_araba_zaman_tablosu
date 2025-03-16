# Database: Adı üstünde database komutlarını içerir.

# Moduller:
import sqlite3

### Fonksiyonlar:

#Veritabanıyla bağlantı kurar.
def baglanti_olustur():
    conn = sqlite3.connect('kullanicilar.db')
    return conn


# Veritabanı yoksa oluşturur.
def table_olustur(conn):
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS kullanicilar 
        (
            kullanici_adi TEXT PRIMARY KEY,
            sifre TEXT NOT NULL,
            kullanici_tipi TEXT NOT NULL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS arabalar 
        (
            araba_numarasi INTEGER PRIMARY KEY,
            araba_ismi TEXT NOT NULL, 
            takim_adi TEXT NOT NULL,
            tur_zamani REAL NOT NULL
        )
    ''')
    
    conn.commit()


# Veritabanı bağlantısını kapatır.
def baglantiyi_kapat(conn):
    conn.close()
