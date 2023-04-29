# DOKUMENTASI-PROJECT-AKHIR-ASD-KELOMPOK-5-

                                                                ########## MEMANAJEMEN KONTAK ##########
                                                                
# DESKRIPSI PROGRAM
Program kami adalah sebuah program manajemen kontak yang dibangun dengan menggunakan bahasa pemrograman Python dan beberapa modul Python, yaitu os, time, pwinput, prettytable, dan mysql.connector. 

Program ini memiliki beberapa fitur utama, yaitu registrasi dan login pengguna, menambahkan kontak baru ke dalam daftar kontak, menampilkan daftar kontak, mencari kontak berdasarkan nama atau nomor telepon, mengedit kontak, dan menghapus kontak dari daftar.
Program ini menggunakan basis data MySQL untuk menyimpan daftar kontak dan data pengguna. Pengguna dapat melakukan registrasi terlebih dahulu dengan memasukkan email, password, dan nomor telepon mereka. Setelah itu, pengguna dapat melakukan login dengan memasukkan email dan password yang telah terdaftar.

Setelah login berhasil, pengguna dapat memilih fitur yang ingin digunakan, yaitu menambahkan kontak baru, menampilkan daftar kontak, mencari kontak, mengedit kontak, atau menghapus kontak. Untuk menambahkan kontak baru, pengguna diminta untuk memasukkan nama dan nomor telepon kontak, dan data kontak tersebut akan disimpan ke dalam basis data.

Untuk menampilkan daftar kontak, program akan mengambil data dari basis data dan menampilkannya dalam sebuah tabel yang menggunakan modul prettytable. Pengguna juga dapat mencari kontak berdasarkan nama atau nomor telepon dengan memasukkan kata kunci pencarian, dan program akan menampilkan kontak yang cocok dengan kriteria pencarian tersebut.

Pengguna juga dapat mengedit atau menghapus kontak dari daftar. Untuk mengedit kontak, pengguna diminta untuk memilih kontak yang ingin diubah dan memasukkan nama dan nomor telepon baru. Setelah itu, data kontak yang telah diubah akan disimpan ke dalam basis data. Sedangkan untuk menghapus kontak, pengguna hanya perlu memilih kontak yang ingin dihapus, dan data kontak tersebut akan dihapus dari basis data.

Program ini juga menyimpan riwayat perubahan kontak yang dilakukan oleh pengguna, yaitu penambahan, pengeditan, dan penghapusan kontak. Riwayat perubahan ini akan ditampilkan saat program dijalankan. Dapat disimpulkan bahwa, program ini dapat membantu pengguna dalam mengelola daftar kontak mereka dengan mudah dan efisien.

# STRUKTUR PROJECT
Program kami merupakan sebuah aplikasi untuk mengelola daftar kontak. Aplikasi ini menggunakan MySQL database untuk menyimpan informasi tentang pengguna dan kontak. Struktur project kami dimulai dari modul atau library python yang dilanjutkan dengan beberapa fungsi. Berikut beberapa library Python yang digunakan dalam program ini antara lain:

Os              : digunakan untuk melakukan operasi sistem, seperti membersihkan layar konsol.
Time            : digunakan untuk menambahkan jeda waktu dalam program.
Pwinput         : digunakan untuk memasukkan password pengguna secara aman.
Prettytable     : digunakan untuk menampilkan data dalam bentuk tabel.
Datetime        : digunakan untuk mengambil waktu saat ini.
mysql.connector : digunakan untuk menghubungkan ke MySQL database.

Setelah selesai menerapkan atau mengaplikasikan library python yang kami butuhkan, berikut beberapa fungsi yang menjadi pelengkap struktur project kami:

