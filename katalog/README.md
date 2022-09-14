# Aplikasi
- Ini jwbannya [klik sini](https://tugas2naiya.herokuapp.com/catalog/)

# Jawaban
### 1.
![Bagan](/Bagan.png) 
-Ketika user memunculkan permintaan, maka permintaan tersebut akan menuju ke internet sebagai permulaannya.
-Kemudian permintaan akan menuju web server environment untuk pemrosesan di aplikasi Django.
-Di aplikasi Django  pemorosesan pertama akan menuju file urls.py untuk menghubungkan permintaan user ke views.py.
-Pada views.py terdapat komponen - komponen yang nantinya dihubungkan pada html. Kemudian views.py akan berkoordinasi dengan model.py untuk meminta resource yang dibutuhkan.
- Views.py nantinya akan memanggil query oleh database melalui models apabila ada permintaan yang melibatkan database.
- Apabila semua permintaan user terpenuhi, maka komponen - komponennya akan diteruskan oleh views.py ke dalam html.
- Kemudian html akan mengembalikan komponen tersebut ke internet melalui aplikasi Django yang kemudian diteruskan ke internet berupa web page.
- Langkah terakhir web page tersebut akan di teruskan kepada pengguna.

### 2. 
Kita menggunakan virtual environment agar lingkungan virtual python tidak dapat diakses dari luar. Hal ini dikarenakan pada program python yang berjalan pada virtual environment memiliki modul-modul yang tentu saja pihak luar tidak dapat mengaksesnya. Modul - modul ini juga berguna agar program python yang kita buat kebal atas pembaruan Django. Sehingga meskipun Django melakukan pembaruan versi, program kita dapat berjalan dengan baik.
Kita bisa-bisa saja membuat web berbasis Django tanpa virtual environment, tetapi hal-hal yang kurang baik bisa saja terjadi. Pertama, pihak luar dapat dengan mudah mengakses program kita. Kedua, program yang telah kita buat tidak dapat beradaptasi dengan pembaruan-pembaruan versi Django. Misalnya suatu program dapat berjalan dengan baik pada Django versi 3.4. Namun ketika Django melakukan pembaruan versi ke 3.5 program kita jadi bermasalah karena tidak menggunakan modul-modul pada virtual environment.

### 3. 

Langkah pertama yang saya lakukan adalah menggunakan template yang tersedia lalu meng-clone repositorynya ke perangkat lokal. Setelah templatenya berhasil digunakan, saya mulai mengimplementasikan fungsi views.
Hal selanjutnya yang saya lakukan adalah membuat sebuah fungsi di folder templates yang mereturn parameter serta file katalog.html pada file views.py . 
Lalu saya menghubungkan halaman html dengan browser dengan melakukan routing terhadap fungsi views tadi. Hal ini saya lakukan dengan cara menambahkan path yang salah satu isinya adalah nama fungsi yang telah saya buat pada berkas views tadi. Tak lupa saya juga melakukan routing pada folder project janggo bagian urls.py dengan menambahkan path juga.
Selanjutnya saya memetakan data ke dalam html. Pada saat ini saya menghubungkan models dengan views dan template. Pertama saya mengimport model yang telah dibuat ke dalam views,py. Lalu saya melengkapi fungsi yang telah saya buat di awal pada berkas views.py. Saya melengkapinya untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Tidak lupa pula untuk menyesuaikan kembalian dari fungsi tersebut. 
Lalu untuk tahap mapping, saya mengubah file katalog.html dengan nama dan npm saya terlebih dahulu. Lalu saya melakukan iterasi pada variabel list_item untuk menampilkan daftar item ke dalam tabel. Iterasi harus dilakukan karena list_item berisikan objek sehingga tidak bisa dipanggil secara langsung. Setelah menjalankan halaman web pada perangkat lokal, maka muncullah item, harga stock,rating, dan yang lainnya pada layar kita. Hal ini menandakan kita telah berhasil membuat aplikasi sederhana.
Selanjutnya saya melakukan persiapan deploy seperti menambahkan beberapa file dan melakukan rangkaian git add-commit-push. Setelah itu, saya melakukan deploy untuk menghubungkan aplikasi Django ke internet. Saya menggunakan Heroku sebagai host. Pada saat melakukan deploy, langkah pertama yang saya lakukan adalah menyalin API key lalu menghubungkannya ke GitHub. lalu tahap terakhir saya menambahkan variabel dan menyimpannya. Kemudian saya menjalankan kembali komponen yang gagal hingga berhasil.

