# Sistem Pakar Menentukan Waktu Belajar Mahasiswa Menggunakan Metode Forward Chaining Berbasis Web

## Deskripsi

Sistem pakar ini dibuat untuk menentukan waktu belajar mahasiswa berdasarkan waktu yang dimiliki mahasiswa. Sistem pakar ini dibuat menggunakan metode forward chaining berbasis web. Sistem pakar ini dibuat menggunakan bahasa pemrograman Python dan framework Django.

## Cara Menjalankan

1. Pastikan Python sudah terinstall di komputer anda. Jika belum, silahkan download Python di https://www.python.org/downloads/
2. Buka terminal atau command prompt
3. Install virtualenv dengan perintah `pip install virtualenv`
4. Clone/Download repository ini
5. Masuk ke folder repository yang sudah di clone/download
6. Jalankan perintah `virtualenv env` untuk membuat virtual environment
7. Jalankan perintah `env\Scripts\activate` untuk mengaktifkan virtual environment
8. Jalankan perintah `pip install -r requirements.txt` untuk menginstall semua library yang dibutuhkan
9. Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi
10. Jalankan perintah `python manage.py migrate` untuk menjalankan migrasi
11. Jalankan perintah `python manage.py runserver` untuk menjalankan server
12. Buka browser dan ketikkan alamat `http://localhost:8000/` untuk mengakses sistem pakar
