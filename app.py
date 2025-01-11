import streamlit as st
from views.home import HomePage
from views.obesity import ObesityPage
from views.calories import CaloriesPage
from views.skin import SkinPage
from views.about import AboutPage

# Fungsi untuk membuat tombol di sidebar
def sidebar_button(label, selected_page_name, selected_page):
    if st.sidebar.button(label, key=label):
        return selected_page_name
    return selected_page

def main():
    st.sidebar.title("Menu")

    # Membuat instance dari setiap halaman
    home_page = HomePage()
    obesity_page = ObesityPage()
    calories_page = CaloriesPage()
    skin_page = SkinPage()
    about_page = AboutPage()

    # Mendefinisikan berbagai halaman dalam dictionary
    pages = {
        "Home": home_page,
        "Obesitas": obesity_page,
        "Kalkulator Kebutuhan Kalori": calories_page,
        "Klasifikasi Penyakit Kulit": skin_page,
        "Tentang Aplikasi": about_page
    }

    # Mengatur halaman default ke "Home" jika belum ada yang dipilih
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Home"

    # Menyimpan nama halaman yang saat ini dipilih
    selected_page = st.session_state.selected_page

    # Membuat tombol di sidebar
    selected_page = sidebar_button("🏠 Home                          ", "Home", selected_page)
    selected_page = sidebar_button("🧑‍⚕️ Obesitas                     ", "Obesitas", selected_page)
    selected_page = sidebar_button("🔥 Kalori                          ", "Kalkulator Kebutuhan Kalori", selected_page)
    selected_page = sidebar_button("🩺 Penyakit Kulit             ", "Klasifikasi Penyakit Kulit", selected_page)
    selected_page = sidebar_button("ℹ️ Tentang Aplikasi         ", "Tentang Aplikasi", selected_page)

    # Menyimpan halaman yang dipilih ke dalam session state jika ada perubahan
    if selected_page != st.session_state.selected_page:
        st.session_state.selected_page = selected_page

    # Menampilkan halaman yang dipilih
    pages[st.session_state.selected_page].display()

if __name__ == "__main__":
    main()
