# link heroku
https://tugas2naiya.herokuapp.com/mywatchlist/json/1
https://tugas2naiya.herokuapp.com/mywatchlist/xml/
https://tugas2naiya.herokuapp.com/mywatchlist/html/

# Screenshoot menggunakan postman


# Jawaban
### 1.
1.XML atau Extensible Markup Language membuat pertukaran data menjadi lebih terstruktur dan membantu dalam konfigurasi dinamis dan pembuatan variabel tetapi kurang efisien. File xml diakhiri dengan ekstensi .xml. Pengguna dapat menerapkan xml untuk menambahkan catatan.
2.Json atau JavaScript Object Notation memuat data dalam format key dan value sehingga lebih mudah untuk dipahami. File json diakhiri dengan ekstensi .json. Penerapan json dengan cara menguraikan data dan mengirimkannya melalui internet.
3.HTML atau Hypertext Markup Language merupakan bahasa standar pemrograman yang digunakan untuk membuat halaman website. HTML disusun berdasar kode dan simbol tertentu, yang dimasukkan dalam sebuah file atau dokumen.

### 2. 
Dalam pengimplementasian sebuah platform, kita pastinya butuh melakukan pengiriman data antara stack satu ke stack lain. Data tersebut bermacam ragam, beberapa bentuknya bisa seperti HTML, XML, JSON. Sehingga data delivery digunakan untuk mengirimkan data-data tersebut.

### 3.
Langkah pertama yang saya lakukan dalam membuat aplikasi ini adalah dengan memasukkan perintah startapp. Setelah itu saya menambahkan nama aplikasinya pada INSTALLED_APPS di folder settings.py. Lalu saya menambahkan models di file models.py. Tidak lupa saya melakukan migrasi dan menerapkan skema model yang dibuat ke database Django lokal. Kemudian saya meletakkan datanya pada file dengan ekstensi .json. Langkah terakhir pada bagian ini, saya memasukkan data tersebut ke database Django lokal.

Bagian kedua, saya melakukan routing pada fungsi views yang dapat melakukan render ke halaman HTML. Hal pertama yang saya lakukan adalah membuat sebuah fungsi ke file views.py.  Lalu saya membuat file html yang terletak pada folder baru yang bernama templates. File tersebut berisi data-data yang akan ditampilkan di website. Lalu pada file urls.py saya melakukan routing fungsi views. Kemudian saya mencoba menjalankan programnya dan membuka localhost sehingga muncullah website tanpa data.

Untuk menampilkan datanya saya menghubungkan models dengan views dan template. Pertama saya mengimport modelnya terlebih dahulu. Kemudian saya menambahkan fungsi show_mywatchlist dengan variabel yang memuat objek dan tidak lupa menambahkan returnnya. Selanjutnya saya berpindah ke file html untuk memunculkan datanya dengan melakukan iterasi. Setelah itu saya mencoba menjalankan programnya kemudian muncullah tabel.

Bagian selanjutnya adalah saya mengimplementasikan bagaimana pengembalian data dengan bentuk xml dan json. Pertama saya membuat fungsi baru pada file views.py kemudia saya juga mengimport HttpResponse dan serializers. Di Dalam fungsi tersebut terdapat variabel yang mengandung objek datanya. Lalu pada file urls.py saya menambahkan path url. Setelah dijalankan muncullah kembalian berupa file xml/json sesuai dengan yang kita buat tadi. 

Setelah semuanya selesai, saya melakukan deploy ke heroku.



