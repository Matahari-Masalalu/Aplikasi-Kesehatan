# Laporan Proyek Kesehatan

## Tentang Penulis
Proyek ini dibuat sebagai tugas untuk mata kuliah **Pemrograman Berorientasi Objek**.

- **Faishal Anwar Hasyim**  
  NIM: 32602300021

- **Haydar Fahri Alaudin**  
  NIM: 32602300010

- **Mumtaz Fikri Nasrullah**  
  NIM: 32602300002

## Akses Aplikasi
Proyek web aplikasi ini dapat diakses di link berikut:  
[https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/](https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/)

Jika Anda menemukan aplikasi ini bermanfaat, suara positif akan sangat dihargai.

## Aplikasi Cek Obesitas dan Kesehatan

### Keterangan Aplikasi
Proyek ini bertujuan untuk membangun aplikasi kesehatan yang dapat membantu pengguna dalam menghitung Indeks Massa Tubuh (BMI), kebutuhan kalori harian, dan memberikan informasi tentang penyakit kulit. Dengan meningkatnya kesadaran akan kesehatan, aplikasi ini diharapkan dapat memberikan informasi yang berguna bagi pengguna untuk menjaga kesehatan mereka. 

Proyek ini mengintegrasikan teknologi web dengan machine learning untuk memberikan pengalaman pengguna yang interaktif dan informatif. Dengan memanfaatkan model machine learning, aplikasi ini tidak hanya menghitung BMI dan kebutuhan kalori, tetapi juga memberikan diagnosis awal untuk penyakit kulit berdasarkan gambar yang diunggah. Kolaborasi ini memungkinkan pengguna untuk mendapatkan informasi kesehatan yang lebih komprehensif dan akurat. 

## Tahapan Pembuatan Model Machine Learning untuk Memp rediksi Penyakit Kulit

1. **Pengumpulan Data**: Mengumpulkan dataset gambar penyakit kulit yang telah diberi label.
2. **Preprocessing Data**: Melakukan preprocessing pada gambar, termasuk resizing, normalisasi, dan augmentasi untuk meningkatkan variasi data dan mengurangi overfitting.
3. **Pembagian Data**: Membagi dataset menjadi set pelatihan dan set pengujian untuk melatih model dan menguji akurasinya.
4. **Pemilihan Model**: Memilih arsitektur model yang sesuai, seperti Convolutional Neural Networks (CNN), yang efektif untuk pengenalan gambar.
5. **Pelatihan Model**: Melatih model menggunakan data pelatihan dengan mengoptimalkan parameter model untuk meminimalkan loss function.
6. **Evaluasi Model**: Menggunakan data pengujian untuk mengevaluasi performa model. Metrik yang digunakan dapat mencakup akurasi, precision, recall, dan F1-score.
7. **Implementasi Model**: Mengimplementasikan model yang telah dilatih ke dalam aplikasi untuk memungkinkan pengguna mengunggah gambar dan mendapatkan prediksi.
8. **Pengujian dan Validasi**: Melakukan pengujian lebih lanjut untuk memastikan model memberikan hasil yang akurat dan dapat diandalkan dalam situasi nyata.

