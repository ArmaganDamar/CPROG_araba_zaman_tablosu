# Main: Ana penceredir. Programın kalbidir.

# Moduller:
import customtkinter as ctk #Arayüz içindir.
from kullanici_islemleri import giris_yap #"kullanici_islemleri" modulünden "giris_yap" fonksiyonunu çağırır.
from gui import yeni_kullanici_olustur, admin_panel #"gui" dan gerkli modulleri çağırır.
from database import baglanti_olustur, table_olustur, baglantiyi_kapat # "database"den "    "    ".
from araba_islemleri import arabalari_gor 

### Fonksiyonlar:

# Ana penceredir.
# Programın ana penceresidir kapanırsa herşey kapanır. Bu pencereden kullanıcı girişi yapılabilir veya yeni bir kullanıcı oluşturula bilir.
def main():
    conn = baglanti_olustur() # Bağlantı oluşturur.
    table_olustur(conn) # Table yoksa table oluşturur.
    baglantiyi_kapat(conn) # Bağlantıyı kapatır.
    
    root = ctk.CTk()
    root.title("[MyRaceTracker] Kullanıcı Girişi") # Pencere ismini belirler.
    root.geometry("400x400") # Sayfa boyutunu belirler.
    
    ctk.CTkLabel(root, text="MyRaceTracker", font=('Ariel', 20)).pack(padx=0, pady=15)
    ctk.CTkLabel(root, text="Kullanıcı Adı:").pack(pady=5) # Kullanıcı adı girişi ister. Yazı kutucuğudur.
    entry_kullanici_adi = ctk.CTkEntry(root)
    entry_kullanici_adi.pack(pady=5)
    
    ctk.CTkLabel(root, text="Şifre:").pack(pady=5) # Kullanıcı şifresi ister. Yazı kutucuğudur.
    entry_sifre = ctk.CTkEntry(root, show="*")
    entry_sifre.pack(pady=5)
    
    ctk.CTkButton(root, text="Giriş Yap", command=lambda: giris_yap(entry_kullanici_adi, entry_sifre, root, lambda r=root: admin_panel(r), lambda r=root: arabalari_gor(r))).pack(pady=20)
    ctk.CTkButton(root, text="Yeni Kullanıcı Oluştur", command=lambda: yeni_kullanici_olustur(root)).pack(pady=5)
    
    ctk.CTkLabel(root, text="by Armağan Damar", font=('Ariel', 10)).pack(padx=10, pady=18)
    
    root.mainloop() # Tkinter loopu.

if __name__ == "__main__":
    main()
