import streamlit as st
from classes.skin_disease_classifier import SkinDiseaseClassifier
from PIL import Image

class SkinPage:
    def __init__(self):
        self.title = "Klasifikasi Penyakit Kulit"

    def display(self):
        st.title(self.title)

        if 'page' not in st.session_state:
            st.session_state.page = 'info'

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Informasi tentang Penyakit Kulit", key="info_button"):
                st.session_state.page = "info"

        with col2:
            if st.button("Prediksi Gambar Penyakit Kulit", key="predict_button"):
                st.session_state.page = "predict"

        if st.session_state.page == "info":
            self.display_info()
        elif st.session_state.page == "predict":
            self.predict_skin_disease()

    def display_info(self):
        st.header("Informasi tentang Penyakit Kulit 🩺")
        st.write("""
            Teknologi machine learning dapat digunakan untuk mendiagnosis dan memprediksi penyakit kulit berdasarkan 
            gambar dan data pasien. Beberapa penyakit kulit yang umum diprediksi meliputi:
            - **Actinic keratosis**
            - **Atopic Dermatitis**
            - **Benign keratosis**
            - **Dermatofibroma**
            - **Melanocytic nevus**
            - **Melanoma**
            - **Squamous cell carcinoma**
            - **Tinea Ringworm Candidiasis**
            - **Vascular lesion**
            
            Model machine learning dapat dilatih menggunakan dataset gambar kulit yang telah diberi label untuk 
            mengenali pola dan gejala yang terkait dengan penyakit tertentu. Dengan demikian, pasien dapat 
            mendapatkan diagnosis awal yang lebih cepat dan akurat.

            Penting untuk diingat bahwa meskipun teknologi ini menjanjikan, konsultasi dengan dokter kulit tetap 
            diperlukan untuk diagnosis dan perawatan yang tepat.
        """)

    def predict_skin_disease(self):
        model_path = 'model/model_quantized.tflite'
        label_path = 'model/labels.txt'
        classifier = SkinDiseaseClassifier(model_path, label_path)

        uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            class_name, confidence_score = classifier.classify_image(image)

            st.write(f"Prediksi Kelas: **{class_name}**")
            st.write(f"Skor Kepercayaan: **{confidence_score:.2f}**")
            st.image(image, caption='Gambar yang Diupload', width=300)