database()  : digunakan untuk membuat koneksi ke database MySQL.
register()  : fungsi untuk mendaftarkan pengguna baru. Fungsi ini akan meminta pengguna untuk memasukkan email, password, dan nomor telepon, kemudian akan memeriksa apakah email sudah terdaftar di dalam tabel user di database. Jika email sudah terdaftar, fungsi akan meminta pengguna untuk memasukkan email yang berbeda. Jika email belum terdaftar, fungsi akan menambahkan pengguna baru ke dalam tabel user di database.
login()     : fungsi untuk melakukan login ke aplikasi. Fungsi ini akan meminta pengguna untuk memasukkan email dan password, kemudian akan memeriksa apakah email dan password yang dimasukkan sudah benar atau belum. Jika email dan password sudah benar, fungsi akan menampilkan pesan "Login berhasil!". Jika email atau password salah, fungsi akan meminta pengguna untuk memasukkan email dan password yang benar.
Contacts    :sebuah kelas Python yang digunakan untuk merepresentasikan kontak. Kelas ini memiliki dua atribut, yaitu nama dan no_hp.
ContactList :sebuah kelas Python yang digunakan untuk merepresentasikan daftar kontak. Kelas ini memiliki tiga atribut, yaitu head, tail, dan history. head dan tail adalah node pertama dan terakhir dalam daftar kontak, sedangkan history digunakan untuk menyimpan riwayat aksi pengguna. Kelas ini memiliki beberapa metode, seperti add_database(): untuk menambahkan kontak ke database dan get_data()  :untuk mengambil kontak dari database, dan display() untuk menampilkan kontak dalam bentuk tabel.

Selain itu, program ini juga menggunakan loop while dan kondisional if-else untuk memeriksa apakah suatu input sudah benar atau belum, serta menggunakan try-except untuk menangani kesalahan saat menghubungkan ke database MySQL.

# FUNGSI DAN FUNGSIONALITAS PROGRAM
Program ini merupakan aplikasi manajemen kontak yang digunakan untuk menyimpan dan mengelola kontak dalam sebuah daftar. Program ini terdiri dari beberapa fungsi dan fungsionalitas, yaitu:

1.	Import library dan modules
•os: untuk mengakses fungsi-fungsi sistem operasi
•time: untuk mengakses fungsi-fungsi waktu
•pwinput: untuk mengakses fungsi-fungsi input password
•PrettyTable: untuk mengakses fungsi-fungsi membuat tabel dengan tampilan yang lebih menarik
•datetime: untuk mengakses fungsi-fungsi tanggal dan waktu
• mysql.connector: untuk mengakses fungsi-fungsi database MySQL.

2.	Fungsi database(): digunakan untuk menghubungkan program ke database MySQL yang telah dibuat.
3.	Fungsi register(): digunakan untuk melakukan registrasi user dan menambahkan data user baru ke dalam tabel user di database. Pada fungsi ini, user diminta memasukkan email, password, dan nomor telepon. Kemudian, data input tersebut dicek apakah kosong atau tidak, apakah nomor telepon hanya terdiri dari angka, serta dicek apakah email telah terdaftar atau belum di dalam tabel user. Jika input tidak valid atau email telah terdaftar, maka user diminta untuk memasukkan input yang benar atau kembali ke menu utama. Jika input valid dan email belum terdaftar, maka data user baru akan ditambahkan ke dalam tabel user di database.
4.	Fungsi login(): digunakan untuk melakukan login user. User diminta memasukkan email dan password. Email dan password tersebut kemudian akan dicocokkan dengan data pada tabel user di database. Jika data cocok, maka user berhasil login dan dapat mengakses menu utama. Jika data tidak cocok, maka user diminta memasukkan email dan password kembali.
5.	Class Contacts: digunakan untuk mendefinisikan objek kontak yang terdiri dari nama dan nomor telepon.
6.	Class ContactList: digunakan untuk mendefinisikan objek daftar kontak yang terdiri dari beberapa metode, yaitu:
    • Method init: Method ini digunakan untuk menginisialisasi objek ContactList dengan membuat daftar kosong yang akan digunakan untuk menyimpan kontak.
    • Method add_contact: Method ini digunakan untuk menambahkan kontak baru ke dalam daftar kontak. Method ini menerima parameter nama, nomor telepon, dan email dari kontak yang ingin ditambahkan. Method ini akan membuat objek Contact baru dan menambahkannya ke dalam daftar kontak.
    • Method delete_contact: Method ini digunakan untuk menghapus kontak dari daftar kontak berdasarkan nama kontak. Method ini menerima parameter nama kontak yang ingin dihapus. Method ini akan mencari kontak dengan nama yang sesuai di dalam daftar kontak, dan jika ditemukan, maka kontak tersebut akan dihapus dari daftar kontak.
    • Metode refreshList() pada class ContactList bertujuan untuk mengambil daftar kontak dari database dan mengupdate list kontak pada program agar sesuai dengan kontak yang terdapat pada database.
    • Method display_history: Method ini digunakan untuk menampilkan history terbaru.
    • Method search_contact: Method ini digunakan untuk mencari kontak dalam daftar kontak berdasarkan nama. Method ini menerima parameter nama kontak yang ingin dicari. Method ini akan mencari kontak dengan nama yang sesuai di dalam daftar kontak, dan jika ditemukan, maka akan mengembalikan informasi kontak tersebut.
    • Method update_contact: Method ini digunakan untuk memperbarui informasi kontak dalam daftar kontak berdasarkan nama kontak. Method ini menerima parameter nama kontak yang ingin diperbarui, serta parameter baru yang ingin diubah dari kontak tersebut (misalnya nomor telepon atau email). Method ini akan mencari kontak dengan nama yang sesuai di dalam daftar kontak, dan jika ditemukan, maka akan memperbarui informasi kontak tersebut dengan parameter baru yang diberikan.

