import streamlit as st

class AboutPage:
    def __init__(self):
        self.title = "Tentang Aplikasi"

    def display(self):
        st.title(self.title)
        st.write("""
            Aplikasi ini dibuat untuk membantu Anda menghitung Indeks Massa Tubuh (BMI) dan kebutuhan kalori harian Anda.
            BMI adalah ukuran yang digunakan untuk menilai berat badan seseorang berdasarkan tinggi badan.
            
            **Catatan:** Hasil ini hanya untuk informasi dan tidak menggantikan saran medis profesional.
        """)

        st.header("Tentang Penulis")

        penulis = [
            {
                "nama": "Fasihal Anwar Hasyim",
                "nim": "32602300021",
                "gambar": "images/faishal.jpg"
            },
            {
                "nama": "Haydar Fahri Alaudin",
                "nim": "32602300010",
                "gambar": "images/haydar.jpeg"
            },
            {
                "nama": "Mumtaz Fikri Nasrullan",
                "nim": "32602300002",
                "gambar": "images/haydar.jpeg"
            }
        ]

        for penulis_info in penulis:
            st.subheader(penulis_info["nama"])
            st.write(f"NIM: {penulis_info['nim']}")
            st.image(penulis_info["gambar"], width=150)
