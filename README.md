# Laporan Proyek Kesehatan - Faishal Anwar Hasyim

## Tentang Penulis
- **Fasihal Anwar Hasyim**  
  NIM: 32602300021

- **Haydar Fahri Alaudin**  
  NIM: 32602300010

- **Mumtaz Fikri Nasrullan**  
  NIM: 32602300002

## Akses Aplikasi
Proyek web aplikasi ini sudah dihosting dan dapat diakses di link berikut:  
[https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/](https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/)

Jika Anda menemukan aplikasi ini bermanfaat, suara positif akan sangat dihargai.

## Aplikasi Kesehatan

## Domain Proyek
Proyek ini bertujuan untuk membangun aplikasi kesehatan yang dapat membantu pengguna dalam menghitung Indeks Massa Tubuh (BMI), kebutuhan kalori harian, dan mendiagnosis penyakit kulit menggunakan teknologi machine learning. Dengan meningkatnya kesadaran akan kesehatan, aplikasi ini diharapkan dapat memberikan informasi yang berguna bagi pengguna untuk menjaga kesehatan mereka.

## Business Understanding

### Problem Statements

- **Pernyataan Masalah**: Bagaimana merancang aplikasi yang dapat membantu pengguna menghitung BMI, kebutuhan kalori harian, dan mendiagnosis penyakit kulit dengan akurasi yang tinggi?

### Goals
- **Jawaban pernyataan masalah**: Membangun aplikasi kesehatan yang dapat menghitung BMI, kebutuhan kalori harian, dan mendiagnosis penyakit kulit dengan akurasi yang tinggi.

### Solution Statement
- **Penggunaan Multiple Algoritma**: Aplikasi ini menggunakan algoritma untuk menghitung BMI dan kebutuhan kalori, serta model machine learning untuk mendiagnosis penyakit kulit berdasarkan gambar.
- **Data Preparation**: Proyek ini akan menggunakan teknik data preparation untuk meningkatkan kualitas data dan performa model.

## Data Understanding

### Dataset
Aplikasi ini tidak menggunakan dataset eksternal, tetapi menggunakan rumus dan algoritma untuk menghitung BMI dan kebutuhan kalori. Untuk klasifikasi penyakit kulit, model machine learning dilatih menggunakan dataset gambar yang telah diberi label.

## Exploratory Data Analysis
Aplikasi ini tidak melakukan analisis data eksplorasi secara mendalam, tetapi memberikan informasi yang relevan kepada pengguna berdasarkan input yang diberikan.

## Data Preparation
Proses data preparation pada aplikasi ini terdiri dari beberapa tahapan:

### Data Cleaning
- Menghapus duplikat dan nilai kosong.
- Menghapus outlier jika diperlukan.

### Data Splitting
- Data dibagi menjadi set pelatihan dan pengujian jika menggunakan model machine learning.

### Creating Data Structures
- Struktur data dibuat untuk menghitung BMI dan kebutuhan kalori berdasarkan input pengguna.

## Modeling
Aplikasi ini menggunakan beberapa kelas untuk menghitung BMI, kebutuhan kalori, dan mendiagnosis penyakit kulit:

1. **BMICalculator**: Menghitung BMI berdasarkan berat dan tinggi badan.
2. **CalorieCalculator**: Menghitung kebutuhan kalori harian berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
3. **SkinDiseaseClassifier**: Menggunakan model machine learning untuk mendiagnosis penyakit kulit berdasarkan gambar.

## Evaluation
Aplikasi ini tidak menggunakan metrik evaluasi seperti RMSE, tetapi memberikan hasil langsung kepada pengguna berdasarkan input yang diberikan.

## Dampak Model terhadap Pemahaman Bisnis
Aplikasi ini memberikan informasi yang berguna bagi pengguna untuk memahami status kesehatan mereka dan mengambil langkah-langkah yang diperlukan untuk menjaga kesehatan.

## Kesimpulan
Aplikasi ini dirancang untuk membantu pengguna memahami dan mengelola kesehatan mereka dengan lebih baik. Dengan fitur-fitur seperti kalkulator BMI, kalkulator kebutuhan kalori, dan klasifikasi penyakit kulit, pengguna dapat membuat keputusan yang lebih baik terkait kesehatan mereka.
