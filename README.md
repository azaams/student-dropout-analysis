# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi tersebut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat tantangan yang signifikan berupa banyaknya jumlah siswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
Tingkat dropout yang tinggi menjadi salah satu masalah besar bagi sebuah institusi pendidikan. Hal ini tidak hanya berdampak negatif pada reputasi akademik Jaya Jaya Institut di mata publik, tetapi juga berpotensi mengganggu stabilitas finansial dan operasional kampus. Oleh karena itu, pihak manajemen membutuhkan sistem deteksi dini untuk mengidentifikasi siswa yang memiliki probabilitas tinggi untuk melakukan dropout agar mereka dapat diberikan bimbingan atau intervensi khusus secepat mungkin.

### Cakupan Proyek
Untuk menyelesaikan permasalahan bisnis di atas, proyek ini mencakup tahapan-tahapan berikut:

1. Data Preparation dan Pembersihan Data: Memfilter data siswa yang berstatus "Enrolled" (masih aktif) untuk memfokuskan model pada klasifikasi murni antara "Graduate" dan "Dropout".

2. Exploratory Data Analysis (EDA): Melakukan analisis univariate, bivariate, dan multivariate untuk menemukan akar penyebab dropout.

3. Pembuatan Model Machine Learning: Mengembangkan model klasifikasi menggunakan algoritma Random Forest Classifier beserta pipeline pemrosesan data (StandardScaler dan OneHotEncoder) untuk memprediksi siswa yang berisiko dropout.

4. Pembuatan Business Dashboard: Membangun dashboard interaktif menggunakan Tableau untuk memantau performa siswa dan menyoroti metrik utama penyebab dropout secara dinamis.

5. Deployment Prototype: Membangun aplikasi web interaktif menggunakan Streamlit agar model prediksi dapat digunakan secara langsung oleh pengguna akhir (End-User).

### Persiapan
Data yang digunakan dalam proyek ini disediakan oleh Jaya Jaya Institut dan dapat diunduh melalui repositori GitHub resmi Dicoding pada tautan berikut:
Sumber data: [Dataset Students Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
Proyek ini dikembangkan menggunakan bahasa pemrograman Python. Berikut adalah daftar pustaka (library) utama yang dibutuhkan beserta cara instalasinya:

1. Pastikan Anda telah menginstal Python (disarankan versi 3.9 atau lebih baru).

2. Clone repositori proyek ini ke dalam direktori lokal Anda.

3. Buka terminal atau command prompt, lalu arahkan ke direktori proyek.

4. Instal seluruh library yang dibutuhkan dengan menjalankan perintah berikut:
```
pip install -r requirements.txt
```

## Business Dashboard
Untuk memudahkan manajemen Jaya Jaya Institut dalam memonitor performa siswa, sebuah Business Dashboard interaktif telah dikembangkan menggunakan Tableau. Dashboard ini berfokus pada tiga pilar utama penyebab dropout yang ditemukan dari ekstraksi Feature Importances algoritma Machine Learning:

1. Pilar Akademik: Menampilkan rata-rata tingkat kelulusan mata kuliah di semester dua.

2. Pilar Finansial: Menampilkan persentase risiko dropout berdasarkan status tunggakan uang kuliah (Paid vs Unpaid).

3. Pilar Demografi: Menampilkan distribusi usia pendaftar dan hubungannya dengan probabilitas dropout.

Dashboard ini juga dilengkapi dengan Key Performance Indicators (KPI) dan filter interaktif (Course dan Gender) yang memungkinkan pengguna untuk melakukan drill-down data secara dinamis.
Tautan Dashboard: [Link Dashboard](https://public.tableau.com/app/profile/azzam.mujahid/viz/Dashboard_17742091064500/Dashboard1?publish=yes)

## Menjalankan Sistem Machine Learning
Solusi Machine Learning telah dibungkus ke dalam prototype aplikasi web interaktif menggunakan Streamlit. Aplikasi ini memungkinkan pengguna (seperti tim HR atau akademik) untuk mengunggah file CSV berisi data mahasiswa dan mendapatkan hasil prediksi status dropout secara otomatis.

Tautan Streamlit Community Cloud: [Masukkan Link Aplikasi Streamlit Anda Di Sini, contoh:
```
Untuk menjalankan sistem dan mereproduksi hasil dari model Machine Learning ini, ikuti langkah-langkah berikut:

1. Unduh atau clone repositori ini ke dalam direktori lokal Anda.

2. Buka file Jupyter Notebook bernama notebook.ipynb.

3. Pastikan dataset data.csv berada di dalam folder yang sama atau sesuaikan path pemanggilan data pada cell pertama.

4. Jalankan setiap cell secara berurutan (Run All).

5. Pada bagian akhir, kode akan menghasilkan metrik evaluasi (seperti Accuracy, Precision, dan Recall) serta mengekspor file CSV bersih (mahasiswa_jaya_institut_cleaned.csv) yang digunakan sebagai sumber data pada dashboard Tableau.
```

## Conclusion
Berdasarkan hasil analisis data dan pelatihan model Random Forest yang menghasilkan tingkat akurasi 93% serta Recall untuk deteksi dropout sebesar 87%, ditarik tiga kesimpulan utama:

1. Performa Akademik adalah Kunci: Kegagalan dalam menyelesaikan (tidak lulus) unit kurikuler pada semester 1 dan semester 2 menjadi prediktor paling kuat yang mengarah pada keputusan dropout.

2. Risiko Tunggakan Finansial: Terdapat korelasi yang sangat tajam antara kepatuhan pembayaran uang kuliah dengan status dropout. Siswa yang memiliki status uang kuliah menunggak memiliki risiko dropout di atas 90 persen.

3. Kerentanan Usia Pendaftar: Usia saat pertama kali mendaftar (Age at enrollment) turut memengaruhi keberhasilan studi. Mahasiswa dengan usia yang lebih matang (kelas pekerja) menunjukkan tingkat kerentanan yang lebih tinggi terhadap dropout dibandingkan mahasiswa reguler yang masuk pada usia standar.

### Rekomendasi Action Items
Untuk menekan angka dropout, pihak Jaya Jaya Institut direkomendasikan untuk melakukan langkah-langkah preventif berikut:

- Membentuk Program Bimbingan Akademik Dini: Mengaktifkan pemantauan khusus pada akhir semester 1. Jika seorang siswa mulai menunjukkan kegagalan pada beberapa unit kurikuler, dosen pembimbing harus segera melakukan konseling akademik sebelum siswa memasuki semester 2.
- Restrukturisasi Skema Pembayaran: Bagian keuangan kampus perlu merancang skema cicilan pembayaran yang lebih fleksibel atau menawarkan program bantuan dana darurat bagi siswa yang mulai menunggak biaya kuliah di tahun pertama mereka.
- Pendampingan Mahasiswa Usia Lanjut: Menyediakan jadwal perkuliahan yang lebih fleksibel serta layanan manajemen waktu bagi mahasiswa yang mendaftar pada usia yang lebih tua, mengingat mereka rentan mengalami benturan antara tanggung jawab pekerjaan, keluarga, dan studi.
