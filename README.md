(Çoklu programla dersi için pyhton üzerinden yaptığım basit database projesi.)

## MyRaceTracker Nasıl Kullanılır? ##

- Kullanıcı Girişi: 
 Programı açınca karşınıza 2 tane kutucuk olacak. <br>
 Varolan bir hesabınız varsa; <br>
 kullanıcı adı ve şifrenizi kutucuklara girerek uygulamaya geçebilirsiniz. <br>
 Hesabınız yoksa; <br>
 Yeni kullanıcı oluştur butonuna basarak yeni bir kullanıcı oluşturabilirsiniz. <br>
 

- Yeni kullanıcı oluşturma paneli: 
 Paneldeki Kullanıc Adı ve Şifre kısmını dolurup kaydettikten sonra 'Standart' kullanıcı olarak <br>
 kayıt olursunuz.


- Admin Paneli: 
 Eğer admin kullanıcısına erişiminiz varsa tüm işlemlerinizi burdan gerçekleştireceksiniz. <br>
 Araba numarası, Araba adı, Takım adı ve Tur zamanı girdikten sonra 'Araba ekle' butonuna basarak
 kayıt işlemi gerçekleştirebilirsiniz. <br>
 Arabaları Görüntüle butonu ile araba listesini görüntülüye bilirsiniz.











## Program Nasıl Çalışır?

!!! Çalışması için gerekenler: Sqlite,  Sqlite3 Editor ve CustomTkinter. !!! <br>
(CustomTkinterı indirmek için cmd ye "pip install customtkinter" komudunu girin.)

- main.py: 
 Kodun kalibidir. Bu pencere kapanınca programda kapanır. Modülleri ve giriş işlemlerini barındırır.

- kullanici_islemleri.py: 
 Yeni kullanıcı kaydı oluşturmak veya var olan kullanıcıların kaydını oluşturur.

- gui.py: 
 Arayüz dosyasıdır. Arayüz kodlarını içerir.

- araba_islemleri.py: 
 Araba eklemek, arabaları CSV dosyasına çıkarmak ve arabaları görüntülemek için kullanılır.

- database.py: 
 Programın veritabanıdır. Bu dosya olmadan araba kaydı veya kullanıcı kaydı gibi işlemler gerçekleşmez.


- Modüller ve veritabanı bağlantısı: 
 Program ilk olarak modülleri cağırır. Gerekli olanlanları "as" komutuyla kısaltır. <br>
 Sonra veritabanı bağlantısı kurulur ve eğer gereken tablolar yoksa onları oluşturur.









## Fonksiyonlar:

- "kullanici_kayit" ve "yeni_kullanici_olustur" birbirine bağlıdır. <br>
 yeni_kullanici_olustur: Arayüz penceresidir giriş kutucuklarına girilenleri Kullanıcı_kayıt fonksiyonuna aktarır. <br>
 kullanici_kayit: Girilen kullanıcı verilerini alır aynısı varsa yada gerekli alanlar doldurulmamşsa hata mesajı verir. <br>
Hatalı bir giriş yapılmadıysa kullanıcı kaydını gerçekleştirir.

- "arabalari_gor" bir Treeview wigetidir. Tüm arbaları ekrana listeler.

- "araba_ekle" ve "admin_panel" birbirine bağlıdır. <br>
araba_ekle: Admin paneline girilen verileri alır gerekli alanlar doldurulmamş veya aynı araba numarası girilmişse hata mesajı verir. <br>
admin_panel: Girilen araba verilerini "Entry" komutu ile araba "araba_ekle" ye aktarır.

- "giris_yap" ve Ana pencere birbirine bağlıdır. <br>
 giris_yap: Kullanıcı verileri girildikten sorna veritabanından uyuşuyormu diye kontrol eder. <br>
 Uyuşursa kullanıcı tipine göre belirli bir sayfaya yönlendirir.

- "arabalar_csv_cikti" araba listesini CSV dosyası olarak export etmeyi sağlar.

- "baglanti_olustur": veritabanına bağlantıyı oluşturur.

- "table_olustur": table yoksa table oluşturur.

- "baglantiyi_kapat": veritabanı bağlantısını kapatır.
