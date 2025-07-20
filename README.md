# Grafkom-
Project Tugas Grafkom 
soal yang di dapat sebagai berikut : 
Modul A: Objek 2D
A. Fungsi Penggambaran Objek
a) Aplikasi harus bisa menggambar objek-objek dasar berupa Titik, Garis, Persegi, dan Ellipse.
b) Penentuan koordinat untuk menggambar objek dilakukan melalui input klik mouse pada kanvas.
B. Fungsi Warna & Ketebalan
a) Pengguna harus dapat memilih warna objek yang akan digambar.
b) Pengguna harus dapat mengatur ketebalan garis, khususnya untuk objek yang digambar menggunakan GL_LINES atau GL_LINE_LOOP.
C. Transformasi Geometri
a) Setiap objek yang telah digambar harus bisa dikenai transformasi geometri, yaitu Translasi, Rotasi, dan Skala.
b) Proses transformasi ini dikontrol melalui input keyboard atau shortcut.
D. Windowing dan Clipping
a) Pengguna dapat menentukan sebuah window aktif di dalam kanvas, misalnya dengan mengklik dua titik sudut.
b) Objek yang berada sepenuhnya di dalam window akan berubah warna (contoh: hijau).
c) Objek yang berada di luar atau sebagian di luar window akan di-clipping, di mana hanya bagian yang berada di dalam window yang ditampilkan.
d) Proses clipping untuk garis harus menggunakan algoritma Cohen-Sutherland atau Liang-Barsky.

Modul B: Objek 3D (Untuk Pengembangan Lanjutan)
A. Visualisasi & Transformasi, Menampilkan objek 3D (Kubus/Piramida) dan memberinya transformasi.
B. Shading & Pencahayaan, Mengimplementasikan model pencahayaan Phong atau Gouraud dengan komponen ambient, diffuse, dan specular.
8
C. Kamera & Perspektif, Mengatur posisi kamera (gluLookAt) dan menggunakan proyeksi perspektif (gluPerspective).

*Cara penggunaan Aplikasi* 
- Pada mode 2D, pengguna dapat memilih jenis objek yang akan digambar melalui input keyboard sebagai berikut:
  Tekan '1' → Menggambar Titik 
  Tekan '2' → Menggambar Garis 
  Tekan '3' → Menggambar Persegi 
  Tekan '4' → Menggambar Elips 

- Objek 2D yang telah digambar dapat dimanipulasi secara langsung dengan tombol-tombol berikut:
  Translasi (pergeseran posisi):
  'w' → Geser ke atas
  'a' → Geser ke kiri
  's' → Geser ke bawah
  'd' → Geser ke kanan

- Rotasi:
  'e' → Putar searah jarum jam (dalam derajat)

- Skala:
  'z' → Perbesar objek
  'x' → Perkecil objek

- Pengguna juga dapat memodifikasi tampilan objek melalui:
  Warna:
  'r' → Mengubah warna objek menjadi merah
  'g' → Mengubah warna objek menjadi hijau
  'b' → Mengubah warna objek menjadi biru

- Ketebalan Garis:
  '+' → Menambah ketebalan garis (glLineWidth)
  '-' → Mengurangi ketebalan garis


