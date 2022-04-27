# Belajar-Python🐍
 - <a href="https://www.python.org/">Website resmi Python</a>
 - <a href="https://visualstudio.microsoft.com/">Text Editor (disini saya menggunakan VSCODE)</a>
  <h3>Sejarah singkat Python</h3>
  <p><a href="#">Python</a> adalah bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. Dibuat oleh <a href="#">Guido van Rossum</a> dan pertama kali dirilis pada tahun 1991, filosofi desain <a href="#">Python</a> menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan. Konstruksi bahasanya dan pendekatan berorientasi objek bertujuan untuk membantu pemrogram menulis kode yang jelas dan logis untuk proyek skala kecil dan besar.</p>
  <hr>
  <h3>Panduan menginstall Python</h3>
  Cara menginstal python sangat mudah, ikuti panduan dibawah ini. Dibawah adalah panduan cara instal python di platform <a href="#">Linux,<a href="#">Windows</a> dan <a href="#">Mac OS</a>.
  <h3>Linux</h3>
 <p>1. Buka browser, kunjungi http://www.python.org/downloads/source/ </p>
 <p>2. Download versi terbaru Python berbentuk file zip untuk Unix/Linux</p>
 <p>3. Ekstrak file zip yang baru saja di download</p>
 <p>4. Edit file Modules/Setup jika Anda ingin kostumisasi Python
     Jalankan 

`./configure`.

script

`make`

`make install`

 </p>
 <p> Langkah ini akan menginstal Python di lokasi standar /usr/local/bin dan library di /usr/local/lib/pythonXX dimana XX adalah versi terbaru Python yang anda gunakan.</p>

>Untuk beberapa distro (distribution store) dari sistem operasi linux sudah terinstal Python di dalamnya. Jadi Anda tidak perlu menginstalnya lagi.
  
  <h3>Hello World</h3>
  <p>Hello world (Halo dunia) umumnya adalah program komputer yang mengeluarkan atau menampilkan pesan "Hello, World!". Program semacam itu sangat sederhana di sebagian besar bahasa pemrograman, dan sering digunakan untuk menggambarkan sintaks dasar bahasa pemrograman.</p>
  untuk bahasa Python kalian tinggal mengetik :

```Python
print("Hello world")
```
 <p>Maka menghasilkan output: 

`Hello world`.

<p>Python bersifat case sensitif, ini artinya huruf besar dan huruf kecil memiliki perbedaan. Sebagai contoh jika Anda menggunakan fungsi print dengan huruf kecil 

``print()``  akan berhasil. Lain hal jika anda menggunakan huruf kapital
 
``Print()`` 

atau

 ``PRINT()`` 

maka akan muncul pesan error.
Aturan ini berlaku untuk nama variabel ataupun fungsi-fungsi lainnya.  </p>
<hr>
<h3>Komentar pada Python</h3>
<p>Komentar (comment) adalah kode di dalam script Python yang tidak dieksekusi atau tidak dijalankan mesin. Komentar hanya digunakan untuk menandai atau memberikan keterangan tertulis pada script.</p>
<p>untuk membuat komentar kalian hanya perlu mengetik 

``#`` dan di ikuti dengan komentar kalian,contohnya 👇

```Python
#ini komentar satu baris
'''
ini menyatakan komentar
lebih dari satu baris 
'''
#dibuat oleh Andhika Pratama Putra
#aku rindu kamu T💙
print("=" * 10)
#maka yang tampil di output hanya tulisan = dikali 10 atau ==========

#mencetak angka/integer
print(127)

```

<hr>
<h3>Tipe Data</h3>
<p>Tipe data adalah suatu media atau memori pada komputer yang digunakan untuk menampung informasi.</h3>
Berikut adalah tipe data dari bahasa pemrograman Python :

