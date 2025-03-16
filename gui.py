# GUI: Arayüz komutları içindir.

# Moduller:
import customtkinter as ctk
from kullanici_islemleri import kullanici_kayit
from araba_islemleri import arabalari_gor, araba_ekle

### Fonksiyonlar:

# Yeni kullanıcı oluşturma penceresi.
# Yeni kullanıcı verilerini alır ve veritabanına kaydeder.
def yeni_kullanici_olustur(root):
    global yeni_kullanici_penceresi, entry_yeni_kullanici_adi, entry_yeni_sifre, var_kullanici_tipi
    
    yeni_kullanici_penceresi = ctk.CTkToplevel(root)
    yeni_kullanici_penceresi.title("Yeni Kullanıcı:")
    yeni_kullanici_penceresi.geometry("250x250")
    
    ctk.CTkLabel(yeni_kullanici_penceresi, text="Kullanıcı Adı:").pack(pady=5) 
    entry_yeni_kullanici_adi = ctk.CTkEntry(yeni_kullanici_penceresi)
    entry_yeni_kullanici_adi.pack(pady=5)
    
    ctk.CTkLabel(yeni_kullanici_penceresi, text="Şifre:").pack(pady=5)
    entry_yeni_sifre = ctk.CTkEntry(yeni_kullanici_penceresi, show="*")
    entry_yeni_sifre.pack(pady=5)
   
    var_kullanici_tipi = ctk.StringVar(value="standart")
    
    ctk.CTkButton(yeni_kullanici_penceresi, text="Kaydet", command=lambda: kullanici_kayit(entry_yeni_kullanici_adi, entry_yeni_sifre, var_kullanici_tipi, yeni_kullanici_penceresi)).pack(pady=20)


# Admin paneli.
# Admin işlemlerinin yapılmasını sağlar. Girilen verileri veritabanına kaydeder.
def admin_panel(root):
    admin_paneli = ctk.CTkToplevel(root)
    admin_paneli.title("[MyRaceTracker] Admin Paneli")
    admin_paneli.geometry("250x530")

    ctk.CTkLabel(admin_paneli, text="Admin Paneli", font=('Ariel', 12)).pack(padx=10, pady=10)

    ctk.CTkLabel(admin_paneli, text="Araba Numarası:").pack(pady=5)
    entry_araba_numarasi = ctk.CTkEntry(admin_paneli)
    entry_araba_numarasi.pack(pady=5)
    
    ctk.CTkLabel(admin_paneli, text="Araba Adı:").pack(pady=5)
    entry_araba_ismi = ctk.CTkEntry(admin_paneli)
    entry_araba_ismi.pack(pady=5)
    
    ctk.CTkLabel(admin_paneli, text="Takım Adı:").pack(pady=5)
    entry_takim_adi = ctk.CTkEntry(admin_paneli)
    entry_takim_adi.pack(pady=5)
    
    ctk.CTkLabel(admin_paneli, text="Tur Zamanı:").pack(pady=5)
    entry_tur_zamani = ctk.CTkEntry(admin_paneli)
    entry_tur_zamani.pack(pady=5)
    
    ctk.CTkButton(admin_paneli, text="Araba Ekle", command=lambda: araba_ekle(entry_araba_numarasi, entry_araba_ismi, entry_takim_adi, entry_tur_zamani)).pack(pady=20)
    ctk.CTkButton(admin_paneli, text="Arabaları Görüntüle", command=lambda: arabalari_gor(root)).pack(pady=5)