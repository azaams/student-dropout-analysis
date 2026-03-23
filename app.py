import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Jaya Jaya Institut - Dropout Prediction", layout="wide")

st.title("Sistem Deteksi Dini Dropout Mahasiswa")
st.markdown("Aplikasi ini dibuat untuk membantu tim HR dan Manajemen Jaya Jaya Institut dalam memprediksi probabilitas mahasiswa yang berisiko dropout berdasarkan data akademik dan demografi.")

@st.cache_resource
def load_model():
    return joblib.load('model/model.joblib')

try:
    model = load_model()
    st.success("Model Machine Learning berhasil dimuat dan siap digunakan.")
except FileNotFoundError:
    st.error("File 'model.joblib' tidak ditemukan. Pastikan Anda telah melatih dan menyimpan model dari notebook.")
    st.stop()

st.subheader("Unggah Data Mahasiswa")
st.markdown("Silakan unggah file CSV yang berisi data mahasiswa. Pastikan format kolom sesuai dengan dataset asli.")

uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, delimiter=';')
        if len(df.columns) == 1:
            df = pd.read_csv(uploaded_file, delimiter=',')
            
        st.write("Preview Data yang Diunggah:")
        st.dataframe(df.head())
        
        # Tombol Prediksi
        if st.button("Jalankan Prediksi"):
            with st.spinner('Sedang memproses prediksi...'):
                if 'Status' in df.columns:
                    X_predict = df.drop(columns=['Status'])
                else:
                    X_predict = df.copy()
                
                
                predictions = model.predict(X_predict)
                
                df_result = df.copy()
                df_result['Prediksi_Status'] = ["Dropout" if p == 1 else "Graduate" for p in predictions]
                
                st.subheader("Hasil Prediksi")
                
                total_dropout = len(df_result[df_result['Prediksi_Status'] == 'Dropout'])
                total_graduate = len(df_result[df_result['Prediksi_Status'] == 'Graduate'])
                
                col1, col2 = st.columns(2)
                col1.metric("Prediksi Dropout", total_dropout)
                col2.metric("Prediksi Lulus (Graduate)", total_graduate)
                
                st.dataframe(df_result)
                
                csv_result = df_result.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Unduh Hasil Prediksi (CSV)",
                    data=csv_result,
                    file_name='hasil_prediksi_dropout.csv',
                    mime='text/csv',
                )
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses data: {e}")