```Python

 Boolean
 contohnya   :  ``True``  dan  ``False``
 Penjelasaan : Benar jika True atau 1 dan salah jika False atau 0
   
 String
 contohnya   : "aku Andhika"
 Penjelasaan : Menyatakan karakter/kalimat bisa berupa huruf angka, dll (diapit tanda ' atau ")
 
 Integer
 contohnya   : 25 atau 1209
 Penjelasaan : Menyatakan bilangan bulat

 Float
 contohnya   : 3.14 dan 7.2
 Penjelasan  : Bilangan yang mempunyai koma

 Hexadecimal
 contohnya   : 9a dan 3b
 Penjelasan  : Menyatakan bilangan hexa (bilangan berbasis 16)
 
 Complex 
 contohnya   : 2 + 3x
 Penjelasan  : Menyatakan angka real dan imajiner

 List
 contohnya   : ['tia',222,9.8]
 Penjelasan  : Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah

 Tuple
 contohnya   : ['tia',222,9.8]
 Penjelasan  : Data untaian yang menyimpan berbagai tipe data tetapi isinya tidak bisa diubah-ubah

 Dictionary
 contohnya   : {'nama':'Tia','id':1}
 Penjelasaan : Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai
 
```
<h3>Contoh penerapan tipe data👇</h3>

```Python

'''
 Sumber:https://belajarpython.com/tutorial/tipe-data-python
'''
#tipe data Boolean
print(True)

#tipe data String
print("Ayo belajar Python")
print('Belajar Python Sangat Mudah')

#tipe data Integer
print(20)

#tipe data Float
print(3.14)

#tipe data Hexadecimal
print(9a)

#tipe data Complex
print(5j)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Agung", 'umur':20})
#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':16} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary

```
<hr>
<h3>Variabel dalam Python</h3>
<p>Variabel adalah lokasi memori yang dicadangkan untuk menyimpan nilai-nilai. Ini berarti bahwa ketika Anda membuat sebuah variabel Anda memesan beberapa ruang di memori. Variabel menyimpan data yang dilakukan selama program dieksekusi, yang nantinya isi dari variabel tersebut dapat diubah oleh operasi - operasi tertentu pada program yang menggunakan variabel.</p>
Penulisan variabel Python sendiri juga memiliki aturan tertentu, yaitu :
 <p>1. Karakter pertama harus berupa huruf atau garis bawah/underscore 
   
   _


   
  </p>
   
 <p>2. Karakter selanjutnya dapat berupa huruf, garis bawah/underscore 
    
    _

   atau angka</p>

 <p>3. Karakter pada nama variabel bersifat sensitif (case-sensitif). Artinya huruf kecil dan huruf besar dibedakan. Sebagai contoh, variabel 
       
       akudia  dan  akuDia    adalah variabel yang berbeda
   
  <p>Untuk mulai membuat variabel di Python caranya sangat mudah, Anda cukup menuliskan variabel lalu mengisinya dengan suatu nilai dengan cara menambahkan tanda sama dengan  =  </p>

<h3>Penerapan variabel dalam Python👇</h3>

```Python

#proses memasukan data ke dalam variabel
nama = "Andhika Pratama Putra"
#proses mencetak variabel
print(nama)

#nilai dan tipe data dalam variabel  dapat diubah
umur = 20               #nilai awal
print(umur)             #mencetak nilai umur
type(umur)              #mengecek tipe data umur
umur = "dua puluh satu" #nilai setelah diubah
print(umur)             #mencetak nilai umur
type(umur)              #mengecek tipe data umur

namaDepan = "Diandra"
namaBelakang = "naufal"
nama = namaDepan + " " + namaBelakang
umur = 18
hobi = "Sepak bola"
print("Biodata\n", nama, "\n", umur, "\n", hobi)

#contoh variabel lainya
inivariabel = "Halo"
ini_juga_variabel = "Hai"
_inivariabeljuga = "Hi"
inivariabel222 = "Bye" 

panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)





```
<hr>
<h3>Operator di Python</h3>
<p>Operator adalah konstruksi yang dapat memanipulasi nilai dari operan.

Sebagai contoh operasi 3 + 2 = 5. Disini 3 dan 2 adalah operan dan + adalah operator</p>
<p>Bahasa pemrograman Python mendukung berbagai macam operator, diantaranya :</p>
 - <h5>Operator Aritmatika (Arithmathic Operators)</h5>
 - <h5>Operator Perbandingan (Comparison (Relational) Operators</h5>
 - <h5>Operator Penugasan (Assignment Operators)

```Python

 

