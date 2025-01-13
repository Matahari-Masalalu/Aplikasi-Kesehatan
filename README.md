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
Proyek ini bertujuan untuk membangun aplikasi kesehatan yang dapat membantu pengguna dalam menghitung Indeks Massa Tubuh (BMI), kebutuhan kalori harian, dan memberikan informasi tentang penyakit kulit. Dengan meningkatnya kesadaran akan kesehatan, aplikasi ini diharapkan dapat memberikan informasi yang berguna bagi pengguna untuk menjaga kesehatan mereka.

Proyek ini mengintegrasikan teknologi web dengan machine learning untuk memberikan pengalaman pengguna yang interaktif dan informatif. Dengan memanfaatkan model machine learning, aplikasi ini tidak hanya menghitung BMI dan kebutuhan kalori, tetapi juga memberikan diagnosis awal untuk penyakit kulit berdasarkan gambar yang diunggah. Kolaborasi ini memungkinkan pengguna untuk mendapatkan informasi kesehatan yang lebih komprehensif dan akurat.

## Langkah-langkah Penggunaan Aplikasi

1. **Menu Home**:
   - Di menu ini, Anda akan menemukan informasi mengenai aplikasi dan cara penggunaannya. Ini adalah titik awal untuk memahami fitur-fitur yang tersedia.
   - ![Screenshot Menu Home](link_to_screenshot_home)

2. **Menu Obesitas**:
   - Di menu ini, terdapat dua opsi:
     - **Informasi tentang Obesitas**: Menyediakan penjelasan mengenai obesitas, faktor penyebab, dan dampaknya terhadap kesehatan.
       - ![Screenshot Informasi Obesitas](link_to_screenshot_obesity_info)
     - **Kalkulator BMI**: Menghitung Indeks Massa Tubuh (BMI) Anda berdasarkan berat dan tinggi badan untuk mengecek status obesitas.
       - ![Screenshot Kalkulator BMI](link_to_screenshot_bmi_calculator)

3. **Menu Kebutuhan Kalori**:
   - Di menu ini, terdapat dua opsi:
     - **Informasi tentang Kebutuhan Kalori**: Menyediakan penjelasan mengenai pentingnya menghitung kebutuhan kalori harian dan cara melakukannya.
       - ![Screenshot Informasi Kebutuhan Kalori](link_to_screenshot_calorie_info)
     - **Kalkulator Kebutuhan Kalori**: Menghitung kebutuhan kalori harian Anda berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
       - ![Screenshot Kalkulator Kebutuhan Kalori](link_to_screenshot_calorie_calculator)

4. **Menu Penyakit Kulit**:
   - Di menu ini, terdapat dua opsi:
     - **Informasi tentang Penyakit Kulit**: Menyediakan penjelasan mengenai berbagai jenis penyakit kulit dan gejalanya.
       - ![Screenshot Informasi Penyakit Kulit](link_to_screenshot_skin_disease_info)
     - **Prediksi Penyakit Kulit**: Menggunakan model machine learning untuk mendiagnosis penyakit kulit berdasarkan gambar yang diunggah oleh pengguna.
       - ![Screenshot Prediksi Penyakit Kulit](link_to_screenshot_skin_disease_prediction)

5. **Menu Tentang Aplikasi**:
   - Di menu ini, Anda akan menemukan informasi tentang pembuat aplikasi dan penjelasan singkat mengenai aplikasi itu sendiri.
   - ![Screenshot Tentang Aplikasi](link_to_screenshot_about_app)

## Tahapan Pembuatan Model Machine Learning untuk Memprediksi Penyakit Kulit

1. **Pengumpulan Data**:
   - Mengumpulkan dataset gambar penyakit kulit yang telah diberi label. Dataset ini harus mencakup berbagai jenis penyakit kulit untuk meningkatkan akurasi model.

2. **Preprocessing Data**:
   - Melakukan preprocessing pada gambar, termasuk resizing, normalisasi, dan augmentasi untuk meningkatkan variasi data dan mengurangi overfitting.

3. **Pembagian Data**:
   - Membagi dataset menjadi set pelatihan dan set pengujian untuk melatih model dan menguji akurasinya.

4. **Pemilihan Model**:
   - Memilih arsitektur model yang sesuai, seperti Convolutional Neural Networks (CNN), yang efektif untuk pengenalan gambar.

5. **Pelatihan Model**:
   - Melatih model menggunakan data pelatihan dengan mengoptimalkan parameter model untuk meminimalkan loss function.

6. **Evaluasi Model**:
   - Menggunakan data pengujian untuk mengevaluasi performa model. Metrik yang digunakan dapat mencakup akurasi, precision, recall, dan F1-score.

7. **Implementasi Model**:
   - Mengimplementasikan model yang telah dilatih ke dalam aplikasi untuk memungkinkan pengguna mengunggah gambar dan mendapatkan prediksi.

8. **Pengujian dan Validasi**:
   - Melakukan pengujian lebih lanjut untuk memastikan model memberikan hasil yang akurat dan dapat diandalkan dalam situasi nyata.

## Modeling
Aplikasi ini menggunakan beberapa kelas untuk menghitung BMI, kebutuhan kalori, dan memberikan informasi tentang penyakit kulit:

1. **BMICalculator**: Menghitung BMI berdasarkan berat dan tinggi badan.
2. **CalorieCalculator**: Menghitung kebutuhan kalori harian berdasarkan berat, tinggi, umur, jenis kelamin, dan tingkat aktivitas.
3. **SkinDiseaseClassifier**: Memberikan informasi tentang penyakit kulit berdasarkan gambar yang diunggah oleh pengguna.

## Evaluation
Aplikasi ini memberikan hasil langsung kepada pengguna berdasarkan input yang diberikan. Hasil dari kalkulasi BMI dan kebutuhan kalori ditampilkan secara real-time, sementara informasi tentang penyakit kulit disediakan berdasarkan gambar yang diunggah. Aplikasi ini dirancang untuk memberikan informasi yang akurat dan relevan untuk membantu pengguna dalam pengelolaan kesehatan mereka.

## Pembuatan Aplikasi
Aplikasi ini dibangun menggunakan **Streamlit**, sebuah framework Python yang memungkinkan pembuatan aplikasi web interaktif dengan cepat. Streamlit memudahkan pengembang untuk membuat antarmuka pengguna yang intuitif dan responsif, sehingga pengguna dapat dengan mudah mengakses fitur-fitur yang disediakan.

## Kesimpulan
Aplikasi ini dirancang untuk membantu pengguna memahami dan mengelola kesehatan mereka dengan lebih baik. Dengan fitur-fitur seperti kalkulator BMI, kalkulator kebutuhan kalori, dan informasi tentang penyakit kulit, pengguna dapat membuat keputusan yang lebih baik terkait kesehatan mereka. Selain itu, dengan adanya model machine learning untuk memprediksi penyakit kulit, aplikasi ini memberikan nilai tambah yang signifikan dalam mendukung pengguna dalam menjaga kesehatan kulit mereka.
