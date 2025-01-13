# Laporan Proyek Kesehatan

## Tentang Penulis
Proyek ini dibuat sebagai tugas untuk mata kuliah **Pemrograman Berorientasi Objek**.

**Faishal Anwar Hasyim**  
  NIM: 32602300021

**Haydar Fahri Alaudin**  
  NIM: 32602300010

**Mumtaz Fikri Nasrullan**  
  NIM: 32602300002

## Akses Aplikasi
Proyek web aplikasi ini sudah dihosting dan dapat diakses di link berikut:  
[https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/](https://aplikasi-kesehatan-mvmowvpwbc49kbjgx5fols.streamlit.app/)

Jika Anda menemukan aplikasi ini bermanfaat, suara positif akan sangat dihargai.

## Aplikasi Kesehatan

### Domain Proyek
Proyek ini bertujuan untuk membangun aplikasi kesehatan yang dapat membantu pengguna dalam:
- Menghitung Indeks Massa Tubuh (BMI)
- Menghitung kebutuhan kalori harian
- Memberikan informasi tentang penyakit kulit

Dengan meningkatnya kesadaran akan kesehatan, aplikasi ini diharapkan dapat memberikan informasi yang berguna bagi pengguna untuk menjaga kesehatan mereka. Proyek ini mengintegrasikan teknologi web dengan machine learning untuk memberikan pengalaman pengguna yang interaktif dan informatif.

### Fitur Utama
- **Kalkulator BMI**: Menghitung status obesitas pengguna.
- **Kalkulator Kebutuhan Kalori**: Menghitung kebutuhan kalori harian berdasarkan data pengguna.
- **Prediksi Penyakit Kulit**: Mendiagnosis penyakit kulit berdasarkan gambar yang diunggah.

## Langkah-langkah Penggunaan Aplikasi

1. **Menu Home**:
   - Informasi mengenai aplikasi dan cara penggunaannya.
   ![Cuplikan layar Home](https://github.com/user-attachments/assets/032fb36e-df65-4a19-97f2-604a43128b14)

2. **Menu Obesitas**:
   - **Informasi tentang Obesitas**: Penjelasan mengenai obesitas, faktor penyebab, dan dampaknya terhadap kesehatan.
   ![Cuplikan layar Obesitas](https://github.com/user-attachments/assets/96ac94ae-5d71-4c5f-831a-7e6fab4a3195)
   - **Kalkulator BMI**: Menghitung Indeks Massa Tubuh (BMI).
   ![Cuplikan layar Kalkulator BMI](https://github.com/user-attachments/assets/3c411611-e5f7-476e-8949-a306ef693bc2)

3. **Menu Kebutuhan Kalori**:
   - **Informasi tentang Kebutuhan Kalori**: Penjelasan mengenai pentingnya menghitung kebutuhan kalori harian.
   ![Cuplikan layar Kebutuhan Kalori](https://github.com/user-attachments/assets/9bfdcd85-5ef9-44be-8dc0-7d4ec7942525)
   - **Kalkulator Kebutuhan Kalori**: Menghitung kebutuhan kalori harian.
   ![Cuplikan layar Kalkulator Kebutuhan Kalori](https://github.com/user-attachments/assets/f33f5bb7-fcb6-44da-9d31-a337cfe644c8)

4. **Menu Penyakit Kulit**:
   - **Informasi tentang Penyakit Kulit**: Penjelasan mengenai berbagai jenis penyakit kulit dan gejalanya.
   ![Cuplikan layar Penyakit Kulit](https://github.com/user-attachments/assets/cadd58a6-1588-4b27-8f19-f52e844a0be7)
   - **Prediksi Penyakit Kulit**: Mendiagnosis penyakit kulit berdasarkan gambar yang diunggah.
   ![Cuplikan layar Prediksi Penyakit Kulit](https://github.com/user-attachments/assets/3368948d-cb7e-481b-b521-2c6e9b78cf20)

5. **Menu Tentang Aplikasi**:
   - Informasi tentang pembuat aplikasi dan penjelasan singkat mengenai aplikasi itu sendiri.
   ![Cuplikan layar Tentang Aplikasi](https://github.com/user-attachments/assets/128a119c-d9ee-42b0-833d-3e10876db0d2)

## Tahapan Pembuatan Model Machine Learning untuk Memprediksi Penyakit Kulit

1. **Pengumpulan Data**: Mengumpulkan dataset gambar penyakit kulit yang telah diberi label.
2. **Preprocessing Data**: Melakukan preprocessing pada gambar, termasuk resizing, normalisasi, dan augmentasi untuk meningkatkan variasi data dan mengurangi overfitting.
3. **Pembagian Data**: Membagi dataset menjadi set pelatihan dan set pengujian untuk melatih model dan menguji akurasinya.
4. **Pemilihan Model**: Memilih arsitektur model yang sesuai, seperti Convolutional Neural Networks (CNN), yang efektif untuk pengenalan gambar.
5. **Pelatihan Model**: Melatih model menggunakan data pelatihan dengan mengoptimalkan parameter model untuk meminimalkan loss function.
6. **Evaluasi Model**: Menggunakan data pengujian untuk mengevaluasi performa model. Metrik yang digunakan dapat mencakup akurasi, precision, recall, dan F1-score.
7. **Implementasi Model**: Mengimplementasikan model yang telah dilatih ke dalam aplikasi untuk memungkinkan pengguna mengunggah gambar dan mendapatkan prediksi.
8. **Pengujian dan Validasi**: Melakukan pengujian lebih lanjut untuk memastikan model memberikan hasil yang akurat dan dapat diandalkan dalam situasi nyata.

## Modeling
Aplikasi ini menggunakan beberapa kelas untuk menghitung BMI, kebutuhan kalori, dan memberikan informasi tentang penyakit kulit:
- **BMICalculator**: Menghitung BMI berdasarkan berat dan tinggi badan.
- **CalorieCalculator**: Menghitung kebutuhan kalori harian berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
- **SkinDiseaseClassifier**: Memberikan informasi tentang penyakit kulit berdasarkan gambar yang diunggah oleh pengguna.

## Evaluation
Aplikasi ini memberikan hasil langsung kepada pengguna berdasarkan input yang diberikan. Hasil dari kalkulasi BMI dan kebutuhan kalori ditampilkan secara real-time, sementara informasi tentang penyakit kulit disediakan berdasarkan gambar yang diunggah. Aplikasi ini dirancang untuk memberikan informasi yang akurat dan relevan untuk membantu pengguna dalam pengelolaan kesehatan mereka.

## Pembuatan Aplikasi
Aplikasi ini dibangun menggunakan **Streamlit**, sebuah framework Python yang memungkinkan pembuatan aplikasi web interaktif dengan cepat. Streamlit memudahkan pengembang untuk membuat antarmuka pengguna yang intuitif dan responsif, sehingga pengguna dapat dengan mudah mengakses fitur-fitur yang disediakan.

## Kesimpulan
Aplikasi ini dirancang untuk membantu pengguna memahami dan mengelola kesehatan mereka dengan lebih baik. Dengan fitur-fitur seperti kalkulator BMI, kalkulator kebutuhan kalori, dan informasi tentang penyakit kulit, pengguna dapat membuat keputusan yang lebih baik terkait kesehatan mereka. Selain itu, dengan adanya model machine learning untuk memprediksi penyakit kulit, aplikasi ini memberikan nilai tambah yang signifikan dalam mendukung pengguna dalam menjaga kesehatan kulit mereka.
