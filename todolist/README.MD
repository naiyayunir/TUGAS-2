# Aplikasi
- LINK MENUJU APLIKASI [klik sini](https://tugas2naiya.herokuapp.com/catalog/)

# Jawaban
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
