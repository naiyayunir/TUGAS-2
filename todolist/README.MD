# Aplikasi
- [LINK MENUJU APLIKASI](https://tugas2naiya.herokuapp.com/todolist/login/)

# Jawaban Tugas 4
### 1.Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

{% csrf_token %} berguna untuk melindungi data pengguna dari serangan. Apabila kita tidak menuliskan potongan kode tersebut pada elemen, maka django tidak akan mengizinkan akses ke route yang menggunakan form, selain itu data kita akan mudah diserang oleh pihak luar.

### 2.Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Kita bisa-bisa saja membuat elemen <form> secara manual. Caranya adalah dengan membuat input fields yang bisa berbentuk text biasa, password, checkbox, radio, dan lainnya.  Lalu membuat trigger untuk mengumpulkan POST request pada text controller yang isinya adalah value. Keuntungan dari menggunakan cara ini adalah developer dapat melakukan kustomisasi sesuai dengan keinginan dengan lebih fleksibel.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

1. Pertama tama user mengetikkan url yang menuju browser. Setelah itu server akan menentukan path mana yang akan menghandle permintaan user. 
2. Ketika sudah ditentukan, browser akan meneruskan html page ke browser yang dalam hal ini adalah HTML page form.
3. Kemudian user mengisi form yang ditampilkan pada browser.
4. Lalu browser akan meng-generate HTTP request, method, dan argumen ke URL destinasi yang bersesuain dengan HTML page form.
5. Server menerima HTTP request, lalu melakukan generate HTML page.
6. Kemudian browser akan menampilkan HTML layout kepada user.

### 4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Pertama kali saya membuat aplikasi baru, sesuai permintaan pada soal yang bernama “todolist”. Saya membuatnya dengan menjalankan perintah python manage.py startapp todolist.
2. Lalu saya menambahkan aplikasi todolist ke variabel INSTALLED_APPS ke settings.py project_django untuk mendaftarlan django-app yang telah dibuat.
3. Kemudian saya membuat models pada folder models.py.
4. Lalu menjalankan perintah makemigrations dan migrate.
5. Saya membuat fungsi-fungsi yang dapat mengimplementasikan form registrasi, login, dan logout pada fungsi views.py.
6. Pada folder templates, saya menambahkan file-file yang dibutuhkan untuk ditampilkan kepada user.
7. Kemudian saya melakukan routing pada file urls.py dengan cara membuat variabel nama aplikasi dan membuat pada list untuk mewadahi url pattern.
8. Tidak lupa saya juga menambahkan path ke urlpatterns project_django pada folder settings.py agar aplikasinya terdaftar.
9. Lalu saya melakukan add, commit, push dan sudah otomatis ter-deploy.
10. Pada website yang sudah saya buat, saya membuat dua akan pengguna serta tiga data contoh dengan menggunakan model task.

# Jawaban Tugas 5

### 1.Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1. Internal, penulisan kode pada inline style terletak pada tag <style>. Penulisan kode dengan internal style hanya dapat dilakukan pada satu halaman website saja, dan tidak dapat digunakan pada halaman lain.
Kelebihan : tidak perlu mengupload beberapa file, karena css dan html terletak pada file yang sama.
Kekurangan : css tidak dapat digunakan bersamaan dengan halaman html yang lain. Selain dapat memperlambat performa website.
2. Inline, penulisan kode yang ditulis langsung pada atribut elemen html. Kode ini ditulis pada setiap kode html yang mempunyai atribut style.
Kelebihan : sangat membantu apabila kita ingin menguji coba atau sekedar ingin melihat perubahan. Lalu dapat memperbaiki kode dengan cepat, dan juga proses load website akan lebih cepat.
Kekurangan : Lebih sulit dalam mengatur website karena hanya dapat mengatur satu elemen.
3. External, penulisan kode yang ditulis pada file eksternal yang terpisah dengan file htmlnya. file CSS ditulis dengan ekstensi .css. 
kelebihan : struktur file html akan lebih rapi, loading website akan jadi lebih cepat, dapat digunakan di beberapa halaman web sekaligus.
kekurangan : apabila koneksi internet lambat, halaman akan berantakan ketika file css gagal dipanggil oleh file html.

### 2.Jelaskan tag HTML5 yang kamu ketahui.

!DOCTYPE      : Tag untuk menentukan tipe dokumen
html	      :Tag untuk membuat sebuah dokumen HTML
title         :Tag untuk membuat judul dari sebuah halaman
body	      :Tag untuk membuat tubuh dari sebuah halaman
h1 to h6      :Tag untuk membuat heading
form          :Tag untuk membuat sebuah form HTML untuk input pengguna
input	      :Tag untuk membuat sebuah kontrol input
textarea	  :Tag untuk membuat sebuah kontrol input multibaris (text area)
button   	  :Tag untuk membuat sebuah tombol yang dapat diklik
img	          :Tag untuk membuat gambar
link	      :Tag untuk membuat hubungan antara dokumen dan sumber daya eksternal 
table	      :Tag untuk membuat tabel
style	      :Tag untuk membuat informasi style untuk dokumen
head          :Tag untuk membuat informasi tentang dokumen
meta	      :Tag untuk membuat metadata tentang dokumen HTML

### 3.Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Selektor Tag, memilih elemen berdasarkan nama tag.
2. Selektor Class, selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class ditandai dengan tanda titik di depannya.
3. Selektor ID, hampir sama dengan selector class hanya saja id bersifat unik dan hanya dapat digunakan pada satu elemen saja.
4. Selektor Atribut, hampir sama dengan selektor tag, hanya saha selektor ini memilih elemen berdasarkan atributnya.
5. Selektor Universal, selektor yang digunakan untuk menyeleksi semua elemen pada jangkauan (scope) tertentu.
6. Selektor Pseudo, selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.

### 4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pertama saya menyertakan kode untuk Include Bootstrap’s CSS and JS ke file html yang telah saya buat di tugas sebelumnya.
2. Selanjutnya saya mulai menghias halaman per halamannnya. Pada tugas ini kebanyakan saya menggunakan inline style. Saya mengubah tulisan menjadi heading, mengganti jenis font, serta menambahkan navigation bar agar halaman websitenya terlihat menarik.
3. Selanjutnya pada halaman todolist, saya membuat card per tasknya. Kemudian saya menghias dengan memberi warna pada card tersebut. Tidak lupa saya menyesuaikan tata letak dan memberikan keterangan mengenaik card tersebut.
4. Untuk tombol-tombol yang ada, saya juga menghiasnya menjadi lebih berwarna.
5. Selanjutnya saya melakukan git add,commit,push seperti biasa.
