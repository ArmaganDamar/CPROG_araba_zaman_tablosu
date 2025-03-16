# Kullanıcı işlemleri: Yeni kullanıcı kaydetme ve giriş yapma komutlarını içerir.

# Moduller:
import sqlite3
from tkinter import messagebox
from database import baglanti_olustur


### Fonksiyonlar:

# Yeni kullanıcı kayıdı için giriş verilerini alır ve veritabanına girer.
def kullanici_kayit(entry_yeni_kullanici_adi, entry_yeni_sifre, var_kullanici_tipi, yeni_kullanici_penceresi):
    kullanici_adi = entry_yeni_kullanici_adi.get()
    sifre = entry_yeni_sifre.get()
    kullanici_tipi = var_kullanici_tipi.get()
    
    conn = baglanti_olustur()
    c = conn.cursor()

    if kullanici_adi and sifre: # Kullanıcı kaydında var olan bir isim yada eksik doldurursanız hata mesajı verir.
        try:
            c.execute("INSERT INTO kullanicilar (kullanici_adi, sifre, kullanici_tipi) VALUES (?, ?, ?)",
                      (kullanici_adi, sifre, kullanici_tipi))
            conn.commit()
            messagebox.showinfo("Başarılı", "Kullanıcı kaydı başarılı!")
            yeni_kullanici_penceresi.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Hata", "Bu kullanıcı adı zaten var.")
    else:
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")

    conn.close()


# Varolan kullanıcı bilgilerini alır ve kullanıcı tipine göre sizi gereken panele yönlendirir.
def giris_yap(entry_kullanici_adi, entry_sifre, root, admin_panel, arabalari_gor):
    kullanici_adi = entry_kullanici_adi.get()
    sifre = entry_sifre.get()
    
    conn = baglanti_olustur()
    c = conn.cursor()
    
    c.execute("SELECT kullanici_tipi FROM kullanicilar WHERE kullanici_adi=? AND sifre=?", (kullanici_adi, sifre))
    result = c.fetchone()
    
    if result: # Kullanıcı tipine göre belirli kullanıcı panellerine yönlendirir.
        kullanici_tipi = result[0]
        if kullanici_tipi == "admin":
            messagebox.showinfo("Giriş Başarılı", "Admin olarak giriş yaptınız!")
            admin_panel(root)
        else:
            messagebox.showinfo("Giriş Başarılı", "Standart kullanıcı olarak giriş yaptınız!")
            arabalari_gor(root)
    else:
        messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre.")
    
    conn.close()
