import streamlit as st
from classes.user import User
from classes.calorie_calculator import CalorieCalculator

class CaloriesPage:
    def __init__(self):
        self.title = "Kalkulator Kebutuhan Kalori"

    def display(self):
        st.title(self.title)

        if 'page' not in st.session_state:
            st.session_state.page = 'info'

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Informasi tentang Kebutuhan Kalori", key="info_button"):
                st.session_state.page = "info"

        with col2:
            if st.button("Hitung Kebutuhan Kalori", key="calorie_button"):
                st.session_state.page = "calorie"

        if st.session_state.page == "calorie":
            self.calculate_calories()
        elif st.session_state.page == "info":
            self.display_info()

    def display_with_info(self):
        self.display_info()
        self.display()

    def calculate_calories(self):
        st.header("Hitung Kebutuhan Kalori Harian")
        st.header("Masukkan Data Anda")

        age = st.number_input("Umur (tahun)", min_value=0, format="%d")
        height = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f")
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f")
        gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        activity_level = st.selectbox("Tingkat Aktivitas", ["Sedentari (tidak aktif)", 
                                                              "Ringan (olahraga ringan 1-3 hari/minggu)", 
                                                              "Sedang (olahraga sedang 3-5 hari/minggu)", 
                                                              "Tinggi (olahraga berat 6-7 hari/minggu)"])

        if st.button("Hitung Kebutuhan Kalori Harian", key="calculate_calories"):
            if weight > 0 and height > 0 and age > 0:
                user = User(age, height, weight, gender, activity_level)
                calculator = CalorieCalculator(user)
                daily_calories = calculator.calculate_daily_calories()

                st.subheader("Hasil")
                st.write(f"Kebutuhan kalori harian Anda adalah: **{daily_calories:.2f} kalori**")
            else:
                st.warning("Silakan masukkan data yang valid.")

    def display_info(self):
        st.header("Informasi tentang Kebutuhan Kalori Harian")
        st.write("""
            Kebutuhan kalori harian bervariasi tergantung pada beberapa faktor termasuk umur, jenis kelamin, 
            tinggi badan, berat badan, dan tingkat aktivitas. 
            Penting untuk mengetahui kebutuhan kalori agar Anda dapat menjaga berat badan yang sehat dan 
            menghindari masalah kesehatan yang terkait dengan asupan kalori yang tidak seimbang.
            
            Berikut adalah rumus untuk menghitung BMR (Basal Metabolic Rate):
            
            $$
            BMR = 10 \times berat \, (kg) + 6.25 \times tinggi \, (cm) - 5 \times umur \, (tahun) + 5 \, (Laki-laki) \, atau \, -161 \, (Perempuan)
            $$
            
            Setelah BMR dihitung, kali dengan faktor aktivitas untuk mendapatkan kebutuhan kalori harian:
            - Sedentari (tidak aktif): BMR × 1.2
            - Ringan (olahraga ringan/satu kali seminggu): BMR × 1.375
            - Sedang (olahraga sedang/3-5 kali seminggu): BMR × 1.55
            - Aktif (olahraga berat/6-7 kali seminggu): BMR × 1.725
        """)

        st.subheader("Mengapa Penting untuk Menghitung Kebutuhan Kalori?")
        st.write("""
            Menghitung kebutuhan kalori dapat membantu Anda menentukan asupan kalori yang tepat untuk mencapai tujuan 
            kesehatan Anda, baik itu untuk menurunkan berat badan, mempertahankan berat badan, atau menambah berat badan. 
            Dengan pemahaman yang baik tentang kebutuhan kalori Anda, Anda dapat membuat pilihan makanan yang lebih sehat 
            dan mengikuti pola hidup yang lebih aktif.
        """)