### Hasil Pelatihan Model
Berikut adalah hasil dari pelatihan model yang menunjukkan akurasi dan metrik lainnya:
![Hasil Pelatihan Model](https://github.com/user-attachments/assets/76dff109-97d7-4e01-9608-962a7846100a)

## Arsitektur Aplikasi
Aplikasi ini menggunakan beberapa kelas untuk menghitung BMI, kebutuhan kalori, dan memberikan informasi tentang penyakit kulit:
- **BMICalculator**: Menghitung BMI berdasarkan berat dan tinggi badan.
- **CalorieCalculator**: Menghitung kebutuhan kalori harian berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
- **SkinDiseaseClassifier**: Memberikan informasi tentang penyakit kulit berdasarkan gambar yang diunggah oleh pengguna.

## Evaluation
Aplikasi ini memberikan hasil langsung kepada pengguna berdasarkan input yang diberikan. Hasil dari kalkulasi BMI dan kebutuhan kalori ditampilkan secara real-time, sementara informasi tentang penyakit kulit disediakan berdasarkan gambar yang diunggah. Aplikasi ini dirancang untuk memberikan informasi yang akurat dan relevan untuk membantu pengguna dalam pengelolaan kesehatan mereka.

## Pembuatan Aplikasi
Aplikasi ini dibangun menggunakan **Streamlit**, sebuah framework Python yang memungkinkan pembuatan aplikasi web interaktif dengan cepat. Streamlit memudahkan pengembang untuk membuat antarmuka pengguna yang intuitif dan responsif, sehingga pengguna dapat dengan mudah mengakses fitur-fitur yang disediakan.


### Langkah-langkah Penggunaan Aplikasi
1. **Menu Home**: 
   - Di menu ini, Anda akan menemukan informasi mengenai aplikasi dan cara penggunaannya.
   ![Cuplikan layar Home](https://github.com/user-attachments/assets/032fb36e-df65-4a19-97f2-604a43128b14)

2. **Menu Obesitas (Obesity)**: 
   - **Informasi tentang Obesitas**: Menyediakan penjelasan mengenai obesitas, faktor penyebab, dan dampaknya terhadap kesehatan.
   ![Cuplikan layar Obesitas](https://github.com/user-attachments/assets/96ac94ae-5d71-4c5f-831a-7e6fab4a3195)
   - **Kalkulator BMI**: Menghitung Indeks Massa Tubuh (BMI) Anda berdasarkan berat dan tinggi badan.
   ![Cuplikan layar Kalkulator BMI](https://github.com/user-attachments/assets/3c411611-e5f7-476e-8949-a306ef693bc2)

3. **Menu Kebutuhan Kalori (Calories)**: 
   - **Informasi tentang Kebutuhan Kalori**: Menyediakan penjelasan mengenai pentingnya menghitung kebutuhan kalori harian.
   ![Cuplikan layar Kebutuhan Kalori](https://github.com/user-attachments/assets/9bfdcd85-5ef9-44be-8dc0-7d4ec7942525)
   - **Kalkulator Kebutuhan Kalori**: Menghitung kebutuhan kalori harian Anda berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
   ![Cuplikan layar Kalkulator Kebutuhan Kalori](https://github.com/user-attachments/assets/f33f5bb7-fcb6-44da-9d31-a337cfe644c8)

4. **Menu Penyakit Kulit (Skin)**: 
   - **Informasi tentang Penyakit Kulit**: Menyediakan penjelasan mengenai berbagai jenis penyakit kulit dan gejalanya.
   ![Cuplikan layar Penyakit Kulit](https://github.com/user-attachments/assets/cadd58a6-1588-4b27-8f19-f52e844a0be7)
   - **Prediksi Penyakit Kulit**: Menggunakan model machine learning untuk mendiagnosis penyakit kulit berdasarkan gambar yang diunggah oleh pengguna.
   ![Cuplikan layar Prediksi Penyakit Kulit](https://github.com/user-attachments/assets/3368948d-cb7e-481b-b521-2c6e9b78cf20)

5. **Menu Tentang Aplikasi (About)**: 
   - Di menu ini, Anda akan menemukan informasi tentang pembuat aplikasi dan penjelasan singkat mengenai aplikasi itu sendiri.
   ![Cuplikan layar Tentang Aplikasi ](https://github.com/user-attachments/assets/128a119c-d9ee-42b0-833d-3e10876db0d2)

### Use Case Diagram
![1](https://github.com/user-attachments/assets/2bd46437-7216-48cd-9366-daf7d573ba74)

#### Penjelasan dari Use Case Diagram:
1. **Home Menu**
   - **Fungsi Utama:**
     - Memberikan informasi umum tentang kesehatan dan sistem dari aplikasi.
     - Mengarahkan pengguna ke media sosial creator.
   - **Relasi:**
     - Terdapat relasi include untuk memberikan informasi umum tentang kesehatan dan sistem dari aplikasi.
     - Terdapat relasi extend untuk mengarahkan pengguna ke media sosial creator.

2. **Obesity Menu**
   - **Fungsi Utama:**
     - Memberikan informasi tentang obesitas.
     - Menyediakan kalkulator BMI/obesity calculator.
   - **Proses:**
     - Pengguna memasukkan:
       1. Umur (dalam tahun),
       2. Berat badan (kg),
       3. Tinggi badan (cm),
       4. Jenis kelamin.
     - Sistem memvalidasi nilai yang dimasukkan.
     - Hasil berupa nilai BMI dan rekomendasi berdasarkan kondisi pengguna.
   - **Relasi:**
     - include:
       1. Relasi ke fitur Informasi tentang obesitas.
       2. Relasi ke BMI Calculator / Obesity Calculator, yang merupakan bagian utama dari menu ini.

3. **Calories Menu**
   - **Fungsi Utama:**
     - Memberikan informasi tentang kebutuhan kalori.
     - Menyediakan kalkulator kebutuhan kalori harian.
   - **Proses:**
     - Pengguna memasukkan:
       1. Umur (dalam tahun),
       2. Berat badan (kg),
       3. Tinggi badan (cm),
       4. Jenis kelamin,
       5. Tingkat aktivitas.
     - Sistem memvalidasi nilai yang dimasukkan.
     - Hasil berupa kebutuhan kalori harian berdasarkan data yang diberikan.
   - **Relasi:**
     - include:
       1. Relasi ke fitur Informasi tentang kebutuhan kalori.
       2. Relasi ke Kalkulator kebutuhan kalori harian, yang merupakan bagian inti dari menu ini.

4. **Skin Menu**
   - **Fungsi Utama:**
     - Memberikan informasi tentang penyakit kulit.
     - Menyediakan fitur prediksi penyakit kulit melalui gambar.
   - **Proses:**
     - Pengguna mengunggah gambar kulit mereka.
     - Sistem memproses gambar dan memberikan hasil prediksi penyakit kulit.
   - **Relasi:**
     - include:
       1. Relasi ke fitur Informasi tentang penyakit kulit.
       2. Relasi ke Prediksi penyakit kulit melalui gambar sebagai bagian utama menu ini.

5. **About Menu**
   - **Fungsi Utama:**
     - Memberikan informasi tentang aplikasi dan pembuatnya.
   - **Relasi:**
     - include:
       1. Relasi ke fitur Informasi tentang aplikasi dan creator.

### Activity Diagram
![Cuplikan layar 2025-01-14 045039](https://github.com/user-attachments/assets/d15decb9-0ee1-426d-8a36-986565eaccd7)

#### Penjelasan Alur Aktivitas:
1. **Masuk ke Home Menu:**
   - **Aktivitas Awal:**
     - Pengguna masuk ke Home Menu.
   - **Proses:**
     - Menampilkan informasi umum tentang kesehatan dan aplikasi.
     - Mengarahkan pengguna ke media sosial creator.

2. **Memilih Menu Obesity:**
   - **Proses:**
     - Aplikasi menampilkan informasi tentang obesitas.
     - Aplikasi menyediakan fitur kalkulator BMI.
   - **Input Pengguna:**
     - Pengguna memasukkan data berupa:
       1. Tinggi badan,
       2. Berat badan,
       3. Umur,
       4. Jenis kelamin.
   - **Validasi Data:**
     - Sistem memvalidasi data yang dimasukkan.
   - **Hasil:**
     - Aplikasi menampilkan hasil perhitungan BMI dan rekomendasi untuk pengguna.

3. **Memilih Menu Calories:**
   - **Proses:**
     - Aplikasi menampilkan informasi tentang kebutuhan kalori.
     - Aplikasi menyediakan fitur kalkulator kalori harian.
   - **Input Pengguna:**
     - Pengguna memasukkan data berupa:
       1. Tinggi badan,
       2. Berat badan,
       3. Umur,
       4. Jenis kelamin,
       5. Tingkat aktivitas.
   - **Validasi Data:**
     - Sistem memvalidasi data yang dimasukkan.
   - **Hasil:**
     - Aplikasi menampilkan hasil perhitungan kebutuhan kalori harian beserta rekomendasi.

4. **Memilih Menu Skin:**
   - **Proses:**
     - Aplikasi menampilkan informasi tentang penyakit kulit.
     - Aplikasi menyediakan fitur prediksi penyakit kulit menggunakan klasifikasi gambar.
   - **Input Pengguna:**
     - Pengguna mengunggah gambar kulit yang ingin diperiksa.
   - **Validasi Data:**
     - Sistem memvalidasi gambar yang diunggah.
   - **Hasil:**
     - Aplikasi menampilkan prediksi penyakit kulit berdasarkan gambar yang diunggah.

5. **Memilih Menu About:**
   - **Proses:**
     - Aplikasi menampilkan informasi tentang aplikasi dan pembuatnya.

### Class Diagram
![Cuplikan layar 2025-01-14 045058](https://github.com/user-attachments/assets/e6b48dba-a828-4250-b90b-beee9a377211)

#### Deskripsi Umum Sistem
Class diagram yang dibuat menggambarkan hubungan antara berbagai kelas dalam sistem, yaitu **BMICalculator**, **CalorieCalculator**, **SkinDiseaseClassifier**, dan **User **. Diagram ini menunjukkan struktur statis dari sistem, termasuk atribut, metode, dan relasi antar kelas. Sistem ini dirancang untuk:
- Menghitung BMI dan memberikan kategori kesehatan.
- Menghitung kebutuhan kalori harian berdasarkan data pengguna.
- Mengklasifikasikan gambar penyakit kulit menggunakan model AI.
- Mengelola data pengguna, seperti usia, berat badan, tinggi badan, jenis kelamin, dan tingkat aktivitas.

#### Penjelasan Kelas
a. **BMICalculator**
- **Atribut**: weight, height
- **Metode**:
  - `calculate_bmi()`: Menghitung nilai BMI berdasarkan berat dan tinggi badan.
  - `get_bmi_category(bmi)`: Menentukan kategori kesehatan berdasarkan nilai BMI.
- **Fungsi**: Mengolah data berat dan tinggi badan untuk memberikan hasil BMI dan kategori terkait.

b. **CalorieCalculator**
- **Atribut**: user
- **Metode**:
  - `calculate_bmr()`: Menghitung Basal Metabolic Rate (BMR) berdasarkan data pengguna.
  - `calculate_daily_calories()`: Menghitung kebutuhan kalori harian berdasarkan tingkat aktivitas pengguna.
- **Fungsi**: Membantu pengguna memahami kebutuhan kalori mereka untuk menjaga atau menurunkan berat badan.

c. **SkinDiseaseClassifier**
- **Atribut**:
  - interpreter: Objek model TensorFlow Lite.
  - class_names: Daftar label penyakit kulit.
- **Metode**:
  - `load_model(model_path)`: Memuat model AI dari file.
  - `load_labels(label_path)`: Memuat label klasifikasi dari file.
  - `classify_image(image, img_size)`: Mengklasifikasikan gambar untuk mendeteksi jenis penyakit kulit.
- **Fungsi**: Menggunakan model AI untuk menganalisis gambar dan memberikan diagnosis penyakit kulit.

d. **User **
- **Atribut**:
  - age, height, weight, gender, activity_level
- **Fungsi**: Menyimpan data pengguna yang digunakan oleh kelas lain untuk perhitungan atau analisis.

#### Hubungan Antar Kelas
a. **User  ↔ BMICalculator**
- **Relasi**: Asosiasi
- **Multiplicity**: 1..1 (Setiap pengguna memiliki satu objek BMICalculator untuk menghitung BMI).
- **Penjelasan**: BMICalculator menggunakan data weight dan height dari User untuk menghitung BMI.

b. **User  ↔ CalorieCalculator**
- **Relasi**: Komposisi
- **Multiplicity**: 1..1 (Setiap pengguna memiliki satu CalorieCalculator untuk menghitung kebutuhan kalori).
- **Penjelasan**: CalorieCalculator memanfaatkan seluruh atribut dari User untuk menghitung BMR dan kebutuhan kalori harian.

c. **SkinDiseaseClassifier ↔ User**
- **Relasi**: Tidak langsung (opsional)

d. **SkinDiseaseClassifier ↔ TensorFlow, NumPy, Pillow**
- **Penjelasan**: SkinDiseaseClassifier bergantung pada pustaka eksternal untuk memproses gambar, mengelola data numerik, dan menjalankan model AI.

#### Multiplicity dalam Diagram
- **1..1**: Setiap pengguna (user) memiliki tepat satu hubungan dengan BMICalculator dan CalorieCalculator.
- SkinDiseaseClassifier dapat memproses banyak gambar, tetapi tidak terkait langsung dengan User.

### Deployment Diagram
![Cuplikan layar 2025-01-14 045111](https://github.com/user-attachments/assets/b6daeaa8-9eff-4d17-9948-6b4529095449)

#### Diagram deployment tersebut menunjukkan arsitektur sistem yang melibatkan tiga perangkat utama, yaitu Local Server, GitHub Repository, dan Web Server (Streamlit). Berikut adalah penjelasan tiap komponen:

1. **Local Server**
   - **Browser / Client**: Digunakan oleh pengguna untuk mengakses aplikasi melalui antarmuka web.
   - **Interact (HTTP/HTTPS)**: Interaksi antara klien dan server menggunakan protokol HTTP atau HTTPS, memastikan komunikasi aman.

2. **Web Server (Streamlit)**
   - **Streamlit App**: Aplikasi berbasis Streamlit yang bertanggung jawab menampilkan antarmuka aplikasi kepada pengguna.
   - **Backend Logic (Python)**: Logika backend yang menjalankan fungsi utama aplikasi, seperti menjalankan model machine learning atau pengolahan data.
   - **UI / UX**: Elemen antarmuka pengguna (User  Interface/User Experience) untuk berinteraksi dengan aplikasi secara visual.
   - **Accesses GitHub**: Menghubungkan server ke GitHub Repository untuk mengambil kode sumber, model, atau dataset yang diperlukan.

3. **GitHub Repository**
   - **Data Files**: Menyimpan berbagai file yang diperlukan, seperti file Python (.py), file gambar (.jpg), file teks (.txt), file model (.tflite), dan file Python bytecode (.pyc).
   - **Scripts: Python Logic**: Kumpulan kode logika program yang ditulis menggunakan Python.
   - **Source Code & Dataset**: Kode sumber aplikasi serta dataset yang digunakan.
   - **Requirements**: File berisi daftar dependensi yang diperlukan untuk menjalankan aplikasi (contoh: requirements.txt).
   - **Model**: Model pembelajaran mesin (machine learning) yang digunakan dalam aplikasi.

4. **Alur Kerja**
   1. Local Server melalui browser mengirimkan permintaan ke Web Server menggunakan protokol HTTP/HTTPS.
   2. Web Server yang menjalankan aplikasi Streamlit menerima permintaan tersebut.
   3. Jika diperlukan, Web Server akan mengakses file atau model dari GitHub Repository.
   4. Aplikasi di Web Server memproses data, menjalankan model, dan menampilkan hasil melalui antarmuka Streamlit ke browser klien.

## Kesimpulan
Aplikasi ini dirancang untuk membantu pengguna memahami dan mengelola kesehatan mereka dengan lebih baik. Dengan fitur-fitur seperti kalkulator BMI, kalkulator kebutuhan kalori, dan informasi tentang penyakit kulit, pengguna dapat membuat keputusan yang lebih baik terkait kesehatan mereka. Selain itu, dengan adanya model machine learning untuk memprediksi penyakit kulit, aplikasi ini memberikan nilai tambah yang signifikan dalam mendukung pengguna dalam menjaga kesehatan kulit mereka.
