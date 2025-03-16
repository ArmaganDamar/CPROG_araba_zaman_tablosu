# Araba işlemleri: Araba girişi, CSV çıktısı ve araba tablosunun komutları yer alır.

# Moduller:
import sqlite3
from tkinter import messagebox, filedialog
import csv
from database import baglanti_olustur


### Fonksiyonlar:

# Arabaları eklemeye yarar.
# Girilen araba numarası vs. yi veritabanıa gönderir. Hatalı veya eksik giriş yaparsa hata mesajı verir.
def araba_ekle(entry_araba_numarasi, entry_araba_ismi, entry_takim_adi, entry_tur_zamani):
    araba_numarasi = entry_araba_numarasi.get()
    araba_ismi = entry_araba_ismi.get()
    takim_adi = entry_takim_adi.get()
    tur_zamani = entry_tur_zamani.get()
    
    conn = baglanti_olustur()
    c = conn.cursor()

    # Girilen veride sorun yoksa araba bilgilerini veritabanına ekler.
    # Hata varsa hata mesajı verir.
    if araba_numarasi and araba_ismi and takim_adi and tur_zamani: 
        try:
            c.execute("INSERT INTO arabalar (araba_numarasi, araba_ismi, takim_adi, tur_zamani) VALUES (?, ?, ?, ?)", 
                      (araba_numarasi, araba_ismi, takim_adi, tur_zamani))
            conn.commit()
            messagebox.showinfo("Başarılı", "Araba bilgisi eklendi!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Hata", "Bu araba numarası zaten var.")
    else:
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")
    
    conn.close()


# Arabalar tablosunu CSV çıktısı almaya yarar.
def arabalar_csv_cikti():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:
        try:
            conn = baglanti_olustur()
            c = conn.cursor()
            c.execute("SELECT * FROM arabalar")
            rows = c.fetchall()
            conn.close()

            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["araba_numarasi", "araba_ismi", "takim_adi", "tur_zamani"])
                writer.writerows(rows)
            messagebox.showinfo("Başarılı", "Arabalar CSV dosyasına kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# Araba tablosudur.
# Veritabanında bulunan arabaları alır ve Treeview şeklinde liste yapar.
def arabalari_gor(root):
    from tkinter import ttk
    import customtkinter as ctk

    conn = baglanti_olustur()
    c = conn.cursor()
    arabalar_penceresi = ctk.CTkToplevel(root)
    arabalar_penceresi.title("[MyRaceTracker] Arabaları Görüntüle")

    tree = ttk.Treeview(arabalar_penceresi, columns=("araba_numarasi", "araba_ismi", "takim_adi", "tur_zamani"), show='headings')
    tree.heading("araba_numarasi", text="Araba Numarası")
    tree.heading("araba_ismi", text="Araba Adı")
    tree.heading("takim_adi", text="Takım Adı")
    tree.heading("tur_zamani", text="Tur Zamanı")
    
    c.execute("SELECT * FROM arabalar")
    rows = c.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", ctk.END, values=row)
    
    tree.pack(expand=True, fill='both')
    ctk.CTkButton(arabalar_penceresi, text="Arabaları CSV'ye Aktar", command=arabalar_csv_cikti).pack(pady=10)