# CARA PENGGUNAAN PROGRAM
Secara umum, program kami menggunakan dua jenis file yaitu file python dan file database sql. Sebelum menjalankan program, pastikan anda telah meng-ekspor file database sql terlebih dahulu di php my admin dan jangan lupa untuk mendownlod mysql conector pada terminal.

Untuk mengakses fungsi atau fitur yang ada pada program kami, user harus login terlebih dahulu menggunakan email dan password yang telah terdaftar pada database. Setelah berhasil login, user dapat memilih menu yang diinginkan melalui tampilan menu utama yang tersedia pada program. Dan apabila belum terdaftar atau belum memiliki akun maka silahkan masuk dengan membuat akun terlebih dahulu atau biasa disebut dengan register. Berikut caranya:

1.	Setelah berhasil masuk ke dalam program. Mulailah dengan menginput nomor yang menu yang ingin diakses.
2.	Ketika user menginputkan nomor 1, maka user memilih untuk menambahkan kontak. User diminta untuk menginputkan nama dan nomo telepon baru. Kemudia user kembali untuk memilih menu lainnya.
3.	Lalu, saat use menginputkan nomo2, maka user memilih untuk menghapus kontak dengan perintah user harus memasukkan nama kontak yang ingin dihapus.
4.	Kemudian jika user menginputkan pilihan nomor 3, maka user memilih untuk melihat kontak yang sudah di urutkan berdasarkan dua kategori yaitu, pilihan 1 untuk urut berdasarkan kategori nama dan pilihan 2 urut berdasarkan kategori nomor telepon.
5.	Selanjutnya, apabila user menginputkan pilihan menu nomor 4, bererti user memilih untuk mencari kontak dengan menginputkan nama kontak yang ingin dicari. Maka akan tampil nama beserta nomor telepon yang mungkin dicari.
6.	Kemudian jika user menginputkan pilihan nomor 5, berarti user ingin memilih menu melihat history kontak. Dalam hal ini yaitu history yang paling terakhir dilakukan.
7.	Jika user menginputkan nomor 6, maka user akan mengupdate kontak untuk memodifikasi nomor telepon dengan cara menginputkan nama yang ingin di modifikasi nomor teleponnya.
8.	Saat user memilih nomor 7, user akan keluar dari menu bukan keluar dari program. Maksudnya user akan kembali pada tampilan pilihan login dan register.

Itulah cara untuk menggunakan program kami. Mudah-mudahan apa yang kami sampaikan dapat dimenegerti dan mudah untuk dipahampi.
